- Project: StudySync 
- Deployment: Streamlit Community Cloud 
- Test material: Logistic Regression for Text Classification
- Testing status: Completed 
- Scope: Four MVP study tools

# 1. Evaluation Design

StudySync is an AI-assisted study companion that transforms student-provided course notes into a review guide, flashcards, multiple-choice practice, and short-response practice with feedback. The same Logistic Regression for Text Classification notes were used for all tests to enable comparisons across tools and generations. The source notes and complete examples are documented in docs/evaluations/final_eval_examples.ipynb.

Three successful generations per tool were manually assessed for content quality using a four-criterion rubric (each criterion scored 0–5, for a maximum of 20). Each rubric was adapted to the purpose of the study tool, allowing evaluation of feature-specific qualities such as organization, study value, and question quality. A separate factual-consistency score (0–5) records whether output accurately reflects the source notes without introducing incorrect or unsupported claims. These are manual judgments, not independently validated measures of educational effectiveness.

Functional testing examined generation, display, interaction, feedback, navigation, error handling, and preservation of existing work. Short Response was additionally tested with 15 deliberately constructed answers spanning correct, incomplete, incorrect, and mixed-quality responses; these were not responses collected from actual students. Gemini scores reflect the intentionally varied test answers, not content-generation quality.

# 2. Results at a Glance

| Feature         | Test 1 | Test 2 | Test 3 | Average     | Factual consistency |
|-----------------|--------|--------|--------|-------------|---------------------|
| Review Guide    | 18/20  | 18/20  | 18/20  | 18/20 (90%) | 4/5                 |
| Flashcards      | 19/20  | 16/20  | 16/20  | 17/20 (85%) | 5/5                 |
| Multiple Choice | 18/20  | 18/20  | 18/20  | 18/20 (90%) | 5/5                 |
| Short Response  | 19/20  | 19/20  | 19/20  | 19/20 (95%) | 5/5                 |
| Overall         | —      | —      | —      | 18/20 (90%) | 4.75/5 (95%)        |

Twelve successful generations were evaluated. Two additional Multiple Choice regeneration attempts failed, for 12 successes in 14 documented generation attempts; this descriptive rate (85.7%) is based on a small, nonrandom sample and should not be treated as a general reliability estimate.

# 3. Review Guide

Rubric: Accuracy, Coverage, Relevance, Organization (5 points each). Three guides were successfully generated from the same notes.

| Criterion           | Test 1 | Test 2 | Test 3 |
|---------------------|--------|--------|--------|
| Accuracy            | 4/5    | 4/5    | 4/5    |
| Coverage            | 4/5    | 4/5    | 4/5    |
| Relevance           | 5/5    | 5/5    | 5/5    |
| Organization        | 5/5    | 5/5    | 5/5    |
| Total               | 18/20  | 18/20  | 18/20  |
| Factual consistency | 4/5    | 4/5    | 4/5    |

## Review Guide — Test 1

Generation: Successful \| Content quality: 18/20 \| Factual consistency: 4/5

### Content observations

- Summarized major concepts, mathematical formulas, regularization, and evaluation metrics.

- Organization was clear and included a useful comparison table.

- Incorrectly suggested logistic regression has no modeling assumptions.

- Omitted numerical examples and some supporting detail; the data-leakage recommendation could better distinguish training, validation, and test sets.

### Assessment

A useful and well-organized study resource, with a recurring need for factual verification of model comparisons.

## Review Guide — Test 2

Generation: Successful \| Content quality: 18/20 \| Factual consistency: 4/5

### Content observations

- Covered text representation, formulas, optimization, regularization, and evaluation metrics.

- Clear explanations and a comparison table supported review.

- Described logistic regression as having “minimal” assumptions, oversimplifying the comparison with Naive Bayes.

- Omitted numerical examples, probability calibration, and distinctions among gradient-descent variants.

- Included helpful advice on cross-validation, error analysis, and preventing leakage.

### Assessment

Strong core coverage and organization, with some omitted details and an oversimplified statement about assumptions.

## Review Guide — Test 3

Generation: Successful \| Content quality: 18/20 \| Factual consistency: 4/5

### Content observations

- Accurately summarized major topics and provided a useful comparison table.

- Repeated the incorrect claim that logistic regression has no modeling assumptions.

- Omitted numerical examples, probability calibration, and distinctions among gradient-descent variants.

- Included useful cross-validation, data-leakage, and classification-error recommendations.

### Assessment

The guide remained useful for studying but required factual verification, especially of the model-comparison statement.

## Review Guide — Final Findings

Average content quality was 18/20 (90%) and factual consistency was 4/5. All three generations succeeded, but all three oversimplified logistic regression’s assumptions. This is a repeated content issue, not an isolated wording problem. A separate usability issue was observed: after a guide is generated, the button still reads “Generate” rather than “Regenerate,” and replacing a guide does not prompt for confirmation. Future work should correct both behaviors.

# 4. Flashcards

Rubric: Accuracy, Coverage, Clarity, Study Value (5 points each). Each generation produced 10 cards.

| Criterion           | Test 1 | Test 2 | Test 3 |
|---------------------|--------|--------|--------|
| Accuracy            | 5/5    | 5/5    | 5/5    |
| Coverage            | 4/5    | 3/5    | 3/5    |
| Clarity             | 5/5    | 4/5    | 4/5    |
| Study Value         | 5/5    | 4/5    | 4/5    |
| Total               | 19/20  | 16/20  | 16/20  |
| Factual consistency | 5/5    | 5/5    | 5/5    |

## Flashcards — Test 1

Generation: Successful \| Content quality: 19/20 \| Factual consistency: 5/5

### Content observations

- All 10 question-answer pairs were factually accurate.

- Questions were concise and encouraged active recall, including model comparisons, regularization, class imbalance, and data leakage.

- No duplicate questions were observed.

- Mathematical formulas, gradient descent, and evaluation calculations received limited attention.

### Assessment

High-quality flashcards with strong clarity and study value, but incomplete coverage of mathematics and optimization.

## Flashcards — Test 2

Generation: Successful \| Content quality: 16/20 \| Factual consistency: 5/5

### Content observations

- All 10 cards were factually accurate and clearly written.

- Two cards covered nearly the same generative-versus-discriminative distinction.

- Binary cross-entropy, gradient descent, learning rate, and the linear-model equation were omitted.

- The F1-score formula on Card 7 appeared as plain text rather than rendered mathematical notation.

### Assessment

Accurate and usable for recall, with reduced topic variety and a minor mathematical-formatting problem.

## Flashcards — Test 3

Generation: Successful \| Content quality: 16/20 \| Factual consistency: 5/5

### Content observations

- All 10 cards were factually accurate.

- Cards 1 and 8 repeated the discriminative-versus-generative comparison.

- Included sigmoid, binary cross-entropy, regularization, metrics, and data leakage.

- Omitted gradient descent, learning rate, the linear-model equation, and numerical examples.

- Cards 3 and 4 displayed mathematical expressions as plain text rather than formatted LaTeX.

### Assessment

Useful content, but repetition, incomplete coverage, and mathematical rendering lowered study value.

## Flashcards — Final Findings

Thirty cards were generated across three successful tests. Average content quality was 17/20 (85%) and factual consistency was 5/5. The recurring limitations were uneven topic coverage, concept repetition, and mathematical expressions shown as plain text in Tests 2 and 3. Improvements should prioritize topic diversity and reliable formula rendering.

# 5. Multiple Choice

Rubric: Accuracy, Coverage, Clarity, Question Quality (5 points each). Three successful quizzes contained 8, 8, and 9 questions, respectively. Additional regeneration attempts are documented separately below.

| Criterion           | Test 1 | Test 2 | Test 3 |
|---------------------|--------|--------|--------|
| Accuracy            | 5/5    | 5/5    | 5/5    |
| Coverage            | 4/5    | 4/5    | 4/5    |
| Clarity             | 5/5    | 5/5    | 5/5    |
| Question Quality    | 4/5    | 4/5    | 4/5    |
| Total               | 18/20  | 18/20  | 18/20  |
| Factual consistency | 5/5    | 5/5    | 5/5    |

## Multiple Choice — Test 1

Generation: Successful \| Content quality: 18/20 \| Factual consistency: 5/5

### Content observations

- Eight questions had accurate answers and explanations.

- Topics included discriminative models, sigmoid, regularization, precision, imbalance, Bag-of-Words, and leakage.

- Included sigmoid and precision calculations; formulas rendered correctly.

- Several distractors were easy to eliminate; the explanation for Question 5 more clearly addressed imbalance than the selected answer.

- Gradient descent, binary cross-entropy, and TF-IDF weighting were not directly assessed.

### Functional observations

- Quiz result was 4/8 from deliberately selected answers; the result matched recorded responses.

- Correct/incorrect answers received immediate feedback, checked answers locked, and progress updated.

- Results showed selected and correct answers with explanations. “Try Again” reset and unlocked the quiz without a confirmation dialog.

- The results-page “Regenerate Questions” control displayed a confirmation dialog; the questions-page regeneration attempts did not.

### Assessment

A successful conceptual and numerical quiz with clear explanations; question difficulty and breadth could improve.

## Multiple Choice — Test 2

Generation: Successful \| Content quality: 18/20 \| Factual consistency: 5/5

### Content observations

- Eight accurate questions covered discriminative models, regularization, sigmoid, imbalance, Bag-of-Words, leakage, and binary cross-entropy.

- The binary cross-entropy scenario tested conceptual understanding.

- Some distractors were implausible or unrelated.

- Gradient descent, precision, recall, F1-score, and TF-IDF weighting were not directly assessed.

- Mathematical expressions rendered correctly.

### Functional observations

- The results page correctly recorded one correct and seven incorrect answers (1/8).

### Assessment

Strong content and functional scoring, with relatively easy distractors and incomplete coverage.

## Multiple Choice — Test 3

Generation: Successful \| Content quality: 18/20 \| Factual consistency: 5/5

### Content observations

- Nine questions were accurate, covering discriminative models, sigmoid, binary cross-entropy, L1, imbalance, leakage, Bag-of-Words, and scikit-learn C.

- Included a numerical sigmoid calculation.

- Questions 2 and 7 both tested sigmoid; Question 7 included an unnecessary classification threshold for a probability calculation.

- Some distractors were too easy to eliminate.

- Precision, recall, F1-score, gradient descent, and TF-IDF weighting were not directly assessed.

### Functional observations

- The results page correctly recorded four correct and five incorrect answers (4/9).

### Assessment

Strong factual accuracy and clear explanations, but limited distractor difficulty, repetition, and gaps in topic coverage.

## Multiple Choice — Additional Regeneration Failures

Failure 1: A regeneration attempt displayed “Error generating questions: Invalid \escape: line 25 column 129 (char 1667).” The message suggests malformed JSON escaping; LaTeX backslashes are a possible but unconfirmed cause. No replacement quiz was generated.

Failure 2: A subsequent attempt displayed “Sorry, we’re busy right now. Try again soon!” This could reflect a temporary API or service issue, but the cause was not confirmed from the UI message. No replacement quiz was generated.

Both failures preserved the existing eight-question quiz and left the application usable. This is a positive resilience finding, although it does not resolve the underlying generation reliability issue.

## Multiple Choice — Final Findings

Average content quality was 18/20 (90%), with factual consistency of 5/5 across 25 questions. The quiz workflow provided immediate feedback, answer locking, progress tracking, accurate scoring, and detailed results. Priority improvements are stronger distractors, broader topic coverage, more robust JSON/API error handling, a confirmation before “Try Again,” and consistent regeneration confirmation on both the questions and results pages.

# 6. Short Response

Rubric: Accuracy, Coverage, Clarity, Question Quality (5 points each). Each successful generation produced five questions, sample answers, and key-point checklists. All 15 deliberately varied student responses were successfully evaluated by Gemini.

| Criterion           | Test 1 | Test 2 | Test 3 |
|---------------------|--------|--------|--------|
| Accuracy            | 5/5    | 5/5    | 5/5    |
| Coverage            | 4/5    | 4/5    | 4/5    |
| Clarity             | 5/5    | 5/5    | 5/5    |
| Question Quality    | 5/5    | 5/5    | 5/5    |
| Total               | 19/20  | 19/20  | 19/20  |
| Factual consistency | 5/5    | 5/5    | 5/5    |

## Short Response — Test 1: Generated Content

- Five accurate questions covered discriminative models, L1/L2 regularization, classification metrics, sigmoid, and data leakage.

- Sample answers were accurate and checklists aligned with the questions.

- The questions required explanation rather than simple recall; no significant repetition occurred within the set.

- Gradient descent, binary cross-entropy, and numerical metric calculations were not covered.

Content quality: 19/20 (95%). Factual consistency: 5/5.

## Short Response — Test 1: Gemini Evaluation

| Q   | Response type     | Expected | Gemini |
|-----|-------------------|----------|--------|
| 1   | Fully correct     | 5/5      | 5/5    |
| 2   | Partially correct | 2–3/5    | 4/5    |
| 3   | Incorrect         | 0–1/5    | 0/5    |
| 4   | Mostly correct    | 3–4/5    | 4/5    |
| 5   | Placeholder       | 0/5      | 0/5    |

- Gemini correctly recognized a complete discriminative-versus-generative answer (Q1).

- Q2 received 4/5, higher than anticipated but defensible: although Gemini's score exceeded the anticipated range, the evaluation was considered reasonable because the response correctly explained the conceptual differences between L1 and L2 regularization. This illustrates that Gemini may award substantial credit for conceptual understanding even when mathematical details are omitted.

- Gemini recognized the misconception about accuracy and class imbalance (Q3), the missing probability interpretation of sigmoid output (Q4), and the meaningless placeholder (Q5).

- Average score was 2.6/5 (13/25); all five evaluations were reasonable.

- All self-assessment checkboxes were left unchecked; this did not prevent evaluation. Blank answers were blocked, while the nonempty “placeholder” was accepted and scored 0/5.

- Feedback included strengths, improvements, stronger examples, and overall assessments; the results page displayed expandable evaluations and the correct average.

## Short Response — Test 2: Generated Content

- Five accurate questions covered linear score/sigmoid/threshold, imbalanced-class metrics, L1/L2, logistic regression versus Naive Bayes, and limitations of Bag-of-Words/TF-IDF.

- Sample answers and checklists were generally accurate, and mathematical notation rendered correctly in the deployed application.

- Gradient descent, binary cross-entropy, and some numerical applications were omitted.

Content quality: 19/20 (95%). Factual consistency: 5/5.

## Short Response — Test 2: Gemini Evaluation

| Q   | Response type     | Expected | Gemini |
|-----|-------------------|----------|--------|
| 1   | Fully correct     | 5/5      | 5/5    |
| 2   | Partially correct | 3–4/5    | 3/5    |
| 3   | Incorrect         | 0–1/5    | 0/5    |
| 4   | Mostly correct    | 3–4/5    | 4/5    |
| 5   | Placeholder       | 0/5      | 0/5    |

- Gemini awarded full credit to a complete explanation of the linear score, sigmoid, and threshold (Q1).

- It identified the missing precision/recall/F1 discussion in Q2 and correctly rejected reversed L1/L2 definitions and an incorrect claim about memorization in Q3.

- Q4 received 4/5 because it omitted the Naive Bayes conditional-independence assumption; Q5 received 0/5 for “placeholder.”

- Average score was 2.4/5 (12/25); all five scores were reasonable.

- Student and Gemini key-point selections matched across all five questions, and the comparison table displayed both sets correctly.

## Short Response — Test 3: Generated Content

- Five accurate questions addressed discriminative versus generative models, Bag-of-Words versus TF-IDF, L1/L2, accuracy versus other metrics, and limitations of linear text classification.

- The generated answers were clear and correct; the Q4 checklist defined precision, recall, and F1 more explicitly than its sample answer.

- The set omitted gradient descent, binary cross-entropy, and some numerical applications.

Content quality: 19/20 (95%). Factual consistency: 5/5.

## Short Response — Test 3: Gemini Evaluation

| Q   | Response type              | Expected | Gemini |
|-----|----------------------------|----------|--------|
| 1   | Correct but incomplete     | 3–4/5    | 3/5    |
| 2   | Mixed correct/incorrect    | 2–3/5    | 2/5    |
| 3   | Mostly correct             | 4/5      | 5/5    |
| 4   | Partially correct          | 3–4/5    | 4/5    |
| 5   | Correct with misconception | 2–3/5    | 3/5    |

- Q1: Gemini recognized the discriminative-model explanation but identified missing generative-model detail (3/5). Student selected 3/3 key points versus Gemini’s 1/3.

- Q2: Gemini identified the incorrect claim that TF-IDF favors terms occurring in nearly every document (2/5). Student selected 3/3 versus Gemini’s 2/3.

- Q3: Gemini gave 5/5 to a correct conceptual account of L1 and L2 effects; this was higher than expected but reasonable for the question. Student selected 1/3 versus Gemini’s 3/3.

- Q4: Gemini correctly identified missing F1-score detail (4/5); student and Gemini each selected 3/4 key points.

- Q5: Gemini caught the incorrect claim that logistic regression automatically learns nonlinear decision boundaries (3/5). Student selected 3/3 versus Gemini’s 2/3.

- Average score was 3.4/5 (17/25). Four of five self-assessment comparisons differed as intentionally designed, demonstrating that Gemini did not simply copy student selections.

## Short Response — Final Findings

| Metric                 | Test 1 | Test 2 | Test 3 |
|------------------------|--------|--------|--------|
| Content quality        | 19/20  | 19/20  | 19/20  |
| Factual consistency    | 5/5    | 5/5    | 5/5    |
| Evaluated responses    | 5/5    | 5/5    | 5/5    |
| Reasonable evaluations | 5/5    | 5/5    | 5/5    |
| Average Gemini score   | 2.6/5  | 2.4/5  | 3.4/5  |

All 15 submitted responses received Gemini scores and detailed feedback, and all 15 scores were judged reasonable in manual review. The application calculated averages correctly and displayed individual expandable evaluations. The optional self-assessment remained independent of Gemini’s identified key points, including when students intentionally overestimated or underestimated coverage. Blank-answer validation worked; nonempty placeholders could be submitted and received zero points.

The feature achieved an average content-quality score of 19/20 (95%) and factual consistency of 5/5. These results support its usefulness for formative feedback but do not establish grading reliability across other subjects, students, or answer styles. A usability improvement is to duplicate “Try Again,” “Regenerate Questions,” and “Back to Questions” at the top of the results page, while retaining the existing bottom controls.

# 7. Cross-Feature Findings

## Content quality and accuracy

The four tools averaged 18/20 (90%) on manually assigned content-quality rubrics and 4.75/5 (95%) on factual consistency. Short Response had the highest average quality score (95%); Flashcards had the lowest (85%). The recurring incorrect statement about logistic regression assumptions in Review Guide illustrates why generated study material still needs factual verification.

## Coverage and educational value

All tools produced usable study materials, but none consistently assessed every important concept. Optimization details, gradient descent, and numerical applications were frequently omitted. Repeated concepts appeared in some Flashcards and Multiple Choice sets, while some Multiple Choice distractors were easy to eliminate. StudySync nonetheless supported several complementary study approaches: structured review, recall, selected-response practice, and written explanation.

## Feedback and self-assessment

Multiple Choice provided immediate explanations, accurate results, progress tracking, and answer locking. Short Response generated individualized feedback and a key-point comparison that exposed mismatches between students’ self-assessments and Gemini’s independent judgments. The 15/15 reasonable evaluations are encouraging but reflect a limited, manually reviewed sample of deliberately constructed responses.

## Reliability and usability

All four deployed tools worked in the evaluated successful runs. Two additional Multiple Choice regeneration attempts failed: one returned an invalid JSON escape error, and the other returned a temporary service message. Neither failure erased the existing quiz. UI issues include inconsistent regeneration confirmations, no confirmation before restarting a completed quiz, the Review Guide button/confirmation behavior, Flashcards formula rendering, and inconvenient Short Response results-page navigation.

# 8. Limitations and Next Steps

- Test with additional subjects, note lengths, writing styles, and input formats to evaluate generalization beyond a single NLP note set.

- Use a defined topic-coverage checklist or topic sampling to reduce omissions and repeated questions.

- Compare a larger set of Gemini short-response scores against independent human judgments to assess consistency and potential bias.

- Improve structured-output validation, escaped-character handling, and retry behavior for temporary API failures.

- Fix formula rendering in Flashcards and standardize confirmation dialogs before destructive or replacement actions.

- Improve results-page navigation and other small usability issues identified in testing.

# 9. Overall Assessment

StudySync met its MVP goal of turning student-provided course materials into study resources and interactive practice with feedback. Twelve successful generations across four tools yielded an average manually assessed content-quality score of 90% and factual-consistency score of 95%. The application also completed all 15 Short Response evaluations with reasonable feedback on deliberately varied answers.

The testing exposed meaningful limitations: uneven topic coverage, occasional repetition, oversimplified Review Guide claims, mathematical formatting problems, two failed regeneration attempts, and inconsistent navigation or confirmation behavior. The findings support StudySync as a functional educational prototype—not as a verified grading system or a substitute for reviewing AI-generated material.

The demonstrated MVP workflow is: 
**Provide course material → Generate study resources → Practice the material → Receive feedback.** 
The next phase should focus on reliability, broader evaluation, and usability while preserving StudySync’s emphasis on active learning and self-assessment.
