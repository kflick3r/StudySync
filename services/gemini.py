import re
from urllib.parse import quote_plus

import streamlit as st
from google import genai

import json
import random


# The Gemini model used by every generator. Change it here to
# switch models everywhere.
GEMINI_MODEL = "gemini-3.5-flash-lite"


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
        model=GEMINI_MODEL,
        contents=prompt
    )

    # Gemini can return nothing (for example, if a safety filter blocks
    # the response). In that case response.text is None, so stop here
    # with a clear message instead of failing later with a confusing one.
    if not response.text or not response.text.strip():
        raise ValueError(
            "Gemini returned an empty response. Please try again."
        )
    
    review_guide = response.text

    return add_verification_links(review_guide)


# -----------------------------
# Gemini Prompt for Flashcards
# JSON construction approach developed with AI assistance
# -----------------------------

# Helper function 
# Validation check for generated flashcards
def is_valid_flashcard(card):
    """Return True if a flashcard has a non-empty question and answer."""

    # Each flashcard must be a dictionary (a JSON object)
    if not isinstance(card, dict):
        return False

    question = card.get("question")
    answer = card.get("answer")

    # Both fields must be strings with something other than spaces in them
    return (
        isinstance(question, str) and bool(question.strip())
        and isinstance(answer, str) and bool(answer.strip())
    )


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
        model=GEMINI_MODEL,
        contents=prompt,
        config={
            "response_mime_type": "application/json"
        }
    )

    flashcards = json.loads(response.text)

    if not isinstance(flashcards, list):
        raise ValueError("Gemini did not return a list of flashcards.")

    # Keep only the valid flashcards, and cap the list at 10.
    # One bad card no longer discards the whole batch.
    flashcards = [c for c in flashcards if is_valid_flashcard(c)][:10]

    # Only fail if nothing usable is left
    if not flashcards:
        raise ValueError(
            "Gemini didn't return any valid flashcards. Please try again."
        )

    return flashcards


# ---------------------------------------------------------
# Gemini Prompt for Multiple Choice Questions
# JSON construction approach developed with AI assistance
# ---------------------------------------------------------

# Helper functions

# Validation check for LaTeX delimiters
def has_valid_math_delimiters(text):
    """Check that inline LaTeX math delimiters are balanced."""
    if not isinstance(text, str):
        return False

    # Count only dollar signs that are not escaped
    dollar_count = 0

    for i, char in enumerate(text):
        if char == "$":
            backslashes = 0
            j = i - 1

            while j >= 0 and text[j] == "\\":
                backslashes += 1
                j -= 1

            if backslashes % 2 == 0:
                dollar_count += 1

    return dollar_count % 2 == 0
 
# Validation check for generated questions
def is_valid_question(question):
    """Return True if a question has the structure the quiz page expects."""

    # Each question must be a dictionary (a JSON object)
    if not isinstance(question, dict):
        return False

    text = question.get("question")
    explanation = question.get("explanation")

    # The question and explanation must be non-empty strings
    if (
        not isinstance(text, str) or not text.strip()
        or not isinstance(explanation, str) or not explanation.strip()
    ):
        return False

    options = question.get("options")

    # There must be exactly four options, and each must be a
    # non-empty string
    if (
        not isinstance(options, list)
        or len(options) != 4
        or any(not isinstance(o, str) or not o.strip() for o in options)
    ):
        return False

    # All four options must be different from each other, ignoring
    # extra spaces and capitalization. A set removes duplicates, so if
    # it has fewer than 4 items, at least two options matched.
    if len({o.strip().casefold() for o in options}) != 4:
        return False

    correct_answer = question.get("correct_answer")

    # The correct answer must be an integer from 0 to 3. 
    # Checking type(...) is int also rejects True/False,
    # which Python would otherwise treat as the numbers 1 and 0
    if type(correct_answer) is not int or not 0 <= correct_answer <= 3:
        return False

    # Check LaTeX delimiters in the question, options, and explanation
    texts = [text, *options, explanation]

    if not all(has_valid_math_delimiters(t) for t in texts):
        return False

    return True


def generate_multiple_choice(course_material):
    """Generate multiple-choice questions from course material."""

    client = genai.Client(
        api_key=st.secrets["GEMINI_API_KEY"]
    )

    
    prompt = rf"""
You are an AI study assistant creating multiple-choice questions
from a college student's course notes.

Generate up to 10 high-quality multiple-choice questions using
only the provided course material.

SOURCE ACCURACY
- Every question, correct answer, distractor, and explanation must
  be consistent with the supplied notes.
- Do not introduce unsupported facts, examples, or concepts.
- Each question must have exactly one defensible correct answer.
- Avoid material that is unclear, contradictory, or insufficiently explained.
- Generate fewer than 10 questions if the notes do not support
  10 distinct, meaningful questions.

QUESTION PLANNING AND COVERAGE
Before writing questions, internally identify the distinct learning
objectives supported by the notes.

Select up to 10 objectives that provide broad coverage of the most
important concepts, relationships, examples, and formulas.

- Generate no more than one question per learning objective.
- Treat equivalent definitions, formulas, and notations as one
  objective unless they require meaningfully different reasoning.
- Prioritize covering different important concepts over generating
  multiple variations of the same question.
- Include factual recall, conceptual understanding, comparison,
  interpretation, and application when supported by the notes.
- When both a recall question and an application question could
  test the same objective, prefer the application question if
  the notes provide enough information.
- When the notes contain worked numerical examples or formulas,
  include at least one question requiring application, provided
  a clear answer can be determined.
- Do not invent scenarios or numerical information that cannot
  be justified from the notes.

DISTRACTOR DESIGN
For each question, internally identify likely misunderstandings
or reasoning mistakes a student might make.

Use these to create three plausible but incorrect answer options.

- Prefer distractors based on confused concepts, incorrect
  relationships, calculation mistakes, or misapplied formulas.
- For mathematical questions, consider realistic errors such as
  incorrect signs, substitutions, or rearrangements.
- Avoid unrelated concepts, nonsensical claims, and answers that
  can be eliminated without understanding the material.
- Make all four options similar in length, detail, and structure.
- Do not make the correct answer stand out through wording,
  specificity, or formatting.
- Ensure every distractor is clearly incorrect based on the notes.
- Do not use "All of the above" or "None of the above."

EXPLANATIONS
For every question, provide a concise explanation of the correct answer.

- Explain the reasoning rather than simply restating the answer.
- Include a relevant relationship, distinction, or calculation
  step when supported by the notes.
- When useful, explain why a likely misconception is incorrect.
- Keep explanations to approximately 1–3 sentences.
- Do not add unsupported information.

MATHEMATICAL NOTATION
- Use LaTeX only when mathematical notation improves readability.
- Wrap every mathematical expression in single dollar-sign
  delimiters, such as $p(X)$ or $z = w \cdot x + b$.
- Never output raw LaTeX commands outside math delimiters.
- Preserve subscripts, superscripts, fractions, and probability notation.
- Escape LaTeX backslashes correctly inside JSON strings.
- Do not use Markdown code fences or display-math delimiters.

FINAL QUALITY CHECK
Before returning the questions, internally verify that:
- Each question tests a distinct learning objective.
- Important concepts are not unnecessarily omitted in favor
  of repeated questions about the same concept.
- Exactly one answer is correct.
- All three distractors represent plausible misunderstandings
  or reasoning errors.
- The correct answer is not identifiable from answer length alone.
- The explanation provides useful reasoning.
- All content is supported by the notes.
- All mathematical notation is correctly formatted.

OUTPUT FORMAT
Return ONLY a valid JSON array.

Each object must contain:
- "question": a nonempty string
- "options": exactly four nonempty strings
- "correct_answer": an integer from 0 to 3
- "explanation": a nonempty string

Do not prefix answer options with A, B, C, or D.
Do not include commentary or Markdown outside the JSON.

The following example illustrates the required JSON structure
and explanation style. Do not use its subject matter unless
it is supported by the student's notes.

Example:
[
    {{
        "question": "If a binary classifier lowers its decision threshold from 0.5 to 0.2, what happens to its positive predictions?",
        "options": [
            "More observations may be classified as positive",
            "Fewer observations may be classified as positive",
            "The predicted probabilities automatically increase",
            "The model's learned coefficients are recalculated"
        ],
        "correct_answer": 0,
        "explanation": "Lowering the threshold means an observation needs a smaller predicted probability to be classified as positive. This can increase the number of positive predictions without changing the model's predicted probabilities."
    }}
]

Course material:
{course_material}
"""


    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config={
            "response_mime_type": "application/json"
        }
    )

    # Convert Gemini's JSON text into a Python list
    questions = json.loads(response.text)

    # Make sure we got a list before filtering it
    if not isinstance(questions, list):
        raise ValueError("Gemini did not return a list of questions.")

    # Keep only the questions that pass validation, and cap the list
    # at 10. One bad question no longer discards the whole batch.
    questions = [q for q in questions if is_valid_question(q)][:10]

    # Only fail if nothing usable is left
    if not questions:
        raise ValueError(
            "Gemini didn't return any valid questions. Please try again."
        )

    # Shuffle the answer options so the correct answer isn't always
    # in the same position.
    for question in questions:

        # Remember the correct answer's text, because shuffling will
        # change which position it ends up in
        correct_text = question["options"][question["correct_answer"]]

        random.shuffle(question["options"])

        # Find where the correct answer landed and update the index.
        # This is safe because validation guarantees the options are
        # all different.
        question["correct_answer"] = question["options"].index(correct_text)

    return questions
