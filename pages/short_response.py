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

    # Temporary display so we can check the output
    for i, item in enumerate(st.session_state.sr_questions):
        st.write(f"{i + 1}. {item['question']}")


# ------------
# Page Footer
# ------------

show_study_navigation()