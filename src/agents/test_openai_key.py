# This is a simple test script to verify that the OpenAI API key is working correctly.
# use this to debug any issues with the API key before running the full application.
#This is no way part of the actual application logic.

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