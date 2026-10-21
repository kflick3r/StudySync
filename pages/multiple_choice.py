import streamlit as st

from components import show_study_navigation, track_page_navigation
from services.gemini import generate_multiple_choice

track_page_navigation("multiple_choice")


# ------------------------------------
# Multiple Choice Button Styling
# ------------------------------------


# ------------------------------------
# Multiple Choice Answer Styling
# ------------------------------------

st.markdown(
    """
    <style>
    /* Style only the multiple-choice answer buttons */
    div.st-key-mc_option_0_0 button,
    div[class*="st-key-mc_option_"] button {
        min-height: 95px;
        height: 100%;
        padding: 12px 16px;
        justify-content: center;
    }

    /* Allow answer text to wrap */
    div[class*="st-key-mc_option_"] button p {
        white-space: normal !important;
        overflow: visible !important;
        text-overflow: clip !important;
        overflow-wrap: anywhere !important;
        text-align: center !important;
        font-size: 16px !important;
        line-height: 1.5 !important;
    }

    /* Keep the selected answer highlighted after checking */
    div[class*="st-key-mc_option_"] button:disabled[kind="primary"] {
        background-color: #B9A7FF !important;
        border-color: #B9A7FF !important;
        color: #241B45 !important;
        opacity: 1 !important;
    }

    /* Ensure the selected answer text remains readable */
    div[class*="st-key-mc_option_"] button:disabled[kind="primary"] p {
        color: #241B45 !important;
    }

    /* Keep selected answers purple when hovering */
    div[class*="st-key-mc_option_"] button[kind="primary"]:hover {
        background-color: #6C63FF !important;
        border-color: #6C63FF !important;
        color: white !important;
    }

    /* Keep selected answer text white */
    div[class*="st-key-mc_option_"] button[kind="primary"]:hover p {
        color: white !important;
    }

    /* Keep checked answers light purple when hovering */
    div[class*="st-key-mc_option_"] button[kind="primary"]:disabled:hover {
        background-color: #B9A7FF !important;
        border-color: #B9A7FF !important;
        color: #241B45 !important;
    }

    div[class*="st-key-mc_option_"] button[kind="primary"]:disabled:hover p {
        color: #241B45 !important;
    }

    /* Use the normal cursor for checked answer buttons */
    div[class*="st-key-mc_option_"] button:disabled {
        cursor: default !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)



# ------------------------------------
# Helper Functions
# ------------------------------------

def reset_quiz_progress():
    """Clear answers and progress without discarding generated questions."""
    st.session_state.mc_current_index = 0
    st.session_state.mc_answers = {}
    st.session_state.mc_selections = {}
    st.session_state.mc_show_results = False


def choose_answer(question_index, option_index):
    """Select an option without submitting it."""
    if question_index not in st.session_state.mc_answers:
        st.session_state.mc_selections[question_index] = option_index


def submit_quiz():
    """Submit all selected answers and display the results."""

    for i in range(len(st.session_state.mc_questions)):

        # Save selections that haven't been checked yet
        if i not in st.session_state.mc_answers:

            selected = st.session_state.mc_selections.get(i)

            if selected is not None:
                st.session_state.mc_answers[i] = selected

    st.session_state.mc_show_results = True


# ------------------------------------
# Page Title and Session State
# ------------------------------------

st.title("Multiple Choice Questions")
st.write("Test your understanding of your NLP course notes.")
st.write(
    "You can check your answers as you go, wait until the end, "
    "or use a combination of both."
)

if "mc_questions" not in st.session_state:
    st.session_state.mc_questions = []

if "mc_current_index" not in st.session_state:
    st.session_state.mc_current_index = 0

if "mc_answers" not in st.session_state:
    st.session_state.mc_answers = {}

if "mc_selections" not in st.session_state:
    st.session_state.mc_selections = {}

if "mc_show_results" not in st.session_state:
    st.session_state.mc_show_results = False


# ------------------------------------
# Generate Questions
# ------------------------------------

if not st.session_state.get("course_material"):

    st.warning(
        "No course material found. Please return to the "
        "landing page and enter your notes."
    )

else:

    if st.button("Generate Questions"):

        with st.spinner("Generating questions..."):

            try:
                generated_questions = generate_multiple_choice(
                    st.session_state.course_material
                )

                if not generated_questions:
                    raise ValueError("No questions were generated.")

                st.session_state.mc_questions = generated_questions
                reset_quiz_progress()

                st.success("Questions generated successfully!")

            except Exception as error:
                st.error(f"Error generating questions: {error}")

    if st.session_state.mc_questions:

        questions = st.session_state.mc_questions
        total_questions = len(questions)
        current_index = st.session_state.mc_current_index
        # Count questions that have a selected answer,
        # whether or not Check Answer was clicked.
        completed = sum(
            1
            for i in range(total_questions)
            if i in st.session_state.mc_answers
            or st.session_state.mc_selections.get(i) is not None
        )

        # -------------------
        # Quiz Results Screen
        # -------------------

        if st.session_state.mc_show_results:

            correct_count = sum(
                st.session_state.mc_answers[i] == question["correct_answer"]
                for i, question in enumerate(questions)
            )

            score = 100 * correct_count / total_questions

            st.subheader(
                "Quiz Complete!",
                anchor=False,
                text_alignment="center"
            )

            st.markdown(
                "<p style='text-align:center'>"
                "You've completed all the questions."
                "</p>",
                unsafe_allow_html=True
            )

            # -------------------
            # Final Score
            # -------------------

            left_margin, results_column, right_margin = (
                st.columns([1, 3, 1])
            )

            with results_column:

                with st.container(border=True):

                    st.metric(
                        "Final Score",
                        f"{correct_count}/{total_questions}"
                    )

                    st.write(f"{score:.0f}% correct")

                    st.progress(correct_count / total_questions)

            # -------------------
            # Try Again
            # -------------------
            
            if st.button(
                "Try Again",
                key="mc_retry_top",
                use_container_width=True
            ):
                reset_quiz_progress()
                st.rerun()
            
            # -------------------
            # Review All Answers
            # -------------------

            st.subheader("Review Your Answers")

            for i, question in enumerate(questions):

                selected = st.session_state.mc_answers[i]
                correct = question["correct_answer"]

                with st.container(border=True):

                    if selected == correct:
                        st.success(f"Question {i + 1}: Correct")
                    else:
                        st.error(f"Question {i + 1}: Incorrect")

                    st.markdown(f"**{question['question']}**")

                    st.write(
                        f"**Your answer:** {chr(65 + selected)}. "
                        f"{question['options'][selected]}"
                    )

                    st.write(
                        f"**Correct answer:** {chr(65 + correct)}. "
                        f"{question['options'][correct]}"
                    )

                    st.write(
                        f"**Explanation:** {question['explanation']}"
                    )

            # -------------------
            # Try Again
            # -------------------

            if st.button(
                "Try Again",
                key="mc_retry_bottom",
                use_container_width=True
            ):

                reset_quiz_progress()
                st.rerun()

        # -------------------
        # Quiz Screen
        # -------------------

        else:

            question = questions[current_index]

            checked = current_index in st.session_state.mc_answers

            selected = (
                st.session_state.mc_answers[current_index]
                if checked
                else st.session_state.mc_selections.get(current_index)
            )

            st.subheader("Your Questions")

            # -------------------
            # Question Progress
            # -------------------

            question_column, progress_column = st.columns([2, 3])

            with question_column:
                st.write(
                    f"Question {current_index + 1} of {total_questions}"
                )

            with progress_column:
                st.progress(
                    completed / total_questions,
                    text=f"{completed} of {total_questions} answered"
                )

            # -------------------
            # Question Content
            # -------------------

            with st.container(border=True):

                st.space("small")

                st.subheader(
                    question["question"],
                    anchor=False,
                    text_alignment="center"
                )

                st.space("small")

                # -------------------
                # Answer Selection
                # -------------------

                # Display answers in a 2 x 2 grid.
                # Streamlit columns stack on narrow screens.

                for row_start in (0, 2):

                    left, right = st.columns(2, gap="medium")

                    for column, option_index in zip(
                        (left, right),
                        (row_start, row_start + 1)
                    ):

                        with column:

                            is_selected = selected == option_index

                            label = (
                                f"{chr(65 + option_index)}. "
                                f"{question['options'][option_index]}"
                            )

                            st.button(
                                label,
                                key=f"mc_option_{current_index}_{option_index}",
                                use_container_width=True,
                                type="primary" if is_selected else "secondary",
                                disabled=checked,
                                on_click=choose_answer,
                                args=(current_index, option_index)
                            )

                st.space("small")

                # -------------------
                # Check Answer
                # -------------------

                if not checked:

                    if st.button(
                        "Check Answer",
                        use_container_width=True,
                        disabled=selected is None
                    ):

                        st.session_state.mc_answers[current_index] = selected
                        st.rerun()

                # -------------------
                # Immediate Feedback
                # -------------------

                else:

                    correct = question["correct_answer"]

                    if selected == correct:

                        st.success("Correct!")

                    else:

                        st.error("Incorrect.")

                        st.write(
                            f"**Correct answer:** {chr(65 + correct)}. "
                            f"{question['options'][correct]}"
                        )

                    st.write(
                        f"**Explanation:** {question['explanation']}"
                    )

                st.space("small")

            # -------------------
            # Navigation Buttons
            # -------------------

            left_spacer, previous_column, next_column, right_spacer = (
                st.columns([2, 1, 1, 2])
            )

            with previous_column:

                if st.button(
                    "Previous",
                    disabled=current_index == 0,
                    use_container_width=True
                ):

                    st.session_state.mc_current_index -= 1
                    st.rerun()

            with next_column:

                # Replace Next with View Results when complete
                if completed == total_questions:

                    if st.button(
                        "View Results",
                        use_container_width=True
                    ):
                        submit_quiz()
                        st.rerun()

                else:

                    if st.button(
                        "Next",
                        disabled=current_index == total_questions - 1,
                        use_container_width=True
                    ):

                        st.session_state.mc_current_index += 1
                        st.rerun()


# ------------
# Page Footer
# ------------

show_study_navigation()
