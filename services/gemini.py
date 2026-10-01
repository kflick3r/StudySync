import streamlit as st
from google import genai


def generate_review_guide(course_material):
    """Generate a review guide from the user's course material."""

    client = genai.Client(
        api_key=st.secrets["GEMINI_API_KEY"]
    )

    prompt = f"""
You are an AI study assistant helping a college student study
Natural Language Processing.

Create a clear review guide from the course material provided below.

Requirements:
- Use only information supported by the provided course material.
- Do not invent facts or add outside information.
- Identify and organize the major concepts, definitions, relationships,
  and important details.
- Use clear headings and concise explanations.
- Preserve important distinctions between related concepts.
- Write the guide for a student studying an NLP course.
- If the notes are unclear or incomplete, do not guess. Indicate that
  the information is unclear or missing.

Course material:
{course_material}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text