# **Evaluation Results**

## V1 Prompt

You are an AI study assistant helping a college student study Natural Language Processing.

Create a clear review guide from the course material provided below.

Requirements:
- Use only information supported by the provided course material.
- Do not invent facts or add outside information.
- Identify and organize the major concepts, definitions, relationships,
  and important details.
- Use clear headings and concise explanations.
- Preserve important distinctions between related concepts.
- Write the guide for a student studying an NLP course.
- If the notes are unclear or incomplete, do not guess. Indicate that
  the information is unclear or missing.


#### **Test 1 — Tokenization**

**Source Type:** Structured notes created with LLM assistance

**Prompt Version:** V1

**Rubric Score:** 20/20

| Criterion | Score |
|---|---:|
| Accuracy | 5/5 |
| Coverage | 5/5 |
| Relevance | 5/5 |
| Organization | 5/5 |
| **Total** | **20/20** |

**Source Questions:** 5/5

| Question | Answerable from guide? | Correct? |
|---|---|---|
| 1. What is tokenization and why is it important? | Yes | Yes |
| 2. Why doesn't token = word? | Yes | Yes |
| 3. Why no universally correct tokenization? | Yes | Yes |
| 4. Symbolic vs. stochastic? | Yes | Yes |
| 5. How does BPE address unknown words? | Yes | Yes |

**Notes:**

The Review Guide preserved the major concepts from the source notes, including tokenization, the distinction between tokens and words, challenges in tokenization, symbolic and stochastic approaches, rule-based tokenization, subword tokenization, and BPE.

The guide also preserved the important qualification that standard BPE is deterministic once its training data and procedure are fixed.

#### **Test 2 — Logistic Regression**

**Source Type:** Structured notes created with LLM assistance

**Prompt Version:** V1

**Rubric Score:** 19/20

| Criterion | Score |
|---|---:|
| Accuracy | 4/5 |
| Coverage | 5/5 |
| Relevance | 5/5 |
| Organization | 5/5 |
| **Total** | **19/20** |

**Source Questions:** 5/5

| Question | Answerable from guide? | Correct? |
|---|---|---|
| 1. What does logistic regression model instead of modeling the response variable directly? | Yes | Yes |
| 2. How does a classification threshold turn a predicted probability into a class prediction? | Yes | Yes |
| 3. Why is logistic regression better suited to binary classification than linear regression? | Yes | Yes |
| 4. How are the logit, sigmoid function, weights, and bias related? | Yes | Yes |
| 5. What do the sign and magnitude of a feature's weight tell us about its contribution to the classification decision? | Yes | Yes |

**Notes:**

The Review Guide captured the major concepts from the source notes, including classification thresholds, decision boundaries, the logistic function, sigmoid and logit notation, feature weights, and the relationship between weights and classification evidence.

The main issue identified was mathematical formatting. The logistic function was not rendered clearly in the generated output, making the formula difficult to interpret accurately.

The guide also appropriately identified that the provided notes referenced estimating the regression coefficients without providing the details needed to explain that process.

#### **Test 3 — Naive Bayes**

**Source Type:** Structured notes created with LLM assistance

**Prompt Version:** V1

**Rubric Score:** 20/20

| Criterion | Score |
|---|---:|
| Accuracy | 5/5 |
| Coverage | 5/5 |
| Relevance | 5/5 |
| Organization | 5/5 |
| **Total** | **20/20** |

**Source Questions:** 5/5

| Question | Answerable from guide? | Correct? |
|---|---|---|
| 1. What conditional independence assumption does Naive Bayes make? | Yes | Yes |
| 2. What are the prior, likelihood, and posterior in Naive Bayes? | Yes | Yes |
| 3. How does Naive Bayes use these probabilities to choose the most likely class? | Yes | Yes |
| 4. What is the difference between Binary and Multinomial Naive Bayes? | Yes | Yes |
| 5. Why can Naive Bayes be computationally efficient even though probability tables would otherwise grow exponentially? | Yes | Yes |

**Notes:**

The Review Guide preserved the major concepts from the source notes, including the conditional independence assumption, the Naive Bayes formula, prior/likelihood/posterior, inference, computational efficiency, text classification, and the distinction between Binary and Multinomial Naive Bayes.

The guide also preserved the important limitation that the independence assumption is generally false while explaining why Naive Bayes can still perform well.

#### **Test 4 — N-Grams and Language Models**

**Source Type:** Raw textbook material

**Prompt Version:** V1

**Rubric Score:** 19/20

| Criterion | Score |
|---|---:|
| Accuracy | 5/5 |
| Coverage | 4/5 |
| Relevance | 5/5 |
| Organization | 5/5 |
| **Total** | **19/20** |

**Source Questions:** 5/5

| Question | Answerable from guide? | Correct? |
|---|---|---|
| 1. Why can't we simply estimate the probability of a word using its entire preceding history? | Yes | Yes |
| 2. What is the Markov assumption, and how does it relate to an N-gram model? | Yes | Yes |
| 3. How does Maximum Likelihood Estimation estimate an N-gram probability? | Yes | Yes |
| 4. Why are language-model probabilities computed in log space? | Yes | Yes |
| 5. What is the difference between a bigram, trigram, and general N-gram model? | Yes | Yes |

**Notes:**

This test used raw textbook material rather than notes previously summarized and organized with LLM assistance.

The Review Guide accurately captured the major concepts, including the chain rule, Markov assumption, N-gram models, MLE, log probabilities, longer context, and large-scale language-model considerations.

Coverage was reduced to 4/5 because the generated guide omitted some specific examples and supporting details from the textbook, including parts of the Berkeley Restaurant Project example, concrete probability calculations, and some discussion of linguistic and cultural phenomena captured by bigram statistics.

The guide nevertheless retained the information needed to answer all five source questions correctly.

#### **Test 5 — Regular Expressions**

**Source Type:** Raw textbook material

**Prompt Version:** V1

**Rubric Score:** 19/20

| Criterion | Score |
|---|---:|
| Accuracy | 4/5 |
| Coverage | 5/5 |
| Relevance | 5/5 |
| Organization | 5/5 |
| **Total** | **19/20** |

**Source Questions:** 5/5

| Question | Answerable from guide? | Correct? |
|---|---|---|
| 1. What is a regular expression, and what are some of its uses in text processing? | Yes | Yes |
| 2. What is the difference between the `*`, `+`, `?`, and `{n}` regex operators? | Yes | Yes |
| 3. What is the difference between greedy and non-greedy matching? | Yes | Yes |
| 4. How are false positives and false negatives related to precision and recall when designing a regex? | Yes | Yes |
| 5. What are capture groups used for, and how are they different from non-capturing groups? | Yes | Yes |

**Notes:**

This test used raw textbook material rather than notes previously summarized and organized with LLM assistance.

The Review Guide captured essentially all of the major regex concepts, including character classes, ranges, counting operators, anchors, boundaries, disjunction, grouping, precedence, greedy and non-greedy matching, precision and recall, aliases, substitutions, capture groups, lookahead assertions, and BPE pre-tokenization.

The main issue identified was a small accuracy problem in the description of the dollar-sign anchor. The guide stated that `$` matches a space at the end of a line, while the textbook uses the pattern ` $` to match a space at the end of a line; `$` itself is the end-of-line anchor.

This was treated as a minor technical distinction rather than a major misunderstanding.

### **Baseline Summary**

The first three tests used Prompt V1 with structured NLP notes that had previously been developed with LLM assistance. The final two tests used raw textbook material to provide a more realistic test of StudySync's ability to transform unstructured source material.

| Test | Source Type | Accuracy | Coverage | Relevance | Organization | Total | Questions |
|---|---|---:|---:|---:|---:|---:|---:|
| Tokenization | Structured/LLM-assisted notes | 5/5 | 5/5 | 5/5 | 5/5 | **20/20** | **5/5** |
| Logistic Regression | Structured/LLM-assisted notes | 4/5 | 5/5 | 5/5 | 5/5 | **19/20** | **5/5** |
| Naive Bayes | Structured/LLM-assisted notes | 5/5 | 5/5 | 5/5 | 5/5 | **20/20** | **5/5** |
| N-Grams | Raw textbook | 5/5 | 4/5 | 5/5 | 5/5 | **19/20** | **5/5** |
| Regular Expressions | Raw textbook | 4/5 | 5/5 | 5/5 | 5/5 | **19/20** | **5/5** |

These results provide an initial baseline for Prompt V1. The structured note tests produced very strong results, but those source materials had already been summarized and organized with LLM assistance.

The raw textbook tests provide a more realistic evaluation. They still show strong performance, but they revealed minor issues that were less apparent in the structured-note tests.


### Prompt V2 Goals

Based on the V1 evaluation, Prompt V2 should:

1. Preserve mathematical formulas and technical notation accurately.
2. Avoid changing the meaning of technical statements when summarizing.
3. Preserve important examples when they help explain a concept.
4. Distinguish major concepts from optional supporting details.
5. Continue prioritizing information supported by the source material.
6. Avoid adding information that is not supported by the source.

---

## V2 Prompt

You are an AI study assistant helping a college student study Natural Language Processing.

Create a clear review guide from the course material provided below.

Requirements:
- Use only information supported by the provided course material.
- Do not invent facts or add outside information.
- Identify and organize the major concepts, definitions, relationships,
  and important details.
- Use clear headings and concise explanations.
- Preserve important distinctions between related concepts.
- Write the guide for a student studying an NLP course.
- If the notes are unclear or incomplete, do not guess. Indicate that
  the information is unclear or missing.

*New V2 Requirements:*
- Preserve important examples when they help explain or distinguish a concept.
- Preserve technical details accurately, including mathematical formulas,
  notation, symbols, operators, and terminology.
- Do not change the meaning of technical statements when summarizing.


#### Test 1 — Tokenization

**Prompt Version:** V2

**Rubric Score:** 20/20

**Source Questions:** 5/5 answerable, 5/5 correct

| Question | Answerable from guide? | Correct? |
|---|---|---|
| 1. What is tokenization and why is it important? | Yes | Yes |
| 2. Why doesn't token = word? | Yes | Yes |
| 3. Why is there no universally correct tokenization? | Yes | Yes |
| 4. What is the difference between symbolic and stochastic approaches? | Yes | Yes |
| 5. How does BPE address the unknown-word problem? | Yes | Yes |

**Notes:**

V2 preserved the major concepts from the source material while retaining more of the supporting examples and technical details. It correctly preserved the distinction between BPE being data-driven and standard BPE being deterministic once its training procedure is fixed. It also retained the UTF-8 detail and the course-file references.

The main issue observed was a minor formatting problem in the BPE conceptual flow, where the arrows and text were rendered without spacing. This did not affect the content or answerability of the guide.


#### **Test 2 — Logistic Regression**

**Prompt Version:** V2

**Rubric Score:** 20/20

**Source Questions:** 5/5 answerable, 5/5 correct

| Question | Answerable from guide? | Correct? |
|---|---|---|
| 1. What is logistic regression and what does it model? | Yes | Yes |
| 2. How does the classification threshold affect predictions? | Yes | Yes |
| 3. How is the decision boundary determined for a single predictor? | Yes | Yes |
| 4. What are the logit and sigmoid function, and how are they related? | Yes | Yes |
| 5. How do feature weights affect the classification decision? | Yes | Yes |

**Notes:**

V2 preserved the major concepts from the source material, including the classification threshold, decision boundary, logistic function, logit form, relationship between β notation and vector notation, and interpretation of feature weights. It also retained important examples such as the 0.1 classification threshold, the w = 1 and b = 2 decision-boundary example, and the sentiment-classification weight examples.

The guide appropriately indicated when referenced material was unavailable rather than attempting to fill in the missing information. The mathematical notation also rendered correctly in the StudySync interface.


#### **Test 3 — Naive Bayes**

**Prompt Version:** V2

**Rubric Score:** 20/20

**Source Questions:** 5/5 answerable, 5/5 correct

| Question | Answerable from guide? | Correct? |
|---|---|---|
| 1. What assumption does Naive Bayes make about the evidence? | Yes | Yes |
| 2. What are the prior, likelihood, and posterior in Naive Bayes? | Yes | Yes |
| 3. How does Naive Bayes use probabilities to classify a document? | Yes | Yes |
| 4. What is the difference between Binary and Multinomial Naive Bayes? | Yes | Yes |
| 5. Why can Naive Bayes work well despite its independence assumption? | Yes | Yes |

**Notes:**

V2 preserved the major concepts from the source material, including conditional independence, the Naive Bayes formula, prior/likelihood/posterior, inference, Binary vs. Multinomial Naive Bayes, computational efficiency, applications, advantages, and limitations. It also retained important examples such as "first" and "quarter" and the distinction between word presence and word frequency.

The guide preserved the graphical structure and mathematical notation from the source material without adding unsupported concepts. It also retained the explanation that Naive Bayes can perform well despite its often-false independence assumption.


#### **Test 4 — N-Grams**

**Prompt Version:** V2

**Rubric Score:** 20/20

**Source Questions:** 5/5 answerable, 5/5 correct

| Question | Answerable from guide? | Correct? |
|---|---|---|
| 1. What does the chain rule of probability do for a sequence of words? | Yes | Yes |
| 2. What is the Markov assumption, and how does it relate to N-grams? | Yes | Yes |
| 3. How are N-gram probabilities estimated using MLE? | Yes | Yes |
| 4. Why are log probabilities used when computing language model probabilities? | Yes | Yes |
| 5. What engineering techniques can be used to improve the storage and efficiency of N-gram models? | Yes | Yes |

**Notes:**

V2 preserved the major concepts from the source material, including the chain rule, Markov assumption, N-gram models, Maximum Likelihood Estimation, sentence boundary symbols, log probabilities, numerical underflow, and engineering techniques for storing and scaling N-gram models.

The guide retained the important mathematical formulas and distinctions between bigrams, trigrams, and general N-grams. It also preserved the engineering details about quantization, 64-bit hashes, data structures, pruning, and Infini-gram. The generated mathematical notation rendered correctly in the StudySync interface.


#### **Test 5 — Regular Expressions**

**Prompt Version:** V2

**Rubric Score:** 20/20

**Source Questions:** 5/5 answerable, 5/5 correct

| Question | Answerable from guide? | Correct? |
|---|---|---|
| 1. What are regular expressions, and what are some of their uses in NLP? | Yes | Yes |
| 2. What do common regex operators such as `?`, `*`, `+`, and `{n}` do? | Yes | Yes |
| 3. What is the difference between greedy and non-greedy matching? | Yes | Yes |
| 4. How can regexes be used to manage false positives and false negatives? | Yes | Yes |
| 5. How are regular expressions used in BPE pre-tokenization? | Yes | Yes |

**Notes:**

V2 preserved the major concepts from the source material, including character classes, ranges, negation, counting operators, anchors, boundaries, grouping, precedence, greediness, precision and recall, character-class aliases, substitutions, capture groups, lookaheads, and BPE pre-tokenization.

The guide retained a large number of the original technical examples and regex patterns, including the GPT-2 pre-tokenization regex and Unicode properties. It also preserved the distinction between different uses of the caret (`^`) and between greedy and non-greedy operators. A minor formatting issue occurred in the escaping examples, but it did not affect the substantive content or answerability of the guide.


## V1 vs. V2 Comparison

The V2 prompt was created in response to issues identified during the V1 evaluation. V1 performed strongly overall, but the evaluation identified minor problems with mathematical formatting and technical accuracy, as well as some loss of supporting examples and details when working from raw textbook material.

V2 added three main requirements:
- Preserve important examples when they help explain or distinguish a concept.
- Preserve technical details accurately, including mathematical formulas, notation, symbols, operators, and terminology.
- Do not change the meaning of technical statements when summarizing.

### Overall Results

| Version | Accuracy | Coverage | Relevance | Organization | Total |
|---|---:|---:|---:|---:|---:|
| V1 | 23/25 | 24/25 | 25/25 | 25/25 | **97/100** |
| V2 | 25/25 | 25/25 | 25/25 | 25/25 | **100/100** |

### Source Question Results

Both versions successfully passed all five source-question tests.

| Version | Questions Answerable | Questions Correct |
|---|---:|---:|
| V1 | 25/25 | 25/25 |
| V2 | 25/25 | 25/25 |

The source-question test therefore did not distinguish between the two prompt versions. Both versions produced guides that contained enough information to answer the selected questions correctly.

### Observed Differences

V1's main weaknesses appeared in the rubric-based evaluation rather than the source-question test. The Logistic Regression test received 4/5 for Accuracy because of a mathematical formatting problem, while the Regular Expressions test received 4/5 for Accuracy because of a minor technical error involving the dollar-sign anchor. The N-Grams test received 4/5 for Coverage because some supporting examples and textbook details were omitted.

V2 addressed the goals identified from those results. The Logistic Regression guide preserved the mathematical relationships and rendered the notation correctly in the StudySync interface. The N-Grams guide retained more of the mathematical formulas and engineering details from the source material. The Regular Expressions guide retained more technical examples and regex patterns, including the GPT-2 pre-tokenization regex and Unicode properties.

### Interpretation

The V2 results provide evidence that the additional prompt requirements improved preservation of technical details and supporting examples without reducing the guide's ability to answer source-based questions.

However, the results should be interpreted cautiously. The evaluation used only five test sets, and the first three source sets were structured notes created with LLM assistance, while the final two were raw textbook material. This difference in source type makes it difficult to attribute all observed differences solely to the prompt change.

The V2 results therefore support continuing with the revised prompt as the current baseline, while additional testing would be useful before considering the prompt finalized.

