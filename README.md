# StudySync
**AI Study Buddy: An Interactive Study Companion for Students**

StudySync is an AI-assisted study application designed to help students turn their own course materials into personalized and interactive study resources.

Rather than simply providing answers, StudySync acts as a study companion that helps students review concepts, practice what they have learned, and identify gaps in their understanding.

The application uses Google's Gemini API to generate study materials and provide feedback based on student-provided course content.

## Project Status

**MVP Complete — Deployed and Tested**

The initial StudySync MVP has been implemented, deployed using Streamlit Community Cloud, and tested across all four study modes.

The MVP focuses specifically on **Natural Language Processing (NLP)** course material. Limiting the initial version to one subject area allowed the application's prompts, generated resources, and AI feedback to be evaluated against familiar course content.

All four study modes are functional in the deployed application.

## Features

Students provide their own NLP course notes or study materials as plain text or Markdown. StudySync uses that material as context for four interactive study modes.

### Review Guide

Generates a structured review guide from the provided course material.

- Identifies important concepts and terminology.
- Organizes information into sections.
- Explains key ideas and relationships.
- Provides Google Search links for additional verification and exploration.

### Flashcards

Generates interactive flashcards for reviewing important terms and concepts.

- Displays one flashcard at a time.
- Allows students to reveal or hide answers.
- Supports navigation between cards.
- Includes a shuffle option for additional practice.

### Multiple Choice

Generates multiple-choice questions based on the provided course material.

- Presents interactive questions with selectable answers.
- Provides immediate feedback after an answer is checked.
- Explains the correct answer.
- Tracks progress through the question set.
- Displays a results summary.
- Allows students to retry questions.

### Short Response

Generates open-ended questions that encourage students to explain concepts in their own words.

- Allows students to write and submit responses.
- Provides optional self-assessment.
- Uses Gemini to evaluate submitted answers.
- Assigns a score from 0–5.
- Identifies what the student answered correctly.
- Highlights areas for improvement.
- Provides stronger example answers.
- Displays an overall results summary.
- Supports retrying questions or generating a new question set.

Gemini's evaluations are intended as study feedback rather than definitive grades.

### Shared Course Material

Students can move between study modes while continuing to use the same course material during their session.

This creates a connected study workflow:

**Provide Course Material → Generate Study Resources → Practice → Receive Feedback**

## Technology

StudySync was developed using:

- **Python** — Core application logic.
- **Streamlit** — Interactive web application and user interface.
- **Google Gemini API** — Study resource generation and short-response evaluation.
- **HTML/CSS** — Interface customization.
- **Plain Text / Markdown** — Supported course material formats.
- **Git and GitHub** — Version control and project management.
- **Streamlit Community Cloud** — Application deployment.

The application uses Streamlit session state to manage course material, generated study resources, and user interactions.

## Running the Application

### Online

StudySync is deployed through Streamlit Community Cloud and can be accessed directly through a web browser.

**Live Application:** [StudySync](https://study-sync-study-buddy.streamlit.app/)

### Running Locally

To run StudySync locally:

1. Clone the GitHub repository.

   ```bash
   git clone <repository-url>
   cd StudySync
   ```

2. Create and activate a virtual environment.

   ```bash
   python -m venv .venv
   ```

   On Windows:

   ```bash
   .venv\Scripts\activate
   ```

   On macOS/Linux:

   ```bash
   source .venv/bin/activate
   ```

3. Install the required dependencies.

   ```bash
   pip install -r requirements.txt
   ```

4. Configure a Google Gemini API key using the application's Streamlit secrets configuration.

   ```toml
   GEMINI_API_KEY = "your-api-key"
   ```

5. Launch the Streamlit application using its main entry-point file.

   ```bash
   streamlit run landing.py
   ```

   The application will open in a local web browser.

**Note:** API keys should never be committed to the repository.

## Testing and Evaluation

StudySync was tested throughout development and after deployment to evaluate functionality, generated content, and the overall student experience.

Testing focused on three primary areas:

### Functional Testing

Each study mode was tested to verify that its core features worked as intended.

Testing included:

- Generating resources from student-provided material.
- Navigating between study modes.
- Revealing and navigating flashcards.
- Submitting and checking multiple-choice answers.
- Submitting short responses for Gemini evaluation.
- Viewing results and feedback.
- Retrying or regenerating practice activities.

All four study modes were successfully tested in the deployed application.

### AI-Generated Content Evaluation

Generated study materials were reviewed for:

- **Accuracy** — Whether the generated information correctly represented the source material.
- **Coverage** — Whether important concepts were included.
- **Relevance** — Whether the generated content remained focused on the provided material.
- **Organization** — Whether the content was clear and useful for studying.

Additional testing examined the usefulness of multiple-choice explanations and short-response feedback.

### Deployment Testing

After deployment, the application was tested in its hosted environment to verify that:

- All four study modes functioned.
- Gemini API requests completed successfully.
- Generated content and feedback displayed correctly.
- Students could complete the intended study workflow.

## AI-Assisted Development

AI assistance was used during development for selected implementation tasks, including designing URL construction for converting verification topics into Google Search links.

AI-assisted suggestions were reviewed, adapted, and tested before being incorporated into the application.

The project also involved designing prompts, implementing application logic, testing generated outputs, and evaluating the effectiveness of the resulting study tools.

## AI in the StudySync Application

StudySync uses the Gemini API to generate study resources from student-provided course material.

The application is designed to keep generated content grounded in the student's source material rather than relying entirely on general model knowledge.

However, AI-generated information may still contain inaccuracies or omissions.

StudySync encourages students to review generated materials critically and verify information when necessary.

Short-response evaluations are intended to help students reflect on their understanding and identify areas for improvement, not replace instructor feedback or formal grading.

## Project Goals

StudySync was developed to gain practical experience with:

- Building an interactive AI-powered application.
- Integrating an LLM API into a Python application.
- Designing prompts and managing context.
- Evaluating AI-generated content for accuracy and usefulness.
- Designing an application around a real student workflow.
- Managing application state and interactive components.
- Testing and debugging an application.
- Deploying a web application for public access.

The project provided experience with the complete development process, from initial planning and feature implementation to testing, evaluation, and deployment.

## Future Development

The NLP-focused MVP serves as the foundation for the broader StudySync concept.

Potential future improvements include:

- Support for additional academic subjects.
- Document uploads, including PDF