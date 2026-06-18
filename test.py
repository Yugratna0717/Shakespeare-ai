from google import genai
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("GEMINI_API_KEY")
print("1. API Key Found:", api_key is not None)

client = genai.Client(api_key=api_key)

prompt = """
You are an expert Shakespeare teacher.
Explain Julius Caesar Act 1 Scene 1 in simple English.
Keep it brief.
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print("2. API Working:", bool(response.text))
print("3. Response Preview:", response.text[:200])