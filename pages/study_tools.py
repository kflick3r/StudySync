import streamlit as st

# Can't access this page without entering study notes
if "course_material" not in st.session_state:
    st.warning("Please add your course material before choosing a study tool.")

    if st.button("Add Notes"):
        st.switch_page("pages/landing.py")

    # Tells Steamlit to stop executing the current script
    st.stop()

st.title("StudySync - Study Tools")
st.header("How do you want to study?")

# creates two side-by-side containers
col1, col2 = st.columns(2)

# col1 is the top left option - Review Guide
with col1:
    st.subheader("Review Guide")
    st.write(
        "Review key ideas, concepts, definitions, and relationships "
        "from your notes."
    )
    # make the button stretch to fill the available width of its container
    if st.button("Generate Guide", width="stretch"):
        #Change to the review guide page
        st.switch_page("pages/review_guide.py")

# col2 is the top right option - Flashcards
with col2:
    st.subheader("Flashcards")
    st.write(
        "Practice important terms and concepts using recall cards."
    )

    if st.button("Generate Flashcards", width="stretch"):
        #Change to the flashcard page
        st.switch_page("pages/flashcards.py")

# creates two more side-by-side containers under the first set
col3, col4 = st.columns(2)

# col3 is the bottom left option - Multiple Choice
with col3:
    st.subheader("Multiple Choice Questions")
    st.write(
        "Test your understanding with multiple-choice questions "
        "based on your notes."
    )

    if st.button("Start Multiple Choice", width="stretch"):
        #Change to the multiple choice page
        st.switch_page("pages/multiple_choice.py")

# col4 is the bottom right option - Short Response
with col4:
    st.subheader("Short Response Questions")
    st.write(
        "Explain concepts in your own words and receive feedback."
    )

    if st.button("Start Short Response", width="stretch"):
        #Change to the short response page
        st.switch_page("pages/short_response.py")

# horizontal line across the page to separate sections
st.divider()

# If user wants to edit their notes.
if st.button("Edit Notes"):
    #Return to the landing page
    st.switch_page("pages/landing.py")