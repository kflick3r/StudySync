# Flashcards: Development & Evaluation

## Overview

Flashcards is StudySync's second AI-powered study tool. It uses Google's Gemini API to transform NLP course materials into questions and answers that support active recall.

Unlike the Review Guide, which organizes and summarizes information, Flashcards encourages students to retrieve concepts from memory.

Development focused on three goals:

- Generate relevant, accurate flashcards grounded in student-provided notes.
- Balance topic coverage with focused, non-repetitive questions.
- Create an interactive study experience that supports repeated review.

## Implementation

Flashcards was built using Python, Streamlit, and the Gemini API.

Gemini generates up to ten question-and-answer pairs in structured JSON format. The application stores these flashcards in Streamlit's session state, allowing students to review their deck without additional API requests.

The interface includes:

- **Generate Flashcards:** Creates a deck from submitted notes.
- **Reveal/Hide Answer:** Supports active recall before revealing the answer.
- **Previous/Next:** Allows navigation between cards.
- **Shuffle:** Randomizes the existing deck without regenerating it.
- **Session Management:** Preserves the deck during navigation and resets it when new material is submitted.

Additional interface improvements included centered flashcard content, clearer navigation, and consistent spacing.

## Prompt Development

During development, I experimented with several prompt revisions to balance coverage, question quality, and repetition.

The initial prompt generated ten flashcards but included repetitive questions. A later revision reduced redundancy but became overly restrictive, generating only four cards from the same material.

The final V1 prompt attempts to balance these requirements while ensuring questions remain grounded in the original notes.

Although several prompt revisions were tested, **Flashcards V1 represents the first functional baseline**, rather than a series of separately evaluated releases.

## Initial Evaluation

I tested Flashcards V1 using two sets of NLP course notes, evaluating accuracy, topic coverage, clarity, redundancy, and usefulness for active recall.

### Test 1 — Foundational NLP Concepts

The first test used shorter notes covering tokenization, n-grams, stemming, and lemmatization.

**Results:** Seven flashcards generated.

The final prompt covered the major concepts without the excessive repetition observed during earlier prompt experiments.

This test helped establish the initial balance between coverage and redundancy.

### Test 2 — Word Embeddings & Information Retrieval

The second test used longer notes covering word embeddings, Word2Vec, cosine similarity, static embeddings, polysemy, TF-IDF, inverted indexes, and BM25.

**Results:** Ten flashcards generated.

| Criterion | Observation |
|---|---|
| Accuracy | All ten flashcards were consistent with the source notes. |
| Coverage | All eight major concepts were represented. |
| Clarity | Questions and answers were generally clear. |
| Redundancy | Minimal repetition, with some related TF-IDF questions. |
| Active Recall | Supported factual recall, although some questions combined multiple concepts. |

The generated flashcards preserved important technical information and provided broad coverage without obvious unsupported claims.

However, some questions required students to recall several pieces of information at once. Future revisions could prioritize one primary recall target per flashcard.

## Limitations

Flashcards V1 is grounded in student-provided material but does not independently verify its factual accuracy. Incorrect information in the original notes may therefore appear in the generated flashcards.

To address this limitation, I added a notice recommending that students use the Review Guide to identify potentially questionable information before generating flashcards.

Other limitations include:

- Questions primarily test factual recall rather than application or reasoning.
- Some flashcards combine multiple recall targets.
- The ten-card maximum may limit coverage or encourage overly broad questions.
- Testing has been limited to two NLP note samples.

## Reflection & Next Steps

Developing Flashcards reinforced the importance of balancing competing requirements during prompt engineering. Reducing repetition improved question quality, but overly restrictive instructions also reduced the number of generated cards.

I also learned that generating useful content is only one part of developing an effective study tool. Interface design, navigation, and session-state management were equally important to the user experience.

For now, **Flashcards V1 is complete as an initial MVP feature**. It generates relevant study questions, supports repeated review, and provides a straightforward interface.

Future improvements may include more focused questions, adjustable deck sizes, additional testing, and a more systematic evaluation rubric similar to the Review Guide.

The next development priority is the Multiple Choice tool, which will allow students to practice applying their knowledge and receive feedback on their responses.