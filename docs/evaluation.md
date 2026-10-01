# StudySync Evaluation

## Purpose

StudySync generates study materials from student-provided course notes.

The evaluation process is designed to determine whether generated study materials are accurate, complete, relevant, and well organized.

The evaluation approach was inspired by ideas from [SummEval](https://aclanthology.org/2021.tacl-1.24/) and [QAGS](https://aclanthology.org/2020.acl-main.450/).

SummEval provided inspiration for evaluating generated content across multiple quality dimensions, while QAGS inspired the use of questions based on the original source material to test whether important information is preserved in the generated output.

## Review Guide Evaluation Rubric

Each generated Review Guide is evaluated on four criteria using a 1–5 scale.

| Criterion | Score |
|---|---:|
| Accuracy | /5 |
| Coverage | /5 |
| Relevance | /5 |
| Organization | /5 |
| **Total** | **/20** |

### Accuracy

Is the information in the Review Guide accurately supported by the source notes?

- **5:** All or nearly all information is accurate and supported by the source notes. No meaningful errors or unsupported claims.
- **4:** Mostly accurate, with only minor inaccuracies or unsupported additions.
- **3:** Generally accurate, but contains some noticeable inaccuracies or misleading simplifications.
- **2:** Multiple inaccuracies or unsupported claims could cause misunderstanding.
- **1:** Major factual errors or unsupported information make the guide unreliable.

Accuracy also includes preserving important distinctions, technical details, and mathematical formulas from the source material.

### Coverage

Does the Review Guide include the important information from the source notes?

- **5:** Includes nearly all major concepts, definitions, relationships, and important details.
- **4:** Covers the major concepts but misses a small amount of useful information.
- **3:** Covers the main topic but misses several important concepts or details.
- **2:** Significant portions of important material are missing.
- **1:** Captures very little of the important source material.

### Relevance

Does the Review Guide focus on information that is useful for studying the provided course material?

- **5:** Consistently focused on useful material with little or no unnecessary information.
- **4:** Mostly focused, with only minor unnecessary information.
- **3:** Generally relevant but includes noticeable unnecessary or repetitive content.
- **2:** Significant portions are distracting, redundant, or unrelated.
- **1:** Much of the guide is irrelevant or poorly focused.

### Organization

Is the Review Guide structured clearly and effectively for studying?

- **5:** Information is logically organized, easy to scan, and grouped into useful sections.
- **4:** Clear overall structure with only minor organizational issues.
- **3:** Understandable but could be organized more effectively.
- **2:** Difficult to follow because of confusing or inconsistent organization.
- **1:** Poorly structured enough to significantly interfere with studying.

## Source Question Test

For each test set, five questions are created from the original course material before evaluating the generated Review Guide.

Each question is then answered using only the generated Review Guide.
The answer is checked against the original course material to determine whether the generated guide preserved the necessary information.

This provides a simple, QAGS-inspired test of both accuracy and coverage.

The result is recorded as the number of questions answered correctly out of five.

## Evaluation Results

### Test 1 — Tokenization

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

### Test 2 — Logistic Regression

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
