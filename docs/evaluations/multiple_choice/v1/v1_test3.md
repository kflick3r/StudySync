# StudySync: Multiple Choice V1 — Test 3 Generated Questions

**Topic:** N-Grams and Language Models  
**Questions Generated:** 9  
**Source:** N-Grams and Language Models course notes (shortened)  
**Prompt Version:** V1

---

### Question 1

**What is the primary task of language models as described in the overview?**

A. Translating text from one natural language into another  
B. Classifying text documents into predefined thematic topics  
C. Computing the joint probability of an entire word sequence or the conditional probability of a word given a history  
D. Assigning sentiment polarity scores to individual sentences

**Correct Answer:** C. Computing the joint probability of an entire word sequence or the conditional probability of a word given a history

**Explanation:** The course material states that the task is to compute the conditional probability P(w | h) of a word w given some history h, or the joint probability of an entire word sequence W.

---

### Question 2

**In practice, what are language models often computed over instead of raw words?**

A. Morphological roots  
B. Phonetic sound units  
C. Tokens like BPE tokens  
D. Sentence embeddings

**Correct Answer:** C. Tokens like BPE tokens

**Explanation:** The material notes that in practice, language models are often computed over tokens (like BPE tokens) rather than raw words.

---

### Question 3

**What does the notation w₁:ₙ₋₁ represent in the course material?**

A. The final word in a sequence  
B. All elements from w₂ to wₙ  
C. The string w₁, w₂, …, wₙ₋₁  
D. A sequence of n words

**Correct Answer:** C. The string w₁, w₂, …, wₙ₋₁

**Explanation:** The notation w₁:ₙ₋₁ explicitly represents the string w₁, w₂, …, wₙ₋₁.

---

### Question 4

**Which mathematical rule is used to decompose the joint probability of a sequence into a product of conditional probabilities?**

A. The Central Limit Theorem  
B. The Chain Rule of Probability  
C. Bayes' Theorem  
D. Markov's Inequality

**Correct Answer:** B. The Chain Rule of Probability

**Explanation:** The Chain Rule of Probability decomposes the joint probability of a sequence into a product of conditional probabilities.

---

### Question 5

**Why is computing the exact probability of a word given a very long preceding sequence, P(wₙ | w₁:ₙ₋₁), considered infeasible?**

A. Because joint probabilities cannot be multiplied together computationally  
B. Because grammar rules prevent sentences from exceeding a certain length  
C. Because computers lack sufficient memory to store dictionary definitions  
D. Because language is creative and a particular context may never have occurred before in a corpus

**Correct Answer:** D. Because language is creative and a particular context may never have occurred before in a corpus

**Explanation:** The material states that computing this exact probability is infeasible because language is creative and any particular context may never have occurred before in a corpus.

---

### Question 6

**What is the core intuition behind the Markov Assumption in N-grams?**

A. Assuming that all words in a sequence are completely independent of one another  
B. Approximating the probability of a word given its entire history by looking only at the last few words  
C. Looking at every preceding word in the entire document history  
D. Averaging the probabilities of all possible future words

**Correct Answer:** B. Approximating the probability of a word given its entire history by looking only at the last few words

**Explanation:** The core intuition of the Markov Assumption is to approximate the probability of a word given its entire history by looking only at the last few words.

---

### Question 7

**How many words into the past does a bigram model (N = 2) look?**

A. 1 word  
B. 2 words  
C. Zero words  
D. N-1 words where N is variable

**Correct Answer:** A. 1 word

**Explanation:** A bigram model (N = 2) looks 1 word into the past.

---

### Question 8

**How many words into the past does a general N-gram model look?**

A. N - 1 words  
B. N squared words  
C. N words  
D. N + 1 words

**Correct Answer:** A. N - 1 words

**Explanation:** The general N-gram looks N - 1 words into the past.

---

### Question 9

**Which of the following formulas represents the bigram approximation for the complete sequence probability P(w₁:ₙ)?**

A. P(w₁:ₙ) ≈ ∏ₖ₌₁ⁿ P(wₖ | wₖ₋₁)  
B. P(w₁:ₙ) ≈ ∑ₖ₌₁ⁿ P(wₖ | wₖ₋₂)  
C. P(w₁:ₙ) ≈ ∏ₖ₌₁ⁿ P(wₖ)  
D. P(w₁:ₙ) ≈ ∏ₖ₌₁ⁿ P(wₖ | w₁:ₖ₋₁)

**Correct Answer:** A. P(w₁:ₙ) ≈ ∏ₖ₌₁ⁿ P(wₖ | wₖ₋₁)

**Explanation:** The complete sequence approximation using the bigram assumption is given by P(w₁:ₙ) ≈ ∏ₖ₌₁ⁿ P(wₖ | wₖ₋₁).