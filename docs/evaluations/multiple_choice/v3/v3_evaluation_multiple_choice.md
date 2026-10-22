# StudySync: Multiple Choice V3 — Implementation and Evaluation

## Overview

The Multiple Choice feature uses Google's Gemini API to generate up to ten multiple-choice questions from student-provided NLP course materials.

Each question includes four answer options, one correct answer, and an explanation. Students can check their answers individually and review their results at the end of the quiz.

The V1 and V2 evaluations showed that Gemini could consistently generate accurate questions grounded in the original notes. However, distractor quality and question variety remained inconsistent. V2 also introduced LaTeX formatting problems, particularly with the N-Grams notes.

For V3, I focused on improving mathematical notation and encouraging more meaningful questions without sacrificing accuracy or grounding.

The purpose of this evaluation is to determine whether these changes improved the quality and usability of the generated questions.

## Implementation Changes

V3 builds on the previous prompt revisions, including instructions for plausible distractors, useful explanations, question variety, and mathematical notation.

The main areas of focus were:

- **Mathematical Notation:** Improve the formatting of mathematical expressions so that LaTeX displays correctly in the application.
- **Question Variety:** Encourage distinct learning objectives and more application-based questions when the notes support them.
- **Distractor Quality:** Continue encouraging plausible incorrect answers based on related concepts and common misunderstandings.
- **Explanation Quality:** Preserve explanations that include useful reasoning rather than simply repeating the correct answer.
- **Source Grounding:** Continue restricting generated questions, answers, and explanations to the student's original notes.

The existing question validation also checks that each question contains four distinct options, one valid correct-answer index, and balanced mathematical delimiters.

These changes were intended to address the weaknesses identified during V2 testing while preserving the accuracy and grounding demonstrated in earlier versions.

## Evaluation Methodology

I conducted three tests using the V3 prompt without modifying it between generations.

1. **Test 1: Baseline Generation:** Generate questions using the same Logistic Regression notes used in V1 and V2.
2. **Test 2: Repeatability:** Generate another quiz using the same Logistic Regression notes to examine consistency.
3. **Test 3: Limited Source Material:** Generate questions using the same shortened N-Grams and Language Models notes.

Each test was evaluated using the same five criteria from previous versions, scored from 1 to 5.

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

LaTeX rendering was evaluated separately because formatting affects the usability of the questions rather than the accuracy of the underlying content.

---

## Test 1: Baseline Generation

**Objective:** Evaluate the quality of questions generated using the V3 prompt.

**Course Material Used:** Logistic Regression

**Number of Questions Generated:** 7

Generated questions, answers, and explanations can be found at: `/doc/evaluations/multiple_choice/v3/v3_test1.md`

### Evaluation Results

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Accuracy | 5 / 5 | All seven questions had defensible correct answers. |
| Grounding | 5 / 5 | Questions and explanations remained supported by the original notes. |
| Distractor Quality | 3 / 5 | Several incorrect options remained easy to eliminate. |
| Explanation Quality | 4 / 5 | Explanations generally included useful reasoning and mathematical relationships. |
| Coverage & Variety | 3 / 5 | One numerical application question was generated, but overall concept coverage remained limited. |
| **Total** | **20 / 25** | Accurate and grounded, with improved application and mathematical formatting. |

### Question-Level Issues

**Questions with incorrect or ambiguous answers:**

No clearly incorrect answer keys were identified.

**Questions containing unsupported information:**

None identified.

**Questions with weak distractors:**

Questions 1, 5, and 6 contained distractors that were relatively easy to eliminate. For example, Question 6 included alternatives suggesting that a positive feature weight has no influence or forces the predicted probability to equal exactly 1.

**Questions with insufficient explanations:**

Most explanations provided useful supporting information. However, some continued to restate the correct answer with only a small amount of additional reasoning.

### Observations

**What worked well?**

Gemini generated seven accurate questions covering several important Logistic Regression concepts.

The most meaningful improvement was Question 7, which required students to calculate the decision boundary using the provided values of ($w=1$) and ($b=2$).

Rather than simply recognizing the decision-boundary formula, students needed to apply it:

$$wx+b=0$$

$$1x+2=0$$

$$x=-2$$

This was an improvement over V2, which did not generate numerical calculation questions despite the example being available in the notes.

The mathematical expressions also rendered correctly throughout the test.

**What could be improved?**

Several distractors were still obviously incorrect or unrelated to the concept being tested.

Although V3 successfully generated a numerical application question, most questions continued to focus on familiar definitions and relationships.

The quiz also generated only seven questions despite the source notes containing additional concepts that could potentially support distinct questions.

### Overall Assessment

V3 Test 1 received a score of 20/25.

The prompt preserved the accuracy and grounding demonstrated in earlier versions while successfully generating a numerical application question.

However, distractor quality and overall question variety remained inconsistent.

---

## Test 2: Repeatability

**Objective:** Evaluate whether the V3 prompt produces consistently useful questions when given the same source material.

**Course Material Used:** Same Logistic Regression notes as Test 1

**Number of Questions Generated:** 6

Generated questions, answers, and explanations can be found at: `/doc/evaluations/multiple_choice/v3/v3_test2.md`

### Evaluation Results

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Accuracy | 5 / 5 | All six questions had defensible correct answers. |
| Grounding | 5 / 5 | Questions and explanations remained grounded in the supplied notes. |
| Distractor Quality | 3 / 5 | Several distractors were implausible or easy to eliminate. |
| Explanation Quality | 4 / 5 | Explanations were generally clear and included supporting reasoning. |
| Coverage & Variety | 3 / 5 | Included mathematical interpretation but repeated many concepts from Test 1. |
| **Total** | **20 / 25** | Consistent accuracy and grounding, but limited question variety. |

### Comparison with Test 1

**Were the generated questions substantially different?**

Not substantially.

Both tests covered similar Logistic Regression concepts, including classification probabilities, thresholds, decision boundaries, feature weights, and the sigmoid function.

Test 2 included a question requiring students to identify the decision-boundary formula ($x=-b/w$), but it did not generate another numerical calculation.

**Was question quality consistent across both runs?**

Yes, in most categories.

Accuracy and grounding remained at 5/5, and both tests received an overall score of 20/25.

Distractor quality also remained at 3/5, suggesting that the revised instructions still did not consistently produce challenging incorrect options.

**Did Gemini emphasize different concepts or question types?**

Only slightly.

Test 1 included a numerical calculation, while Test 2 focused more on identifying formulas and understanding conceptual relationships.

Both generations still emphasized a relatively small set of familiar concepts.

**Were any problems repeated?**

Yes. Weak distractors, limited coverage, and repeated concepts appeared in both tests.

### Question-Level Issues

**Questions with incorrect or ambiguous answers:**

No clearly incorrect answer keys were identified.

**Questions containing unsupported information:**

None clearly identified.

**Questions with weak distractors:**

Questions 1, 4, and 6 contained relatively easy distractors.

For example, Question 1 included clustering unlabeled observations and transforming categorical variables into dummy variables as alternatives to logistic regression's purpose.

**Questions with insufficient explanations:**

Most explanations were accurate and useful, although some primarily restated familiar relationships from the notes.

### Overall Assessment

Test 2 received a score of 20/25, matching Test 1.

The results suggest that V3 consistently preserves accuracy and grounding, but improvements in question difficulty and variety are less reliable.

The numerical application question generated in Test 1 did not appear in Test 2, despite using the same source material.

---

## Test 3: Limited Source Material

**Objective:** Evaluate whether Gemini can generate meaningful questions from shorter notes without introducing unsupported information, while checking mathematical rendering.

**Course Material Used:** Short N-Grams and Language Models notes

**Number of Questions Generated:** 7

Generated questions, answers, and explanations can be found at: `/doc/evaluations/multiple_choice/v3/v3_test3.md`

### Evaluation Results

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Accuracy | 5 / 5 | All seven questions had defensible correct answers. |
| Grounding | 5 / 5 | Questions and explanations remained supported by the original notes. |
| Distractor Quality | 3 / 5 | Several incorrect options were implausible or unrelated. |
| Explanation Quality | 4 / 5 | Most explanations included useful reasoning or supporting relationships. |
| Coverage & Variety | 3 / 5 | Covered several important concepts, but some questions tested equivalent information. |
| **Total** | **20 / 25** | Accurate and grounded, with improved LaTeX rendering but continued repetition. |

### Limited-Material Observations

**Did Gemini generate fewer than ten questions when appropriate?**

Yes. Gemini generated seven questions from the shortened notes.

This demonstrates that the prompt allows fewer than ten questions, although it does not establish whether seven was the ideal number.

**Did the questions remain grounded in the provided notes?**

Yes.

The questions covered sequence notation, the chain rule, long-context limitations, the Markov assumption, trigram history lengths, and bigram approximations.

No clearly unsupported information was identified.

**Were any questions repetitive or overly similar?**

Yes.

Questions 1 and 7 tested nearly equivalent notation.

Question 1 asked about ($w_{1:n-1}$), while Question 7 asked about ($w_{<n}$). Both represent the sequence of words preceding the current word.

Although the questions used different notation, they tested essentially the same learning objective.

Questions 4, 5, and 6 also focused on related aspects of N-gram context lengths, although they addressed different relationships.

**Did Gemini introduce unsupported examples, definitions, or explanations?**

No clearly unsupported information was identified.

However, some explanations remained shallow, particularly when the question only required identifying notation.

### Question-Level Issues

**Questions with incorrect or ambiguous answers:**

No clearly incorrect answer keys were identified.

**Questions containing unsupported information:**

None identified.

**Questions with weak distractors:**

Questions 2, 3, and 7 contained relatively weak distractors.

For example, Question 3 included the suggestion that computers cannot multiply more than three conditional probabilities.

Question 6 was stronger because the distractors represented different context lengths and required students to distinguish between related N-gram formulations.

**Questions with insufficient explanations:**

Question 7 mostly repeated the definition of the notation being tested.

Question 5 provided a stronger explanation by connecting trigram context length to the general ($N-1$) relationship.

### LaTeX Rendering

One of the most important improvements in V3 was the successful rendering of mathematical notation.

In V2 Test 3, several expressions displayed raw LaTeX commands rather than formatted mathematical expressions.

In V3 Test 3, the mathematical expressions appeared correctly throughout the generated questions, answer options, and explanations.

This included conditional probabilities, sequence notation, subscripts, and the chain-rule formula.

However, the existing delimiter validation only checks whether dollar signs are balanced. It does not guarantee that every mathematical expression is syntactically valid or will render correctly.

The successful results are encouraging, but additional testing would be needed to establish reliability across different mathematical topics.

### Overall Assessment

Test 3 received a score of 20/25, improving on the V2 Test 3 score of 18/25.

The clearest improvement was mathematical rendering. Unlike V2, the N-Grams questions displayed correctly.

Explanation quality also improved, but distractor quality and question variety remained inconsistent.

The repetition between Questions 1 and 7 suggests that future revisions should place more emphasis on identifying distinct learning objectives before generating questions.

---

## Summary of Results

| Evaluation | Accuracy | Grounding | Distractors | Explanations | Coverage | Total |
|---|---|---|---|---|---|---|
| Test 1: Baseline | 5 | 5 | 3 | 4 | 3 | 20 / 25 |
| Test 2: Repeatability | 5 | 5 | 3 | 4 | 3 | 20 / 25 |
| Test 3: Limited Material | 5 | 5 | 3 | 4 | 3 | 20 / 25 |
| **Average** | **5** | **5** | **3** | **4** | **3** | **20 / 25** |

Across the three tests, Gemini generated 20 multiple-choice questions.

### Comparison with V1 and V2

| Evaluation | V1 Score | V2 Score | V3 Score |
|---|---|---|---|
| Test 1: Baseline | 20 / 25 | 20 / 25 | 20 / 25 |
| Test 2: Repeatability | 20 / 25 | 19 / 25 | 20 / 25 |
| Test 3: Limited Material | 20 / 25 | 18 / 25 | 20 / 25 |
| **Average** | **20 / 25** | **19 / 25** | **20 / 25** |

| Metric | V1 | V2 | V3 |
|---|---|---|---|
| Total questions generated | 29 | 23 | 20 |
| Numerical application questions | No | No | Yes, Test 1 |
| LaTeX rendering issues observed | Not a focus of V1 | Yes, Test 3 | None observed |
| Recurring weak distractors | Yes | Yes | Yes |
| Repeated or overlapping concepts | Yes | Yes | Yes |

### Key Findings

**Strengths of the V3 Prompt:**

Across all three tests, Gemini continued to generate accurate questions grounded in the original course notes.

V3 also successfully generated a numerical application question using the Logistic Regression decision-boundary example.

Mathematical notation rendered correctly throughout all three tests, including the N-Grams test that previously caused problems.

Explanations were generally clear and included useful supporting information.

**Weaknesses or Recurring Problems:**

Distractor quality remained the most consistent weakness. All three tests received 3/5 in this category.

Several incorrect options were still obviously wrong or unrelated to the question.

Question variety also remained limited. Gemini frequently returned to the same concepts, even when the source notes contained additional material.

The total number of questions decreased again, from 29 in V1 to 23 in V2 and 20 in V3.

Generating fewer questions is not necessarily a problem, but it becomes concerning when distinct concepts from the notes are left untested.

**Question Difficulty and Variety:**

V3 demonstrated that Gemini can generate application-based questions when the source material includes numerical examples.

However, this improvement was not consistent across repeated generations.

Most questions continued to test definitions, formulas, and basic conceptual relationships.

**Explanation Quality:**

Explanation quality was relatively consistent across V3.

Most explanations included relevant relationships or supporting details. However, some still repeated the correct answer without adding much instructional value.

**LaTeX Reliability:**

Mathematical rendering improved substantially compared with V2.

The N-Grams test successfully displayed expressions that previously appeared as raw LaTeX commands.

This is an encouraging result, although additional testing is needed before considering mathematical rendering fully reliable.

---

## Prompt Evaluation and Next Steps

### Does the V3 Prompt Need Revision?

**Decision:** Preserve the mathematical formatting improvements and continue refining question selection and distractor quality.

**Reasoning:**

V3 maintained the accuracy and grounding demonstrated in previous versions and improved mathematical rendering.

The average evaluation score increased from 19/25 in V2 to 20/25 in V3, matching V1.

However, the overall question quality did not improve substantially.

Distractor quality remained unchanged, and the generated questions continued to emphasize familiar concepts rather than exploring the full range of material.

The results suggest that future improvements should focus on how Gemini selects questions, rather than simply adding more instructions about question quality.

### Proposed Changes

| Identified Issue | Proposed Change | Supporting Evidence |
|---|---|---|
| Weak distractors | Encourage incorrect options based on closely related concepts or realistic mistakes. | All three V3 tests scored 3/5 for distractor quality. |
| Repeated learning objectives | Encourage Gemini to identify distinct concepts before generating questions. | Test 3 Questions 1 and 7 tested equivalent notation. |
| Limited application questions | Encourage calculations and interpretation when worked examples are available. | Only Test 1 included a numerical calculation. |
| Reduced question coverage | Improve concept selection so fewer important topics are overlooked. | V3 generated only 20 questions across three tests. |
| Mathematical rendering | Preserve the current formatting approach and continue testing it with additional material. | All three V3 tests displayed LaTeX correctly. |

### Next Steps

For V4, I would like to focus on improving coverage and question diversity without sacrificing accuracy or grounding.

Rather than making the prompt significantly longer, I want to explore whether a more structured approach to identifying learning objectives can help Gemini generate a wider variety of questions.

I also want to continue improving distractor quality and test whether the current mathematical formatting approach works consistently with other topics.

Any revised prompt should be evaluated using the same source notes and rubric so the results remain comparable.

---

## Final Reflection

**What did I learn from implementing and evaluating Multiple Choice V3?**

One of my biggest takeaways was that improving one part of an AI-generated feature does not necessarily improve the entire output.

V3 successfully addressed the LaTeX rendering problems observed in V2, and it generated a numerical application question that earlier versions had missed.

However, the overall evaluation scores remained similar, and several of the same weaknesses continued to appear.

This reinforced the importance of evaluating different aspects of AI-generated content separately rather than relying only on an overall score.

**What challenges did I encounter?**

The biggest challenge continues to be generating questions that are both accurate and meaningful.

Gemini consistently produces correct answers grounded in the notes, but many distractors are too easy to eliminate.

Another challenge is question variety. Even when the notes contain several concepts, Gemini tends to return to familiar definitions and relationships.

The decreasing number of generated questions also raises questions about how the prompt balances quality requirements with coverage.

**What would I improve in future versions?**

For future versions, I want to focus more on how Gemini selects the concepts it tests.

I would like the application to generate questions that cover a wider range of learning objectives, include realistic distractors, and encourage students to apply what they have learned rather than simply recognize definitions.

I also want to continue testing mathematical notation with different types of course material.

Overall, V3 made meaningful progress in mathematical formatting and demonstrated some improvement in application-based question generation. However, the evaluation also showed that accurate and correctly formatted questions are not necessarily challenging or comprehensive.

For the next iteration, I want to prioritize question quality and coverage while preserving the improvements that are already working.