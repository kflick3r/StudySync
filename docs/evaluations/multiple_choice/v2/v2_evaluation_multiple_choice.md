# StudySync: Multiple Choice V2

## Overview

The Multiple Choice feature uses Google's Gemini API to generate up to ten multiple-choice questions from student-provided NLP course materials.

Each question includes four answer options, one correct answer, and an explanation. Students can check their answers individually or wait until the end of the quiz to view their results.

The purpose of this evaluation is to determine whether the generated questions are accurate, grounded in the student's notes, and useful for studying. The results will help determine whether the current V2 prompt needs revisions.

## Evaluation Methodology

Three tests will be conducted using the V2 prompt without modifications.

1. **Test 1: Baseline Generation** — Evaluate the quality of questions generated from a set of NLP course notes.
2. **Test 2: Repeatability** — Generate another quiz using the same notes to examine consistency and variation.
3. **Test 3: Limited Source Material** — Generate questions from a shorter set of notes to evaluate how Gemini handles limited information.

Each test will be evaluated using five criteria, scored from 1 to 5.

| Score | Description |
|---|---|
| 5 | Excellent, no meaningful issues |
| 4 | Good, minor issues |
| 3 | Acceptable, but improvements needed |
| 2 | Significant problems |
| 1 | Unreliable or unusable |

### Evaluation Criteria

| Criterion | Description |
|---|---|
| Accuracy | The correct answer is factually accurate, and exactly one answer is defensible. |
| Grounding | Questions, answers, and explanations are supported by the original notes. |
| Distractor Quality | Incorrect options are plausible but clearly incorrect. |
| Explanation Quality | Explanations are accurate, clear, and useful for learning. |
| Coverage & Variety | Questions cover important concepts and include different types of understanding. |

Each test receives a total score out of 25.

---

## Test 1: Baseline Generation

**Objective:** Evaluate the initial quality of multiple-choice questions generated using the V2 prompt.

**Course Material Used:** Logistic Regression

**Number of Questions Generated:** 10

Generated questions, answers, and explanations can be found at: `/doc/evaluations/multiple_choice/v2/v2_test1.md`

### Evaluation Results

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Accuracy | 5 / 5 | All ten questions had defensible correct answers. No incorrect answer keys were identified. |
| Grounding | 5 / 5 | Questions, correct answers, and explanations were supported by the original Logistic Regression notes. |
| Distractor Quality | 3 / 5 | Several incorrect options were too easy to eliminate, particularly in Questions 1, 4, 5, and 9. |
| Explanation Quality | 3 / 5 | Explanations were accurate but often repeated the correct answer without providing additional context. |
| Coverage & Variety | 4 / 5 | Questions covered several important concepts, but most focused on factual recall rather than application or problem-solving. |
| **Total** | **20 / 25** | Good initial results, with room to improve distractors, explanations, and question variety. |

### Question-Level Issues

**Questions with incorrect or ambiguous answers:**  
No clearly incorrect answer keys were identified. However, Question 2 could be more precise about the difference between the general probability range of 0 to 1 inclusive and the logistic sigmoid's output range of strictly between 0 and 1 for finite inputs.

**Questions containing unsupported information:**  
None identified.

**Questions with weak distractors:**  
Questions 1, 4, 5, and 9 contained distractors that were relatively easy to eliminate or did not require much conceptual understanding.

**Questions with insufficient explanations:**  
Questions 4, 6, 7, 8, and 9 contained explanations that largely repeated the correct answer without providing much additional context.

### Observations

**What worked well?**

Gemini successfully generated ten multiple-choice questions from the provided Logistic Regression notes. The questions were accurate and remained grounded in the source material. They covered several important concepts, including classification thresholds, decision boundaries, the sigmoid function, and feature weights. The quiz interface also appeared to function as expected, including answer selection, immediate feedback, and progress tracking.

**What could be improved?**

The biggest weaknesses were distractor quality and explanation depth. Some incorrect options were too obviously wrong, making the questions easier to answer through elimination. Several explanations also repeated the correct answer rather than explaining the underlying concept. Although the questions covered a reasonable range of topics, more application-based questions would make the quiz more useful for testing understanding.

**Overall Assessment:**

The initial results suggest that the V1 prompt provides a good foundation for generating multiple-choice study questions. The questions were accurate and grounded in the provided notes, but improvements to distractor quality, explanations, and question variety could make the tool more effective. Additional testing is needed to determine whether these weaknesses occur consistently before revising the prompt.

---

## Test 2: Repeatability

**Objective:** Evaluate whether the V1 prompt produces consistently useful questions when given the same source material.

**Course Material Used:** Same notes as Test 1

**Number of Questions Generated:** 10

### Evaluation Results

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Accuracy | 5 / 5 | All ten questions had defensible correct answers. No incorrect answer keys were identified. |
| Grounding | 5 / 5 | Questions, correct answers, and explanations were supported by the original notes. |
| Distractor Quality | 3 / 5 | Several incorrect options remained easy to eliminate or were unrelated to the concept being tested. |
| Explanation Quality | 3 / 5 | Explanations were accurate but often repeated the correct answer without providing additional context. |
| Coverage & Variety | 4 / 5 | Questions covered important concepts, but there was substantial overlap with Test 1 and little application-based reasoning. |
| **Total** | **20 / 25** | Consistent with Test 1, including recurring weaknesses. |

### Comparison with Test 1

**Were the generated questions substantially different?**

No. Eight questions tested essentially the same concepts in both runs. The other two also remained within the same general areas of the logistic model.

The second run did not explore several concepts available in the notes, including calculating a decision boundary using \(x=-b/w\), the effect of changing the intercept, or applying the sigmoid formula.

**Was question quality consistent across both runs?**

Yes. Both runs generated ten questions with defensible correct answers and no obvious unsupported content.

**Did Gemini emphasize different concepts or question types?**

Not substantially. Both runs emphasized factual recall and straightforward conceptual understanding. Neither included a numerical calculation, and both relied heavily on questions asking students to identify definitions or relationships.

**Were any problems repeated?**

Yes. The same two problems appeared in both runs: weak distractors and explanations that largely restated the correct answer. This is stronger evidence that those weaknesses are associated with the current prompt rather than an isolated generation.

### Question-Level Issues

**Questions with incorrect or ambiguous answers:**
No clearly incorrect answer keys were identified.

**Questions containing unsupported information:**
None identified.

**Questions with weak distractors:**
Questions 1, 3, 5, 8, and 10 contained distractors that were relatively easy to eliminate or did not require much conceptual understanding.

**Questions with insufficient explanations:**
Questions 1, 4, 6, 9, and 10 contained explanations that largely repeated the correct answer or provided limited additional context.

### Overall Assessment

The second test confirmed that the V1 prompt produces consistently accurate and grounded multiple-choice questions. However, the repeated weaknesses in distractor quality, explanation depth, and question variety suggest that the prompt could be improved. Gemini generated almost the same set of concepts in both tests, with little emphasis on application or problem-solving. These findings support exploring prompt revisions after completing the limited-source-material test.

---

## Test 3: Limited Source Material

**Objective:** Evaluate whether Gemini can generate meaningful questions from a smaller amount of course material without introducing unsupported information.

**Course Material Used:** Short N-Gram notes

**Number of Questions Generated:** 9

### Evaluation Results

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Accuracy | 5 / 5 | All nine questions had defensible correct answers. No incorrect answer keys were identified. |
| Grounding | 5 / 5 | Questions, correct answers, and explanations remained grounded in the supplied notes. |
| Distractor Quality | 3 / 5 | Several incorrect options were implausible or unrelated to the concepts being tested. |
| Explanation Quality | 3 / 5 | Explanations were accurate but frequently repeated the correct answer without additional context. |
| Coverage & Variety | 4 / 5 | Questions covered the major concepts in the shortened notes, but relied primarily on factual recall and included some overlap. |
| **Total** | **20 / 25** | Accurate and grounded, with recurring weaknesses in distractors, explanations, and variety. |

### Limited-Material Observations

**Did Gemini generate fewer than ten questions when appropriate?**
Yes, Gemini only generated nine questions with the shorter notes. This is a positive result for the limited-material test. However, generating nine questions doesn't necessarily mean all nine are meaningfully distinct. Questions 7 and 8 overlap substantially.

**Did the questions remain grounded in the provided notes?**
All nine answer keys are defensible based on the supplied notes. Gemini also avoided reproducing the apparent indexing error in the general N-gram formula.

**Were any questions repetitive or overly similar?**
Most questions asked students to recognize a definition, identify a formula, or recall a fact. Gemini could have tested application by asking students to identify the appropriate history for a trigram model or apply the chain rule to a short sequence.

**Did Gemini introduce unsupported examples, definitions, or explanations?**
Explanations remained shallow. For example, Question 8 asks how many words a general N-gram model looks into the past. Its explanation simply states that an N-gram looks $N-1$ words into the past, without explaining that one position in the N-gram is occupied by the word being predicted.

### Question-Level Issues

**Questions with incorrect or ambiguous answers:**
No clearly incorrect answer keys were identified.

**Questions containing unsupported information:**
None identified.

**Questions with weak distractors:**
Questions 1, 2, 5, 7, and 8 contained incorrect options that were relatively easy to eliminate or did not require much conceptual understanding.

**Questions with insufficient explanations:**
Questions 3, 4, 6, 7, 8, and 9 contained explanations that largely repeated the correct answer without providing additional reasoning.

### Overall Assessment

The limited-material test showed that the V1 prompt can generate fewer than ten questions while maintaining accuracy and grounding. All nine questions were supported by the provided notes, and no incorrect answer keys were identified.

However, the same weaknesses observed in Tests 1 and 2 appeared again. Several distractors were too easy to eliminate, explanations often repeated the correct answer, and most questions emphasized factual recall rather than application. There was also some overlap between questions testing similar concepts.

These results suggest that the V1 prompt provides a reliable foundation but could benefit from revisions that encourage stronger distractors, more informative explanations, and greater question variety.

---

## Summary of Results

| Evaluation | Accuracy | Grounding | Distractors | Explanations | Coverage | Total |
|---|---|---|---|---|---|---|
| Test 1: Baseline | 5 | 5 | 3 | 3 | 4 | 20 / 25 |
| Test 2: Repeatability | 5 | 5 | 3 | 3 | 4 | 20 / 25 |
| Test 3: Limited Material | 5 | 5 | 3 | 3 | 4 | 20 / 25 |
| **Average** | 5 | 5 | 3 | 3 | 4 | 20 / 25 |

### Key Findings

**Strengths of the V1 Prompt:**

Across all three tests, Gemini generated 29 multiple-choice questions with no clearly incorrect answer keys or unsupported information identified. The questions remained grounded in the original course notes and covered the main concepts in each topic.

The results were also consistent across multiple generations. All three tests received an overall score of 20/25. In the limited-material test, Gemini generated nine questions instead of the maximum of ten, suggesting that the prompt can adjust the number of questions based on the available material.

**Weaknesses or Recurring Problems:**

The most consistent weaknesses were distractor quality and explanation depth. Several incorrect answer options were obviously wrong or unrelated to the question, making it possible to identify the correct answer through elimination rather than understanding the concept.

Some questions also tested very similar information. In Test 2, Gemini generated almost the same set of questions as Test 1, despite using a new generation. Test 3 also contained some overlap between questions about bigram and general N-gram history lengths.

**Answer Length and Distractor Balance:**

In several questions, the correct answer was noticeably longer or more specific than the incorrect options. This was particularly apparent in Test 3, where some correct answers included detailed definitions while the distractors were shorter or less relevant.

Although this was not consistent across every question, it could make some answers easier to identify without fully understanding the material.

**Question Difficulty and Variety:**

Most questions focused on factual recall or basic conceptual understanding. There were some useful conceptual questions, particularly those involving classification thresholds and the Markov assumption, but very few required students to apply information or solve a problem.

For example, the Logistic Regression notes included formulas and numerical examples for calculating decision boundaries, but neither generation included a calculation-based question.

**Explanation Quality:**

The explanations were generally accurate and grounded in the original notes, but many simply repeated the correct answer. They confirmed which option was correct without always explaining why it was correct or helping the student understand the underlying concept.

More informative explanations could make the feature more useful for studying, especially when students answer incorrectly.

---

## Prompt Evaluation and Next Steps

### Does the V1 Prompt Need Revision?

**Decision:** Revise Prompt

**Reasoning:**

The V1 prompt consistently generated accurate and grounded questions, so the basic approach appears to be working well. However, the same weaknesses appeared across all three tests, particularly with distractors, explanations, and question variety.

Rather than rewriting the entire prompt, I want to make targeted changes that address these issues while preserving the accuracy and grounding demonstrated in V1.

### Proposed Prompt Changes

| Identified Issue | Proposed Change | Supporting Evidence |
|---|---|---|
| Weak distractors | Instruct Gemini to generate plausible incorrect answers that reflect common misconceptions or closely related concepts, rather than obviously unrelated options. | All three tests contained distractors that were easy to eliminate. |
| Shallow explanations | Require explanations to briefly explain the reasoning behind the correct answer instead of simply repeating it. | Questions 4, 6, and 8 in Test 1 and several questions in Test 3 contained repetitive explanations. |
| Limited question variety | Encourage a mix of recall, conceptual understanding, and application questions when supported by the source material. Avoid generating multiple questions that test essentially the same concept. | Tests 1 and 2 contained no numerical application questions, and Test 3 included overlapping questions about N-gram history lengths. |
| Answer-length imbalance | Encourage answer options to have similar levels of detail and length without sacrificing accuracy or clarity. | Several questions, particularly in Test 3, had correct answers that were noticeably longer or more specific than the distractors. |

### Next Steps

The next step is to develop a V2 prompt that incorporates these targeted improvements.

I plan to keep the existing question generation and validation functionality while revising the prompt instructions for distractor quality, explanations, and question variety.

Once V2 is implemented, I will test it using the same Logistic Regression and N-Grams notes from V1. Using the same source material and evaluation rubric will allow me to compare the results and determine whether the prompt changes improve question quality without reducing accuracy or grounding.

---

## Final Reflection

**What did I learn from implementing and evaluating Multiple Choice V1?**

One of my biggest takeaways was that generating technically correct multiple-choice questions is only part of building a useful study tool. Gemini consistently produced accurate questions, but that did not necessarily mean they were challenging or effective for studying. The quality of the incorrect answer options and explanations matters just as much as getting the correct answer right.

I also found that evaluating multiple generations was useful for identifying patterns. Some issues might have seemed minor in a single quiz, but seeing the same weaknesses across three tests helped me identify where the prompt needs improvement.

**What challenges did I encounter?**

One challenge was balancing question difficulty with accuracy and grounding. I want Gemini to generate questions that require students to think, but I also want to make sure it doesn't introduce information that isn't supported by their notes.

Another challenge was evaluating distractor quality. An incorrect answer can be factually wrong but still be a poor distractor if it is too obvious. I also found that explanations need more attention because simply repeating the correct answer doesn't provide much additional value to the student.

**What would I improve in future versions?**

For V2, I want to focus on making the generated questions more useful for active recall and understanding. This includes improving distractors, generating more application-based questions when the material supports them, and providing explanations that help students understand the reasoning behind an answer.

I also want to continue evaluating generated content against the original notes. The goal is not just to generate questions that look correct, but to create a study tool that helps students identify what they understand and where they might need more review.