import streamlit as st

st.title("StudySync")
st.write("AI-assisted NLP study companion")

# Check whether the user already has course material saved.
# If they do, use it as the starting text when editing notes.
existing_material = st.session_state.get("course_material", "")

# Whatever the user types into this box gets assigned to the 
# Python variable `course_material`
course_material = st.text_area(
    "Paste your NLP course notes or study material below:",
    value=existing_material,
    height=300
)

st.warning(
    "**Before You Start Studying**\n\n"
    "StudySync generates flashcards, multiple-choice questions, "
    "and short-response exercises based on your submitted course materials. "
    "These tools do not independently verify the accuracy of your notes.\n\n"
    "**We recommend starting with the Review Guide** to identify "
    "information that may be incorrect or need further verification "
    "before using the other study tools."
)


# Save the course material when the user is ready to study
if st.button("Start Studying"):

    # Check that the student entered material
    if course_material.strip():

        # Compare submitted notes with previously saved notes
        notes_have_changed = (
            course_material != st.session_state.get("course_material", "")
        )

        # Save the submitted course material
        st.session_state.course_material = course_material

        # Reset generated content only when the notes change
        if notes_have_changed:

            # Clear the previous review guide
            st.session_state.pop("review_guide", None)

            # Clear previously generated flashcards
            st.session_state.flashcards = []

            # Reset flashcard navigation
            st.session_state.current_flashcard_index = 0
            st.session_state.show_flashcard_answer = False

        # Navigate to the study tools selection page
        st.switch_page("pages/study_tools.py")

    else:
        # Prevent continuing without course material
        st.warning("Please add some course material before starting.")
