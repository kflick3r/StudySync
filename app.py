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

pg = st.navigation([
    landing_page,
    study_tools_page
])

pg.run()