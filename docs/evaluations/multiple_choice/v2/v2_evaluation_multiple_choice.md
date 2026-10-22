# StudySync: Multiple Choice V2 — Implementation and Evaluation

## Overview

The Multiple Choice feature uses Google's Gemini API to generate up to ten multiple-choice questions from student-provided NLP course materials.

Each question includes four answer options, one correct answer, and an explanation. Students can check their answers individually and review their results at the end of the quiz.

The V1 evaluation showed that Gemini could consistently generate accurate questions grounded in the original notes. However, several weaknesses appeared across all three tests, particularly with distractor quality, explanation depth, and question variety.

For V2, I revised the prompt to address these issues while preserving the accuracy and grounding demonstrated in V1. I also added support for LaTeX mathematical notation and additional validation.

The purpose of this evaluation is to determine whether these changes improved the quality of the generated questions.

## Implementation Changes

The V2 prompt includes more specific instructions for generating high-quality multiple-choice questions.

The main changes include:

- **Distractor Quality:** Encourage plausible incorrect answers based on related concepts or common misunderstandings rather than obviously unrelated options.
- **Explanation Quality:** Require explanations to provide useful reasoning instead of simply repeating the correct answer.
- **Question Variety:** Encourage a mixture of factual recall, conceptual understanding, and application questions when supported by the notes.
- **Answer Balance:** Keep answer options reasonably similar in length, detail, and grammatical structure.
- **Mathematical Notation:** Instruct Gemini to use LaTeX formatting for mathematical expressions.

I also added a `has_valid_math_delimiters()` helper function to check whether inline mathematical delimiters are balanced. This validation runs alongside the existing checks for question structure, answer options, and correct answer indices.

Additionally, I fixed an issue where previously generated multiple-choice questions remained available after the student submitted different course notes. The application now clears the previous quiz when the source material changes.

## Evaluation Methodology

I conducted three tests using the V2 prompt without modifying it between generations.

1. **Test 1: Baseline Generation:** Evaluate questions generated from the same Logistic Regression notes used in V1.
2. **Test 2: Repeatability:** Generate another quiz using the same Logistic Regression notes to examine consistency.
3. **Test 3: Limited Source Material:** Generate questions from the same shortened N-Grams and Language Models notes used in V1.

Each test was evaluated using the same five criteria from V1, scored from 1 to 5.

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

LaTeX rendering was evaluated separately because it affects the usability of the generated questions rather than the accuracy of the underlying content.

---

## Test 1: Baseline Generation

**Objective:** Evaluate the quality of questions generated using the revised V2 prompt.

**Course Material Used:** Logistic Regression

**Number of Questions Generated:** 9

Generated questions, answers, and explanations can be found at: `/doc/evaluations/multiple_choice/v2/v2_test1.md`

### Evaluation Results

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Accuracy | 5 / 5 | All nine questions had defensible correct answers. |
| Grounding | 5 / 5 | Questions and explanations remained supported by the original notes. |
| Distractor Quality | 3 / 5 | Several incorrect options were still relatively easy to eliminate. |
| Explanation Quality | 4 / 5 | Some explanations included more useful reasoning and relationships than V1. |
| Coverage & Variety | 3 / 5 | Questions included mathematical interpretation but still emphasized recall and repeated familiar concepts. |
| **Total** | **20 / 25** | Some improvement in explanations, but no overall score increase from V1. |

### Question-Level Issues

**Questions with incorrect or ambiguous answers:**

No clearly incorrect answer keys were identified.

**Questions containing unsupported information:**

None identified.

**Questions with weak distractors:**

Questions 1, 3, 5, and 7 contained incorrect options that were relatively easy to eliminate. For example, Question 5 included distractors suggesting that linear regression cannot calculate an intercept or can only handle negative weights.

**Questions with insufficient explanations:**

Questions 8 and 9 provided accurate explanations but mostly repeated the formulas used in the correct answers.

### Observations

**What worked well?**

Gemini generated nine accurate questions covering important Logistic Regression concepts. The revised prompt produced some stronger explanations, particularly for classification thresholds, decision boundaries, and the relationship between the logit and sigmoid function.

Question 4 was an improvement over V1 because it required students to connect the classification threshold of 0.5 with the logit value of zero, rather than simply identifying the probability threshold.

Question 8 also included mathematical notation for computing the logit using multiple features.

LaTeX rendering appeared to work correctly throughout this test.

**What could be improved?**

Distractor quality remained inconsistent. Several incorrect options were obviously wrong, making it possible to identify the correct answer without much understanding.

Although the prompt encouraged application-based questions, Gemini did not generate any numerical calculations using the examples available in the notes.

The questions also overlapped substantially with the concepts tested in V1.

### Overall Assessment

V2 Test 1 received the same overall score as V1 Test 1, 20/25.

The revised prompt showed some improvement in explanation quality and mathematical interpretation, but the distractors remained weak and question variety decreased slightly.

The results suggest that the prompt revisions may help with certain aspects of question quality, but additional testing is needed to determine whether those improvements are consistent.

---

## Test 2: Repeatability

**Objective:** Evaluate whether the V2 prompt produces consistently useful questions when given the same source material.

**Course Material Used:** Same Logistic Regression notes as Test 1

**Number of Questions Generated:** 8

Generated questions, answers, and explanations can be found at: `/doc/evaluations/multiple_choice/v2/v2_test2.md`

### Evaluation Results

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Accuracy | 5 / 5 | All eight questions had defensible correct answers. |
| Grounding | 5 / 5 | Questions and explanations remained grounded in the supplied notes. |
| Distractor Quality | 3 / 5 | Several incorrect options were implausible or easy to eliminate. |
| Explanation Quality | 4 / 5 | Some explanations included useful relationships, although others repeated the answer. |
| Coverage & Variety | 2 / 5 | Most questions repeated concepts from Test 1 and relied on recall or basic understanding. |
| **Total** | **19 / 25** | Accurate and grounded, but limited variety and repeated distractor weaknesses. |

### Comparison with Test 1

**Were the generated questions substantially different?**

No. Most questions covered the same concepts as Test 1, including response types, classification thresholds, decision boundaries, feature weights, and the logit.

One new question asked how the logistic regression coefficients are determined, but the overall content remained very similar.

**Was question quality consistent across both runs?**

Accuracy and grounding remained consistent. Both tests received 5/5 in those categories.

Distractor quality also remained at 3/5, suggesting that the revised instructions did not consistently produce more plausible incorrect answers.

**Did Gemini emphasize different concepts or question types?**

Not substantially. Test 2 included some mathematical notation and conceptual relationships, but no numerical calculation questions.

Question 4 provided a useful explanation connecting the sigmoid, the logit, and the decision-boundary formula. However, most questions still required recognizing definitions or relationships rather than applying them.

**Were any problems repeated?**

Yes. Weak distractors and limited question variety appeared again.

Several questions also had correct answers that were noticeably more detailed than the incorrect options.

### Question-Level Issues

**Questions with incorrect or ambiguous answers:**

No clearly incorrect answer keys were identified.

**Questions containing unsupported information:**

None identified.

**Questions with weak distractors:**

Questions 1, 5, 6, and 7 contained particularly weak distractors. For example, Question 6 suggested that logistic regression coefficients could be calculated by taking the square root of the input features.

**Questions with insufficient explanations:**

Question 6 simply stated that the coefficients must be learned from training data without providing additional reasoning. Other explanations were more informative, particularly Questions 3 and 4.

### Overall Assessment

Test 2 received a score of 19/25, slightly below the first V2 test.

The results suggest that the revised prompt continues to produce accurate and grounded questions, but does not consistently improve distractors or question variety.

The overlap between the two generations is particularly noticeable. Despite using the revised prompt, Gemini generated nearly the same types of questions without taking advantage of the numerical examples in the notes.

---

## Test 3: Limited Source Material

**Objective:** Evaluate whether Gemini can generate meaningful questions from shorter notes without introducing unsupported information.

**Course Material Used:** Short N-Grams and Language Models notes

**Number of Questions Generated:** 6

Generated questions, answers, and explanations can be found at: `/doc/evaluations/multiple_choice/v2/v2_test3.md`

### Evaluation Results

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Accuracy | 5 / 5 | All six questions had defensible intended answers. |
| Grounding | 5 / 5 | Questions and explanations remained supported by the supplied notes. |
| Distractor Quality | 3 / 5 | Several incorrect options were implausible or unrelated to the concept being tested. |
| Explanation Quality | 3 / 5 | Some explanations included useful examples, but others repeated the correct answer. |
| Coverage & Variety | 2 / 5 | Only six questions were generated, with limited coverage and mostly recall-based questions. |
| **Total** | **18 / 25** | Accurate and grounded, but limited variety and significant LaTeX rendering issues. |

### Limited-Material Observations

**Did Gemini generate fewer than ten questions when appropriate?**

Yes. Gemini generated six questions from the shortened notes, compared with nine in V1.

This shows that the prompt allows fewer questions to be generated, although it does not necessarily mean Gemini selected the ideal number of questions.

The V2 generation covered fewer concepts than V1 despite using the same source material.

**Did the questions remain grounded in the provided notes?**

Yes. The questions covered concepts from the original notes, including the chain rule, long-context limitations, N-gram history lengths, sequence notation, bigram approximations, and BPE tokens.

No clearly unsupported content was identified.

**Were any questions repetitive or overly similar?**

There was some overlap between questions about N-gram history lengths and bigram approximations.

Most questions focused on identifying definitions, formulas, or relationships. None required students to apply the chain rule to a short sequence or work through a probability calculation.

**Did Gemini introduce unsupported examples, definitions, or explanations?**

No clearly unsupported information was identified. However, several explanations remained shallow.

For example, Question 6 explained that language models often operate over BPE tokens instead of raw words, but did not provide additional reasoning beyond the statement in the notes.

### Question-Level Issues

**Questions with incorrect or ambiguous answers:**

No clearly incorrect intended answer keys were identified. However, mathematical notation failed to render correctly in several questions, making some options difficult to interpret.

**Questions containing unsupported information:**

None identified.

**Questions with weak distractors:**

Questions 2 and 6 contained distractors that were relatively easy to eliminate. Question 6, for example, included joint probability tables as an alternative to tokens.

**Questions with insufficient explanations:**

Questions 4, 5, and 6 contained explanations that largely repeated the correct answer or the notation being tested.

Question 3 was stronger because it explained the general N-gram history length using bigram and trigram examples.

### LaTeX Rendering Issues

Unlike the Logistic Regression tests, several mathematical expressions in Test 3 appeared as raw LaTeX rather than formatted equations.

This affected Questions 1, 2, 4, and 5.

For example, some questions displayed literal commands such as `\mid` and underscore notation instead of properly formatted conditional probabilities and subscripts.

The existing `has_valid_math_delimiters()` function checks whether dollar-sign delimiters are balanced. However, it does not detect mathematical expressions that contain LaTeX commands without delimiters.

This means a question can pass validation even when its mathematical notation does not render correctly.

The issue is especially important for questions involving probability formulas, where students need to distinguish between similar expressions.

### Overall Assessment

The limited-material test received a score of 18/25, the lowest of the three V2 tests.

The questions remained accurate and grounded, but distractors and explanations showed limited improvement. Coverage also decreased compared with V1.

The LaTeX rendering problems revealed an additional weakness that was not apparent during the Logistic Regression tests.

These findings suggest that future improvements should address both prompt quality and mathematical formatting reliability.

---

## Summary of Results

| Evaluation | Accuracy | Grounding | Distractors | Explanations | Coverage | Total |
|---|---|---|---|---|---|---|
| Test 1: Baseline | 5 | 5 | 3 | 4 | 3 | 20 / 25 |
| Test 2: Repeatability | 5 | 5 | 3 | 4 | 2 | 19 / 25 |
| Test 3: Limited Material | 5 | 5 | 3 | 3 | 2 | 18 / 25 |
| **Average** | **5** | **5** | **3** | **3.67** | **2.33** | **19 / 25** |

Across the three tests, Gemini generated 23 multiple-choice questions.

### Comparison with V1

| Evaluation | V1 Score | V2 Score | Difference |
|---|---|---|---|
| Test 1: Baseline | 20 / 25 | 20 / 25 | 0 |
| Test 2: Repeatability | 20 / 25 | 19 / 25 | -1 |
| Test 3: Limited Material | 20 / 25 | 18 / 25 | -2 |
| **Average** | **20 / 25** | **19 / 25** | **-1** |

### Key Findings

**Strengths of the V2 Prompt:**

Across all three tests, Gemini continued to generate accurate questions grounded in the original course notes. No clearly incorrect answer keys or unsupported information were identified.

Some explanations were more informative than those generated in V1, particularly when explaining relationships between classification thresholds, logits, and decision boundaries.

V2 also successfully generated and displayed LaTeX notation in the Logistic Regression tests.

**Weaknesses or Recurring Problems:**

The revised prompt did not consistently improve distractor quality. Several incorrect options were still obviously wrong or unrelated to the concept being tested.

Question variety also decreased. Gemini generated fewer questions in each V2 test than in the corresponding V1 test, and the questions continued to emphasize factual recall and basic conceptual understanding.

The limited-material test also revealed inconsistent LaTeX formatting.

**Answer Length and Distractor Balance:**

Some correct answers remained noticeably longer or more specific than the distractors.

This was particularly apparent in Test 2, where several correct options contained more detailed mathematical or conceptual information.

Although the prompt specifically requested balanced answer options, the results suggest that this instruction was not consistently followed.

**Question Difficulty and Variety:**

Most questions focused on recalling definitions, identifying formulas, or recognizing relationships.

V2 included some stronger mathematical interpretation questions, particularly those involving the logit and decision boundary. However, it still did not generate numerical calculations using the worked examples in the Logistic Regression notes.

The repeated emphasis on similar concepts suggests that simply asking for a mixture of question types may not be enough to encourage greater variety.

**Explanation Quality:**

Explanation quality improved slightly in the first two tests.

Some explanations included additional reasoning or connected related concepts. However, others continued to repeat the correct answer without providing much additional context.

The improvement was not consistent across all three tests.

**LaTeX Reliability:**

LaTeX rendering worked correctly in the Logistic Regression tests but failed for several expressions in the N-Grams test.

The current validation checks balanced delimiters but does not guarantee that mathematical notation is properly formatted or rendered.

This will need additional investigation before the feature can reliably support mathematical course materials.

---

## Prompt Evaluation and Next Steps

### Does the V2 Prompt Need Revision?

**Decision:** Investigate LaTeX formatting and revise the prompt.

**Reasoning:**

The V2 prompt preserved the accuracy and grounding demonstrated in V1, which is encouraging. However, it did not produce a consistent improvement in overall question quality.

The average evaluation score decreased from 20/25 in V1 to 19/25 in V2.

Distractor quality remained unchanged, explanations improved slightly, and question variety decreased.

The LaTeX rendering problems in Test 3 also showed that the new mathematical formatting instructions and validation are not yet reliable.

Because the same notes and evaluation rubric were used for both versions, the results provide a useful comparison. However, the evaluation is still limited to three generations per version, so the differences should not be treated as definitive evidence that V2 performs worse in general.

### Proposed Changes

| Identified Issue | Proposed Change | Supporting Evidence |
|---|---|---|
| Weak distractors | Explore more specific instructions for generating closely related incorrect answers and common misconceptions. | All three V2 tests scored 3/5 for distractor quality. |
| Limited question variety | Consider a more structured approach to selecting distinct concepts and question types before generating questions. | V2 Tests 2 and 3 scored 2/5 for coverage and variety. |
| Shallow explanations | Continue encouraging explanations that include reasoning or clarify a misconception rather than repeating the answer. | Several explanations in Tests 2 and 3 remained repetitive. |
| Inconsistent LaTeX formatting | Investigate generated strings and improve mathematical notation handling and validation. | Test 3 displayed raw LaTeX commands in multiple questions. |
| Answer-length imbalance | Improve instructions for keeping correct and incorrect answers similar in length and specificity. | Some correct answers remained more detailed than distractors. |

### Next Steps

For V3, I would like to focus on improving distractor quality and question variety without sacrificing accuracy or grounding.

Any revised prompt should be tested using the same source notes and evaluation rubric so the results can be compared with V1 and V2.

---

## Final Reflection

**What did I learn from implementing and evaluating Multiple Choice V2?**

One of my biggest takeaways was that adding more detailed prompt instructions does not necessarily produce better results.

I expected the revised prompt to improve distractors, explanations, and question variety. Although some explanations improved, the overall scores did not increase, and the generated questions became less varied.

This reinforced the importance of evaluating AI-generated content rather than assuming that a more specific prompt will automatically perform better.

I also learned that formatting is an important part of evaluating an AI-assisted study tool. Even when the mathematical content is correct, incorrectly rendered notation can make a question confusing or difficult to answer.

**What challenges did I encounter?**

The biggest challenge was improving question difficulty without introducing unsupported information. Gemini continued to generate accurate questions, but many distractors were too obvious, and most questions relied on factual recall.

Another challenge was implementing reliable LaTeX rendering. The notation worked in the Logistic Regression tests, but several expressions failed to render in the N-Grams test. This revealed a limitation in my initial validation approach.

I also encountered a session-state issue where changing the submitted course notes did not clear the previously generated quiz. Fixing this helped ensure that students would not accidentally study questions generated from outdated material.

**What would I improve in future versions?**

For future versions, I want to focus on generating more meaningful questions rather than simply adding more instructions to the prompt.

I would like Gemini to produce stronger distractors, cover a wider range of concepts, and include more application-based questions when the source material supports them.

I also want to improve mathematical formatting validation so that students can reliably study topics involving formulas and notation.

Overall, V2 helped me better understand the difference between improving an AI prompt and improving the complete application. Even when the generated content is accurate, question design, formatting, and application behavior all affect how useful the tool is for studying.