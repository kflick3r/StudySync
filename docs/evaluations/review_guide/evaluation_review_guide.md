# Review Guide: Development & Evaluation

## Overview

The Review Guide is StudySync's first AI-powered study tool. It uses Google's Gemini API to transform NLP course materials into organized study guides while preserving the accuracy and meaning of the original content.

Development focused on two goals:
- Generate useful, accurate study guides from student-provided materials.
- Evaluate and improve the quality of generated content through systematic testing and prompt engineering.


## Evaluation Methodology

To evaluate the Review Guide, I developed a rubric inspired by **SummEval** and **QAGS**, two approaches to evaluating generated summaries and their factual consistency.

Each guide was evaluated using four criteria:

| Criterion | Description |
|---|---|
| Accuracy | Does the guide accurately represent the source material? |
| Coverage | Are important concepts and details preserved? |
| Relevance | Is the content useful for studying the topic? |
| Organization | Is the guide clear, structured, and readable? |

Each criterion received a score from 1–5, giving each individual test a maximum of **20 points**. Scores were combined across tests, meaning five tests could earn a maximum of **100 points**.

I also used a QAGS-inspired evaluation by creating five questions for each test based on the original source material and checking whether the generated guide contained enough information to answer them correctly.

Testing included both structured NLP notes previously developed with LLM assistance and raw textbook excerpts. This helped evaluate how well the tool handled different types of source material.

## Prompt Versions

Each prompt version was developed based on the results and challenges identified during testing. The full prompts are available below.

| Version | Focus | Prompt |
|---|---|---|
| V1 | Initial baseline | [View V1](./prompt_v1.md) |
| V2 | Technical accuracy and examples | [View V2](./prompt_v2.md) |
| V3 | Identifying questionable information | [View V3](./prompt_v3.md) |
| V4 | Refining correctness detection | [View V4](./prompt_v4.md) |

The following sections summarize the development process, evaluation results, and improvements made between versions.

## Prompt Development

### V1 — Establishing a Baseline

The initial prompt instructed Gemini to organize course material into a clear review guide without introducing unsupported information.

Five NLP topics were tested: Tokenization, Logistic Regression, Naive Bayes, N-Grams, and Regular Expressions.

**Results:** 97/100 rubric points across five tests and 25/25 source questions answered correctly.

Although performance was strong, testing revealed three issues:
- Mathematical formatting was occasionally incorrect.
- Some supporting examples were omitted from textbook material.
- Minor technical inaccuracies appeared when summarizing complex concepts.

These findings guided the next prompt revision.

### V2 — Preserving Technical Details

V2 added explicit instructions to preserve mathematical notation, technical terminology, and important supporting examples without changing their meaning.

The same five topics were evaluated again.

**Results:** 100/100 rubric points across five tests and 25/25 source questions answered correctly.

V2 improved the preservation of formulas, examples, and technical details while maintaining the clarity of the generated guides. Minor formatting issues remained, but they did not affect the evaluation scores.

Based on these results, V2 became the baseline for further development.

### V3 — Identifying Potentially Incorrect Information

The next goal was to help students identify questionable information in their own notes.

V3 introduced a **Notes to Review for Correctness** section. Rather than automatically correcting potentially inaccurate statements, the guide would flag them and provide a suggested Google Search topic for independent verification.

To test this feature, I intentionally introduced two incorrect or contradictory statements into the Tokenization notes.

**Results (one test):** 20/20 rubric points, 5/5 source questions correct, and both intentional issues flagged.

StudySync successfully generated clickable Google Search links for the flagged statements.

However, Gemini sometimes included its own suggested correction in the explanation. This raised an important design question: how much should the AI explain versus leaving verification to the student?

### V4 — Refining the Correctness Review

V4 refined the instructions to reduce unnecessary flags and discourage AI-generated corrections.

The updated prompt emphasizes that:

- Only meaningful potential factual inaccuracies should be flagged.
- Simplifications, missing details, and alternative terminology are not automatically errors.
- Gemini should explain the concern without presenting its own correction as fact.
- Finding no potential inaccuracies is an acceptable outcome.

This version represents the current direction of the Review Guide's correctness-review feature. Additional testing is needed to determine whether these changes improve its reliability.

## Evaluation Results

The most directly comparable results come from V1 and V2, which were evaluated on the same five NLP topics.

| Metric | V1 | V2 |
|---|---:|---:|
| Accuracy | 23/25 | 25/25 |
| Coverage | 24/25 | 25/25 |
| Relevance | 25/25 | 25/25 |
| Organization | 25/25 | 25/25 |
| **Total (5 tests)** | **97/100** | **100/100** |
| Source Questions | 25/25 | 25/25 |

Both versions answered all source-based questions correctly, but the rubric identified improvements in technical accuracy and coverage.

V3 received 20/20 in its single documented test, including successful detection of both intentional issues. Because it was evaluated on fewer samples, its results are not directly comparable to the five-test totals for V1 and V2.

V4 introduced further changes to correctness detection but has not yet undergone an equivalent documented evaluation.

## Reflection & Next Steps

Developing the Review Guide showed me that getting an LLM-powered feature to work is only the beginning. Evaluating the quality of its output requires careful testing, iteration, and prompt engineering.

The biggest improvement came from making the prompt more explicit about preserving technical details and supporting examples. However, the correctness-review feature introduced a more complicated challenge: helping students recognize questionable information without encouraging them to blindly trust AI-generated corrections.

For now, I consider the Review Guide functional, with V2's summarization instructions serving as the established baseline and V4's correctness-review instructions as the current iteration.

Future improvements may include broader testing with different source materials, measuring false positives and missed errors in the correctness review, and evaluating the feature with more realistic student notes.

The next development priority is expanding StudySync's other study tools, beginning with Flashcards.