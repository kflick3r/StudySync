import streamlit as st
from components import show_study_navigation

from components import track_page_navigation
track_page_navigation("multiple_choice")


st.title("Multiple Choice Questions")
st.write("Your Multiple Choice Questions will appear here.")

# Page Footer
show_study_navigation()