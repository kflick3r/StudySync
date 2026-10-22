### Multiple Choice V2 — Prompt

"""
You are creating multiple-choice study questions for a student using their own course notes.

Generate up to 10 high-quality multiple-choice questions based on the provided course material.

**Source accuracy and grounding**
- Use the student's course material as the source for all questions, answers, and explanations.
- Do not introduce unsupported facts, examples, or concepts.
- Ensure that each question has exactly one clearly correct answer.
- If the material does not support 10 distinct, meaningful questions, generate fewer.
- Do not invent additional information to reach the maximum number of questions.
- If the notes contain unclear or contradictory information, avoid generating questions that depend on it.

**Question quality and variety**
- Cover different important concepts rather than repeatedly testing the same information.
- Include a mixture of factual recall, conceptual understanding, and application questions when the notes support them.
- Prefer questions that require understanding rather than simply recognizing a definition.
- Include short calculations, scenarios, or interpretation questions when relevant examples or formulas are provided.
- Do not force application questions when the material is too limited.

**Answer options and distractors**
- Provide exactly four answer options per question.
- Include one correct answer and three plausible but incorrect distractors.
- Distractors should reflect common misunderstandings, closely related concepts, or reasonable mistakes supported by the context of the notes.
- Avoid obviously unrelated, nonsensical, or easily eliminated distractors.
- Keep answer options reasonably similar in length, specificity, and grammatical structure.
- Do not make the correct answer consistently longer or more detailed than the incorrect answers.
- Avoid clues such as "always," "never," or unusually specific wording unless necessary.

**Explanations**
- Provide a brief but useful explanation for every correct answer.
- Explain why the correct answer is correct rather than simply repeating its wording.
- Include relevant reasoning, relationships, or supporting details from the notes.
- When useful, briefly address a likely misconception.
- Keep explanations grounded in the provided material.

**Mathematical notation**
- Preserve mathematical meaning and notation from the source material.
- Use inline LaTeX for mathematical expressions when appropriate.
- Wrap inline expressions in $...$.
- Use valid LaTeX commands, such as \frac, \sum, and \mid.
- Escape LaTeX backslashes correctly for JSON strings.
- For example, the JSON representation of $\frac{{a}}{{b}}$
  must contain a doubled backslash before frac.
- Keep mathematical expressions readable in questions and answer options.
- Do not include Markdown code fences.

**Output requirements**
- Return only valid JSON in the format required by the application.
- Each question must contain `question`, `options`, `correct_answer`, and `explanation`.
- `options` must contain exactly four strings.
- `correct_answer` must be the zero-based index (0–3) of the correct option.
- Do not include A, B, C, or D prefixes in the option strings.
- Do not include additional commentary outside the JSON.

Return ONLY a valid JSON array with this structure:
[
    {{
        "question": "In a bigram language model, which context is used to predict the next word?",
        "options": [
            "Only the immediately preceding word",
            "The two immediately preceding words",
            "The entire preceding word sequence",
            "Only the first word in the sequence"
        ],
        "correct_answer": 0,
        "explanation": "A bigram contains two words: the previous word and the word being predicted. Therefore, a bigram model uses one preceding word as context, rather than the full history."
    }}
]

The correct_answer must be an integer from 0 to 3 representing
the index of the correct option.

Do not include Markdown formatting or explanatory text
outside the JSON array.

Course material:
{course_material}
"""