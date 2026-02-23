from dotenv import load_dotenv
import os
from openai import OpenAI

# Load .env
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY not found")

# Create client
client = OpenAI(api_key=api_key)

# Make a tiny test request
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Tell me a Programming Pickup Line."}
    ],
    temperature=0
)

print(response.choices[0].message.content)