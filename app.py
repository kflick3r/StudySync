import streamlit as st

# st.Page() defines a page, 
# while st.navigation() creates the navigation system

landing_page = st.Page(
    "pages/landing.py",
    title="Add Notes"
)

study_tools_page = st.Page(
    "pages/study_tools.py",
    title="Study Tools"
)

review_guide_page = st.Page(
    "pages/review_guide.py",
    title="Review Guide"
)

flashcards_page = st.Page(
    "pages/flashcards.py",
    title="Flashcards"
)

multiple_choice_page = st.Page(
    "pages/multiple_choice.py",
    title="Multiple Choice"
)

short_response_page = st.Page(
    "pages/short_response.py",
    title="Short Response"
)

pg = st.navigation(
    [
        landing_page,
        study_tools_page,
        review_guide_page,
        flashcards_page,
        multiple_choice_page,
        short_response_page
    ],
    #Hid the side navigation bar to create my own at the bottom of page
    position="hidden"
)

pg.run()