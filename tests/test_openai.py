import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

response = client.responses.create(
    model="gpt-5.6-luna",
    input="In one sentence, explain what tokenization means in NLP."
)

print(response.output_text)