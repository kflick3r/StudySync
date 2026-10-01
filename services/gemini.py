import re
from urllib.parse import quote_plus

import streamlit as st
from google import genai


# ------------------------
# URL generation
# URL construction approach developed with AI assistance
# ------------------------

def create_google_search_link(search_topic):
    query = quote_plus(search_topic)
    return f"https://www.google.com/search?q={query}"


def add_verification_links(review_guide):
    pattern = r"\*\*Suggested verification topic:\*\*\s*(.+)"

    def replace_topic(match):
        search_topic = match.group(1).strip()
        url = create_google_search_link(search_topic)

        return f"**Suggested verification:** [{search_topic}]({url})"

    return re.sub(pattern, replace_topic, review_guide)


# ------------------------
# Gemini Prompt
# ------------------------

def generate_review_guide(course_material):
    """Generate a review guide from the user's course material."""

    client = genai.Client(
        api_key=st.secrets["GEMINI_API_KEY"]
    )

    prompt = f"""
You are an AI study assistant helping a college student study Natural Language Processing.

Create a clear review guide from the course material provided below.

Requirements:
- Use only information supported by the provided course material.
- Do not invent facts or add outside information.
- Identify and organize the major concepts, definitions, relationships,
  examples, and important supporting details.
- Preserve important examples when they help explain or distinguish a concept.
- Preserve technical details accurately, including mathematical formulas,
  notation, symbols, operators, and terminology.
- Do not change the meaning of technical statements when summarizing.
- Preserve important distinctions between related concepts.
- Use clear headings and concise explanations.
- Write the guide for a student studying an NLP course.
- If the notes are unclear or incomplete, do not guess. Indicate that
  the information is unclear or missing.

IMPORTANT:
If the provided course material contains a statement that appears
potentially incorrect, contradictory, or unclear, do not silently correct it.

Instead, include a final section titled:

## Notes to Review for Correctness

For each potentially incorrect or unclear statement:
1. Quote or closely reproduce the relevant statement from the notes.
2. Explain briefly why the statement may need verification.
   Focus on contradictions, ambiguity, or conflicts within the provided 
   course material. Do not provide a corrected answer unless the 
   provided course material itself establishes the correction.
3. Provide a concise search topic that the student can use to verify the statement using a trusted external source.
4. Write the search topic on its own line in this exact format:

**Suggested verification topic:** [search topic]

Important formatting rules:
- Write the search topic as plain text.
- Do not create a hyperlink yourself.
- Include only one Suggested verification topic for each flagged statement.
- Do not repeat the same verification topic.

Do not claim that a statement is definitely wrong unless the provided 
course material itself establishes that it is wrong.

Do not flag a statement merely because it is technical, unfamiliar, 
or incomplete. Only flag statements when there is a meaningful reason 
that the student should verify it.

Course material:
{course_material}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    review_guide = response.text

    return add_verification_links(review_guide)
