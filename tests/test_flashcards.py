from services.gemini import generate_flashcards

# Sample NLP course material
sample_notes = """
Tokenization is the process of dividing text into smaller
units called tokens. Tokens may be words, subwords, or
individual characters.

An n-gram is a sequence of n consecutive tokens.
A bigram contains two tokens, while a trigram contains
three tokens.

Stemming reduces words to a common base form by
removing affixes. The resulting stem is not necessarily
a valid dictionary word.

Lemmatization reduces words to their dictionary form,
called a lemma. It often uses morphological information
and part-of-speech information.
"""

print("Generating flashcards...\n")

flashcards = generate_flashcards(sample_notes)

print(f"Generated {len(flashcards)} flashcards.\n")

for i, card in enumerate(flashcards, start=1):
    print(f"Flashcard {i}")
    print(f"Question: {card['question']}")
    print(f"Answer: {card['answer']}")
    print("-" * 40)
