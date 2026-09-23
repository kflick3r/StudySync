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

# Save the course material when the user is ready to study.
if st.button("Start Studying"):
    #Check that there was something entered
    if course_material:
        # Session state persists across apps inside a multipage app
        st.session_state.course_material = course_material
        #When notes are entered, navigate to the study tools selection page
        st.switch_page("pages/study_tools.py")
    else:
        # Prevent the user from continuing without course material.
        st.warning("Please add some course material before starting.")