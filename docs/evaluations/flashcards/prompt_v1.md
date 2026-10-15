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