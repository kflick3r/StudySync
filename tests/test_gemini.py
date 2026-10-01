import streamlit as st
from google import genai

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="In one sentence, explain what tokenization means in NLP."
)

print(response.text)