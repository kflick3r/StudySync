import streamlit as st
from components import show_study_navigation
from services.gemini import generate_review_guide


st.title("Review Guide")

course_material = st.session_state.get("course_material", "")

if not course_material:
    st.warning("Please add some course material before generating a review guide.")
else:
    st.write("Generate a review guide from your NLP course material.")

    if st.button("Generate Review Guide"):
        with st.spinner("Generating your review guide..."):
            try:
                # Call on function from gemini.py
                review_guide = generate_review_guide(course_material)

                # Save the review guide to be accessed again during the current session
                st.session_state.review_guide = review_guide

            except Exception as e:
                st.error(f"Unable to generate review guide: {e}")

    # If a review guide has already been created, display it
    if "review_guide" in st.session_state:
        st.markdown(st.session_state.review_guide)


# Page Footer
show_study_navigation()