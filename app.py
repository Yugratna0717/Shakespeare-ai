import streamlit as st
from google import genai
from dotenv import load_dotenv
from pathlib import Path
import os

# Load .env file explicitly
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("GEMINI_API_KEY")

# Streamlit page settings
st.set_page_config(
    page_title="Shakespeare AI",
    page_icon="🎭",
    layout="centered"
)

st.title("🎭 Shakespeare AI")

# Check API key
if not api_key:
    st.error("❌ GEMINI_API_KEY not found.")
    st.stop()

# Gemini client
client = genai.Client(api_key=api_key)

# User inputs
play = st.text_input(
    "Enter Play Name",
    "Julius Caesar"
)

act = st.number_input(
    "Act",
    min_value=1,
    value=1,
    step=1
)

scene = st.number_input(
    "Scene",
    min_value=1,
    value=1,
    step=1
)

# Button
if st.button("Explain Scene"):

    prompt = f"""
You are an expert Shakespeare teacher.

Explain {play} Act {act} Scene {scene} line by line.

Rules:

1. Write the original Shakespeare dialogue.
2. Immediately below it write:

Meaning:

3. Explain in simple modern English.
4. Explain difficult words and metaphors.
5. Preserve speaker names.
6. Do not skip dialogues.
7. If you don't know the exact scene, say:
"I don't have access to the exact text of this scene."

Example:

BRUTUS:
I do fear the people choose Caesar for their king.

Meaning:
Brutus is worried that the Roman people may make Caesar their king.

Now explain the complete scene.
"""

    try:
        with st.spinner("Gemini is thinking..."):

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

        st.success("Explanation generated successfully!")

        st.markdown(response.text)

    except Exception as e:
        st.error(f"Error: {e}")