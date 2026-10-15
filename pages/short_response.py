import streamlit as st
from components import show_study_navigation

from components import track_page_navigation
track_page_navigation("short_response")


st.title("Short Response Questions")
st.write("Your Short Response Questions will appear here.")

# Page Footer
show_study_navigation()