import streamlit as st

from components import show_study_navigation, track_page_navigation
from services.gemini import generate_short_response

track_page_navigation("short_response")


# ------------------------------------
# Helper Functions
# ------------------------------------

def generate_questions():
    """Generate a fresh set of short response questions."""
    with st.spinner("Generating questions..."):
        try:
            st.session_state.sr_questions = generate_short_response(
                st.session_state.course_material
            )

            # Start the new set at question 1
            st.session_state.sr_current_index = 0

            # Start with no saved answers for the new set
            st.session_state.sr_answers = {}

            # Clear answers typed for the old set of questions
            for key in list(st.session_state.keys()):
                if key.startswith("sr_answer_"):
                    del st.session_state[key]

            st.success("Questions generated successfully!")

        except Exception as error:
            # Gemini's errors carry the HTTP status code. 503 means
            # the model is overloaded, so show a friendly message
            if getattr(error, "code", None) == 503:
                st.warning("Sorry, we're busy right now. Try again soon!")
            else:
                st.error(f"Error generating questions: {error}")


# ------------------------------------
# Page Title and Session State
# ------------------------------------

st.title("Short Response Questions")
st.write("Practice explaining concepts from your NLP course notes.")

if "sr_questions" not in st.session_state:
    st.session_state.sr_questions = []

if "sr_current_index" not in st.session_state:
    st.session_state.sr_current_index = 0

if "sr_answers" not in st.session_state:
    st.session_state.sr_answers = {}

# ------------------------------------
# Generate Questions
# ------------------------------------

if not st.session_state.get("course_material"):

    st.warning(
        "No course material found. Please return to the "
        "landing page and enter your notes."
    )

else:

    label = (
        "Regenerate Questions"
        if st.session_state.sr_questions
        else "Generate Questions"
    )

    if st.button(label):
        generate_questions()

    if st.session_state.sr_questions:

        questions = st.session_state.sr_questions
        current_index = st.session_state.sr_current_index
        question = questions[current_index]

        st.subheader("Your Questions")
        st.write(f"Question {current_index + 1} of {len(questions)}")

        with st.container(border=True):

            st.subheader(question["question"], anchor=False)

            answer = st.text_area(
                "Your answer",
                value=st.session_state.sr_answers.get(current_index, ""),
                key=f"sr_answer_{current_index}",
                height=150
            )

            # Save what the student typed so it survives navigation
            st.session_state.sr_answers[current_index] = answer

        # Navigation buttons
        left_spacer, previous_column, next_column, right_spacer = (
            st.columns([2, 1, 1, 2])
        )

        with previous_column:
            if st.button(
                "Previous",
                disabled=current_index == 0,
                width="stretch"
            ):
                st.session_state.sr_current_index -= 1
                st.rerun()

        with next_column:
            if st.button(
                "Next",
                disabled=current_index == len(questions) - 1,
                width="stretch"
            ):
                st.session_state.sr_current_index += 1
                st.rerun()


# ------------
# Page Footer
# ------------

show_study_navigation()