import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🎭 Shakespeare AI")

play = st.text_input("Enter Play Name", "Julius Caesar")
act = st.number_input("Act", min_value=1, value=1)
scene = st.number_input("Scene", min_value=1, value=1)

if st.button("Explain Scene"):

    prompt = f"""
You are an expert Shakespeare teacher.

Explain {play} Act {act} Scene {scene} line by line.

Rules:
1. First write the original dialogue exactly as it appears in Shakespeare's text.
2. Immediately below it write:

Meaning:

3. Explain in simple modern English.
4. Explain difficult words, metaphors and references.
5. Do not skip any dialogue.
6. Preserve speaker names.

Example:

BRUTUS:
I do fear the people choose Caesar for their king.

Meaning:
Brutus is worried that the Roman people may make Caesar their king.

Now explain the entire scene.
"""

    response = model.generate_content(prompt)

    st.markdown(response.text)