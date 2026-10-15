# StudySync: Mid-Semester Project Update

**CSPB 3112 – Professional Development in Computer Science**
**October 15, 2026**

## Original Project and Goals

For my semester project, I am developing **StudySync**, an AI-assisted application that turns student-provided course materials into personalized study resources and interactive practice activities.

My motivation comes from my experience as an online student. AI has been a valuable study companion, helping me organize notes, review difficult concepts, and generate additional practice. I wanted to explore how that support could be built into a more purposeful application that supplements students' learning rather than simply providing answers.

My professional goals are to strengthen my software development skills while gaining practical experience with **LLM API integration, prompt engineering, AI output evaluation, and responsible AI use in education**.

## Changes to the Original Plan

After receiving feedback on my proposal, I narrowed StudySync to focus specifically on **Natural Language Processing (NLP)**, a subject I am currently studying. I also established four tools for my minimum viable product (MVP):

- **Review Guide:** Organizes and summarizes course notes.
- **Flashcards:** Generates questions and answers for active recall.
- **Multiple Choice:** Creates practice questions with feedback.
- **Short Response:** Allows students to explain concepts and receive feedback.

This is a slight shift from my original vision of a more open-ended AI study companion. I am prioritizing structured activities that can be developed and evaluated individually. I would still like to add an **Ask StudySync** feature for open-ended questions and explanations, but I am treating that as a stretch goal if time allows.

I also switched from OpenAI's API to Google's Gemini API after encountering billing requirements during development.

## Accomplishments So Far

At the midpoint of the semester, I have a functioning Streamlit application with **two of the four planned study tools implemented**.

I began by defining the MVP, creating wireframes, and building the application's navigation and session-state management. Students can enter their NLP notes, navigate between study tools, and return to edit their material.

In Week 5, I completed **Review Guide**, which generates an organized study guide from the student's notes. I experimented with several prompt versions and developed an evaluation rubric inspired by SummEval and QAGS, focusing on accuracy, coverage, relevance, organization, and preservation of source information.

I also added a feature that flags potentially incorrect or uncertain statements for students to investigate rather than automatically accepting AI-generated corrections.

In Week 7, I completed **Flashcards V1**. Students can generate up to ten flashcards, reveal answers, navigate through their deck, and shuffle questions. I experimented with prompt revisions to improve question variety and topic coverage, and conducted an initial evaluation of the generated cards.

These features have given me practical experience with Python, Streamlit, Gemini's API, JSON responses, application state, debugging, and prompt engineering.

## Progress Toward Project Assessments

| Original Assessment           | Current Progress                                                                                                                       |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **Course Material Input**     | Complete. Students can submit and edit NLP notes used as context for generation.                                                       |
| **Study Material Generation** | In progress. Review Guide and Flashcards are functional; Multiple Choice and Short Response remain.                                    |
| **Interactive Study Support** | In progress. Flashcards supports active recall, and Short Response will provide feedback. Open-ended questions are now a stretch goal. |
| **AI Output Evaluation**      | In progress. Review Guide has undergone structured evaluation, and Flashcards has received initial testing.                            |
| **Project Documentation**     | Ongoing through my GitHub repository and portfolio website.                                                                            |
| **Professional Growth**       | Ongoing. I have developed new skills in AI integration, prompt engineering, evaluation, and application development.                   |

Although only two study tools are complete, the underlying application structure is already in place, which should make developing the remaining features more manageable.

## Challenges and Reflection

My biggest challenge has been balancing development with my other coursework and professional responsibilities. Some weeks have been particularly busy, requiring me to adjust my original schedule.

I've also learned that **getting an AI feature to technically work is only part of the process**. Evaluating whether the generated content is accurate, useful, and grounded in the student's notes takes considerable experimentation. Prompt engineering has involved quite a bit of trial and error, and even small changes can produce noticeably different results.

This has reinforced my interest in AI evaluation and responsible AI development, particularly in educational applications where students may not recognize incorrect information.

## Goals for the Remainder of the Semester

My main priority is completing **Multiple Choice** and **Short Response**, followed by testing and evaluating the full MVP.

To complete my original project assessments, I plan to:

- Test each study tool using sample NLP notes and evaluate the generated content for accuracy, coverage, relevance, and usefulness.
- Test the application's main workflow, including entering notes, generating materials, navigating between tools, and editing source material.
- Document successful results, limitations, and areas for improvement.
- Complete a final reflection on my technical and professional growth.

Short Response will likely present the biggest challenge because evaluating open-ended answers requires more nuanced feedback than checking multiple-choice responses.

If time allows after completing the MVP and evaluations, I would like to explore adding **Ask StudySync**, a feature that allows students to ask follow-up questions and receive personalized explanations based on their course notes and performance on Multiple Choice and Short Response activities. This could help students identify gaps in their understanding and focus on concepts that need additional review.

Overall, I am happy with my progress. StudySync has grown from an initial idea into a functioning application, and I have gained a better understanding of the challenges involved in building and evaluating AI-assisted software. For the remainder of the semester, I want to prioritize completing a functional, well-tested MVP rather than continuing to expand the project's scope.

---

**Project Repository:** [https://github.com/kflick3r/StudySync](https://github.com/kflick3r/StudySync)

**Professional Portfolio:** [https://kflick3r.github.io/](https://kflick3r.github.io/)
