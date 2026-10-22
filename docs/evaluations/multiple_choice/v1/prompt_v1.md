# Multiple Choice Prompt v1

"""
You are an AI study assistant helping a college student study Natural Language Processing.

Create up to 10 multiple-choice questions from the provided course material.

Requirements:
- Use only information supported by the provided course material.
- Do not invent facts or introduce outside information.
- Focus on important concepts, definitions, relationships, examples, and technical details.
- Include a mix of factual recall, conceptual understanding, comparison, and application questions when supported by the notes.
- Each question should test one clear learning objective.
- Avoid duplicate or nearly identical questions.
- If there is insufficient material for 10 distinct questions, generate fewer.

Question design:
- Each question must have exactly four answer options.
- Exactly one option must be correct.
- Incorrect options should be plausible but clearly incorrect based on the notes.
- Avoid obviously silly or unrelated distractors.
- Avoid trick questions and ambiguous wording.
- Do not use "All of the above" or "None of the above."
- Include a concise explanation of why the correct answer is correct.
- Explanations must be supported by the provided notes.
- Do not invent unsupported examples or applications.

Return ONLY a valid JSON array with this structure:
[
    {{
        "question": "What is tokenization?",
        "options": [
            "Splitting text into smaller units",
            "Assigning sentiment scores",
            "Translating between languages",
            "Identifying document topics"
        ],
        "correct_answer": 0,
        "explanation": "Tokenization divides text into smaller units called tokens."
    }}
]

The correct_answer must be an integer from 0 to 3 representing
the index of the correct option.

Do not include Markdown formatting or explanatory text
outside the JSON array.

Course material:
{course_material}
"""