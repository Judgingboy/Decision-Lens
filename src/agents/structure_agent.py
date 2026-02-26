import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise RuntimeError("OPENAI_API_KEY not found in environment")

client = OpenAI(api_key=API_KEY)


STRUCTURE_SYSTEM_PROMPT = """
You are an assistive decision-structuring agent.

Your role is to HELP the user structure a decision problem.
You DO NOT make decisions.

You must PRODUCE A DRAFT STRUCTURE that the USER will review and confirm.

Your responsibilities are to SUGGEST:
- The decision goal
- A list of options
- A list of evaluation criteria

For EACH criterion you MUST:
- Classify it as either:
  • "benefit" (higher values are better), or
  • "cost" (lower values are better)

- If the criterion is QUALITATIVE:
  • You MUST provide an explicit ordinal scale
  • The scale MUST be ordered from lowest → highest
  • Example: ["cheap", "affordable", "expensive"]

- If the criterion is NUMERIC:
  • You MUST specify a unit (e.g. "USD", "grams", "hours")
  • You MUST NOT provide a scale

- Extract raw numeric values when the user provides numbers
- Use descriptive terms ONLY if numeric values are not available
- Use "unknown" when information is missing

IMPORTANT:
- All cost/benefit classifications are PROVISIONAL
- The user will confirm or edit them
- Prefer being explicit over being brief

You MUST NOT:
- Assign weights
- Score options
- Rank options
- Convert descriptors into numbers
- Recommend any option

Output ONLY valid JSON matching the schema.
Do not include explanations outside the JSON.
"""


STRUCTURE_SCHEMA_DESCRIPTION = """
Return JSON in the following format:

{
  "decision_goal": string,

  "criteria": {
    "<criterion_name>": {
      "type": "benefit | cost",

      // REQUIRED for qualitative criteria
      // Ordered from lowest to highest
      "scale": [string],

      // REQUIRED for numeric criteria
      // e.g. "USD", "grams", "hours"
      "unit": string | null,

      "description": string
    }
  },

  "options": {
    "<option_name>": {
      "<criterion_name>": number | string | "unknown"
    }
  },

  "assumptions": [string],
  "unknowns": [string]
}
"""


def structure_decision(user_input: str) -> dict:
    """
    Converts natural language decision input into structured attributes.
    """

    last_error = None

    for attempt in range(2):  # one retry
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            temperature=0.2,
            response_format={"type": "json_object"},    #FORCE JSON OUTPUT
            messages=[
                {"role": "system", "content": STRUCTURE_SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": f"""
User decision description:
\"\"\"{user_input}\"\"\"

{STRUCTURE_SCHEMA_DESCRIPTION}

IMPORTANT:
- Output ONLY valid JSON
- No comments
- No trailing commas
- No explanations
"""
                }
            ],
        )

        content = response.choices[0].message.content.strip()

        try:
            return json.loads(content)
        except json.JSONDecodeError as e:
            last_error = e
            # Retry with stronger instruction
            user_input += (
                "\n\nNOTE: Your previous response was invalid JSON. "
                "Return ONLY valid JSON matching the schema."
            )

    raise ValueError("Structure Agent returned invalid JSON") from last_error