StudySync: Multiple Choice V3 — Test 3 Generated Questions
Topic: N-Grams and Language Models
Questions Generated: 7
Source: N-Grams and Language Models course notes
Prompt Version: V3
Question 1
What does the notation $w_{1:n-1}$ represent in the context of word sequences?

A. The sequence of all $n$ words including the final word
B. The joint probability of the entire sequence $w_1$ through $w_n$
C. The conditional probability of the $n$-th word
D. The string of words from $w_1$ up to and including $w_{n-1}$  

Correct Answer: D. The string of words from $w_1$ up to and including $w_{n-1}$

Explanation: The notation $w_{1:n-1}$ represents the string consisting of words $w_1, w_2, \ldots, w_{n-1}$. It is also equivalent to $w_{<n}$.
Question 2
How does the chain rule of probability decompose the joint probability of a word sequence $P(w_{1:n})$?

A. As a product of only the first and last words in the sequence
B. As the product of each word given its entire preceding history
C. As a sum of independent word probabilities
D. As the average probability of all unigrams in the corpus  

Correct Answer: B. As the product of each word given its entire preceding history

Explanation: The chain rule decomposes the joint probability of a sequence into a product of conditional probabilities, specifically $P(w_{1:n}) = \prod_{k=1}^{n} P(w_k \mid w_{1:k-1})$.
Question 3
What is the primary limitation of computing exact probabilities using the general chain rule without any approximations?

A. Computers cannot handle products of more than three conditional probabilities
B. Language is creative, making it likely that a long preceding context has never occurred before
C. The chain rule only applies to numerical tokens rather than text words
D. Exact probabilities can only be calculated for bigram models  

Correct Answer: B. Language is creative, making it likely that a long preceding context has never occurred before

Explanation: Computing $P(w_n \mid w_{1:n-1})$ is infeasible because language is creative and long specific contexts may never have appeared in the training corpus.
Question 4
What is the core intuition behind the Markov assumption in language modeling?

A. To calculate the exact probability using the entire preceding sentence
B. To replace raw words with subword tokens permanently
C. To ensure that every word in a sequence is treated as completely independent
D. To approximate the probability of a word by looking only at the last few words  

Correct Answer: D. To approximate the probability of a word by looking only at the last few words

Explanation: The Markov assumption simplifies computation by approximating the probability of a word given its entire history by looking only at the preceding $N - 1$ words.
Question 5
In a trigram language model ($N = 3$), how many words into the past does the model look?

A. 2 words
B. 3 words
C. 1 word
D. 4 words  

Correct Answer: A. 2 words

Explanation: A general N-gram looks $N - 1$ words into the past. For a trigram model where $N = 3$, it looks 2 words into the past ($N - 1 = 2$).
Question 6
Which of the following expressions represents the bigram approximation for the conditional probability $P(w_n \mid w_{1:n-1})$?

A. $P(w_n \mid w_1)$
B. $P(w_n \mid w_{1:n-2})$
C. $P(w_n \mid w_{n-2}, w_{n-1})$
D. $P(w_n \mid w_{n-1})$  

Correct Answer: D. $P(w_n \mid w_{n-1})$

Explanation: A bigram model ($N = 2$) looks 1 word into the past, approximating $P(w_n \mid w_{1:n-1})$ as $P(w_n \mid w_{n-1})$. Look-back of two words would be a trigram.
Question 7
What is the notation $w_{<n}$ equivalent to according to the notes?

A. All elements of $w$ from $w_1$ up to and including $w_{n-1}$
B. The entire sequence $w_1$ through $w_n$
C. Only the single preceding word $w_{n-1}$
D. The joint probability of $w_n$  

Correct Answer: A. All elements of $w$ from $w_1$ up to and including $w_{n-1}$

Explanation: The notes state that $w_{<n}$ is equivalent notation for all elements of $w$ from $w_1$ up to and including $w_{n-1}$.