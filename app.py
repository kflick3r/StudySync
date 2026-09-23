import streamlit as st

# st.Page() defines a page, 
# while st.navigation() creates the navigation system

landing_page = st.Page(
    "pages/landing.py",
    title="Add Notes"
)

study_home_page = st.Page(
    "pages/study_home.py",
    title="Study Home"
)

pg = st.navigation([
    landing_page,
    study_home_page
])

pg.run()