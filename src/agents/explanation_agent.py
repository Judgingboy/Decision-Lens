import os
from dotenv import load_dotenv
from openai import OpenAI
from typing import Dict
import json
# Load environment variables
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise RuntimeError("OPENAI_API_KEY not found in environment")

client = OpenAI(api_key=API_KEY)

SYSTEM_PROMPT = """
You are an Explanation Agent for a decision-support system.

Your job is to explain the ranking in a way that a non-technical user can easily understand.

STRICT RULES (DO NOT BREAK):
- Use ONLY the information provided in the explanation payload.
- Do NOT introduce new criteria, assumptions, or opinions.
- Do NOT change rankings, scores, or weights.
- Do NOT speculate about missing data.
- If something was not used in the decision, say so clearly.
- Never sound like a technical report or system log.

STYLE & TONE:
- Plain language
- Calm and honest
- Short sentences
- Cause-and-effect explanations (“because”, “mainly due to”)
- Speak directly to the user
- Neutral and non-judgmental

HOW TO EXPLAIN:
- Focus on WHAT mattered and WHY
- Do NOT repeat all numbers unless necessary
- Mention user priorities if they were available but not used
- Clearly separate “used” vs “missing” information

OUTPUT STRUCTURE (MANDATORY):
1. Short summary (1–2 sentences, high level)
2. Why the top option ranked highest (plain reasoning)
3. Why the other options ranked lower (brief comparison)
4. What information was missing or not used (and why that matters)

Write as if you are calmly walking the user through the result.
"""


def render_explanation(explanation_payload: Dict) -> str:
    """
    Converts a deterministic explanation payload into
    a natural-language explanation using OpenAI.

    This function MUST NOT alter payload content.
    """

    user_prompt = f"""
Here is the explanation payload from the decision engine:

{json.dumps(explanation_payload, indent=2)}

Explain the ranking to the user.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.2
    )

    return response.choices[0].message.content.strip()










