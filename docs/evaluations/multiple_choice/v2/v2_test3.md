StudySync: Multiple Choice V2 — Test 3 Generated Questions
Topic: N-Grams and Language Models
Questions Generated: 6
Source: Short N-Grams and Language Models course notes
Prompt Version: V2
Rendering note: Mathematical expressions in several questions appeared as raw LaTeX in the StudySync interface. The notation below preserves the generated content for evaluation.
Question 1
What is the primary purpose of the chain rule of probability in the context of language models?

A. To decompose the joint probability of a sequence into a product of conditional probabilities
B. To convert raw words into BPE tokens for language computation
C. To approximate word sequences using only the last $N - 1$ words
D. To compute the exact conditional probability of a word given a very long preceding sequence  

Correct Answer: A. To decompose the joint probability of a sequence into a product of conditional probabilities

Explanation: The chain rule of probability conceptually decomposes the joint probability of a sequence into a product of conditional probabilities, such as P(w_{1:n}) = \prod_{k=1}^{n} P(w_k \mid w_{1:k-1}).
Question 2
What is a major limitation of computing the exact probability P(w_n \mid w_{1:n-1}) using the general chain rule without approximations?

A. Language is creative, making it likely that any particular long context has never occurred before in a corpus
B. Conditional probabilities cannot be multiplied together across more than two tokens
C. Tokens like BPE tokens cannot be used with the general formulation
D. It requires looking at least three words into the past, which is computationally expensive  

Correct Answer: A. Language is creative, making it likely that any particular long context has never occurred before in a corpus

Explanation: Computing the exact probability of a word given a very long preceding sequence is infeasible because language is creative and specific long contexts may never have appeared in the training corpus.
Question 3
How many words into the past does a general N-gram model look according to the Markov assumption?

A. N + 1 words
B. N - 1 words
C. Only 1 word regardless of N
D. N words  

Correct Answer: B. N - 1 words

Explanation: A general N-gram model approximates the history by looking N - 1 words into the past, such as a bigram (N=2) looking 1 word back and a trigram (N=3) looking 2 words back.
Question 4
Which of the following notations represents 'all elements of w from w_1 up to and including w_{n-1}'?

A. w_{<n}
B. P(w \mid h)
C. w_{1:n}
D. w_{1:n-1}  

Correct Answer: A. w_{<n}

Explanation: The notation w_{<n} is explicitly defined in the course notes as equivalent notation for all elements of w from w_1 up to and including w_{n-1}.
Question 5
Under the bigram model assumption, how is the conditional probability P(w_n \mid w_{1:n-1}) approximated?

A. P(w_n \mid w_{n-2:n-1})
B. P(w_n \mid w_{n-1})
C. P(w_n \mid w_1)
D. P(w_n \mid w_{1:n})  

Correct Answer: B. P(w_n \mid w_{n-1})

Explanation: A bigram model (N = 2) looks 1 word into the past, approximating the probability as P(w_n \mid w_{n-1}).
Question 6
In practice, what are language models often computed over instead of raw words?

A. Full sentences
B. Character frequencies
C. Tokens like BPE tokens
D. Joint probability tables  

Correct Answer: C. Tokens like BPE tokens

Explanation: The notes state that in practice, language models are often computed over tokens (like BPE tokens) rather than raw words.