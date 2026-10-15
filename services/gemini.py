import re
from urllib.parse import quote_plus

import streamlit as st
from google import genai

import json

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


# -------------------------------
# Gemini Prompt for Review Guide
# -------------------------------

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
- Identify and organize the major concepts, definitions, relationships, examples, and important supporting details.
- Preserve important examples when they help explain or distinguish a concept.
- Preserve technical details accurately, including mathematical formulas, notation, symbols, operators, and terminology.
- Do not change the meaning of technical statements when summarizing.
- Preserve important distinctions between related concepts.
- Use clear headings and concise explanations.
- Write the guide for a student studying an NLP course.
- If the notes are unclear or incomplete, do not guess. Indicate that the information is unclear or missing.


IMPORTANT — FACTUAL ACCURACY REVIEW:

After generating the review guide, independently examine the original course material for potential factual inaccuracies.

This review is intended to identify meaningful factual concerns, not to find errors in every set of notes.

A result of ZERO flagged statements is completely acceptable.

Only flag a statement when:
- It makes a specific factual claim that appears inaccurate.
- It directly contradicts another statement in the notes.
- It contains a technical or mathematical error that materially changes the meaning of the concept.

Do NOT flag a statement simply because:
- It is simplified for educational purposes.
- It omits additional details or context.
- It uses different terminology than you would prefer.
- It could be explained more thoroughly.
- It discusses a complex topic with multiple valid interpretations.
- You are uncertain whether it is correct.
- You need to populate the review section.

For each potential error, you must be able to identify a specific reason the statement warrants verification.

If you cannot identify a specific factual concern, do not flag the statement.

Do not introduce outside information into the review guide.
You may use your existing knowledge to recognize potential factual concerns, but treat these as unverified suspicions, not established corrections.

Do not provide corrected answers based on your own knowledge. The student should independently verify the information.

OUTPUT FORMAT:

If one or more meaningful potential inaccuracies are found, include a final section titled:

## Notes to Review for Correctness

For each flagged statement:
1. Quote the exact statement from the original notes.
2. Briefly explain the specific factual concern.
3. Provide a concise search topic for independent verification.
4. Write the search topic on its own line in this exact format:

**Suggested verification topic:** [search topic]

Do not create hyperlinks yourself.
Include only one verification topic per flagged statement.
Do not repeat verification topics.

If no meaningful potential inaccuracies are identified, include the section with only this sentence:

"No potential factual inaccuracies identified in the provided notes."

Do not invent concerns to populate this section.

Course material:
{course_material}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    review_guide = response.text

    return add_verification_links(review_guide)


# -----------------------------
# Gemini Prompt for Flashcards
# JSON construction approach developed with AI assistance
# -----------------------------


def generate_flashcards(course_material):
    """Generate flashcards from the user's course material."""

    client = genai.Client(
        api_key=st.secrets["GEMINI_API_KEY"]
    )

    prompt = f"""
You are an AI study assistant helping a college student study Natural Language Processing.

Create 10 flashcards from the provided course material.

Requirements:
- Use only information supported by the course material.
- Do not invent facts or introduce outside information.
- Focus on important concepts, definitions, relationships, examples, and technical details.
- Include a mix of definition, conceptual, and application questions.
- Each flashcard should test one clear concept.
- Keep answers concise but sufficiently detailed.
- Preserve technical terminology and mathematical notation.
- Avoid duplicate or nearly identical questions.
- Do not generate questions that cannot be answered from the provided material.
- If there is insufficient material for 10 distinct flashcards, generate fewer rather than inventing content.

Flashcard design:
- Generate up to 10 flashcards, depending on the amount of meaningful information in the notes.
- Each flashcard should test one specific learning objective.
- Do not combine multiple unrelated questions into one card.
- Avoid questions that substantially duplicate another card.
- Include factual recall, conceptual understanding, comparisons, and application questions when the
  source material supports them.
- A comparison question may address two related concepts when understanding their relationship is the objective.
- Prioritize important concepts over minor isolated facts.
- Keep answers concise enough for flashcard-based studying.
- Do not invent examples or applications unsupported by the notes.


Return ONLY a valid JSON array with this structure:
[
    {{
        "question": "What is tokenization?",
        "answer": "The process of splitting text into tokens."
    }},
    {{
        "question": "What is an n-gram?",
        "answer": "A sequence of n consecutive tokens."
    }}
]
Do not include Markdown formatting or explanatory text
outside the JSON array.

Course material:
{course_material}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
        config={
            "response_mime_type": "application/json"
        }
    )

    flashcards = json.loads(response.text)

    if not isinstance(flashcards, list):
        raise ValueError("Gemini did not return a list of flashcards.")

    for card in flashcards:
        if not isinstance(card, dict):
            raise ValueError("Invalid flashcard format.")

        if (
            not isinstance(card.get("question"), str)
            or not isinstance(card.get("answer"), str)
            or not card["question"].strip()
            or not card["answer"].strip()
        ):
            raise ValueError(
                "Each flashcard must contain a non-empty question and answer."
            )

    return flashcards
