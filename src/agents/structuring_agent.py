import os
import json
from openai import OpenAI

class StructuringAgent:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            # Ensure the caller has loaded .env before initializing
            raise ValueError("OPENAI_API_KEY environment variable not set.")
        self.client = OpenAI(api_key=api_key)

    def suggest_criteria(self, topic: str) -> list[str]:
        """
        Uses OpenAI to suggest relevant decision criteria for a given topic.
        Returns a list of strings.
        """
        system_prompt = (
            "You are a helpful decision companion. "
            "The user will provide a decision topic. "
            "Return a JSON list of 5-7 relevant evaluation criteria strings. "
            "Do not include markdown formatting or explanations, just the raw JSON list."
        )

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Topic: {topic}"}
                ],
                temperature=0.7
            )
            content = response.choices[0].message.content.strip()
            # Clean up potential markdown code blocks if the model adds them
            if content.startswith("```"):
                content = content.split("\n", 1)[1].rsplit("\n", 1)[0]
            
            return json.loads(content)
        except Exception as e:
            print(f"Error fetching criteria from AI: {e}")
            return []