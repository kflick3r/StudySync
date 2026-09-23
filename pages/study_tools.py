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

st.write("Review Guide")
st.write("Flashcards")
st.write("Multiple Choice")
st.write("Short Response")