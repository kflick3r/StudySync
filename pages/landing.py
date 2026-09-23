import streamlit as st

st.title("StudySync")
st.write("AI-assisted NLP study companion")

# Whatever the user types into this box gets assigned to the 
# Python variable `course_material`
course_material = st.text_area(
    "Paste your NLP course notes or study material below:",
    height=300
)

if st.button("Start Studying"):
    #Check that there was something entered
    if course_material:
        # Session state persists across apps inside a multipage app
        st.session_state.course_material = course_material
        #When notes are entered, navigate to the study selection page
        st.switch_page("pages/study_tools.py")
    else:
        st.warning("Please add some course material before starting.")