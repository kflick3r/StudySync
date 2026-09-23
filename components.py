import streamlit as st

# Display a confirmation dialog before returning to the notes page.
# The user's current notes are preserved, but saving changes later
# will require generated study materials to be recreated.
@st.dialog("Edit course material?")
def confirm_edit_notes():
    st.write(
        "Your current notes will remain available to edit. "
        "If you save changes, your generated study materials "
        "and practice progress will be reset."
    )

    # Place the Cancel and Edit Notes buttons side by side.
    cancel_col, edit_col = st.columns(2)

    with cancel_col:
        if st.button("Cancel", width="stretch"):
            # Close the dialog by rerunning the current page.
            st.rerun()

    with edit_col:
        if st.button("Edit Notes", width="stretch"):
            # Send the user back to the landing page.
            st.switch_page("pages/landing.py")

            

# Create a function for the footer of every page
def show_study_navigation():
    st.divider()

    st.write("Study another way:")

    # Create four equal columns for the four study tools.
    col1, col2, col3, col4 = st.columns(4)

    #col1 is the Review Guide
    with col1:
        # st.page_link() creates a link to another page in the multipage app
        st.page_link(
            "pages/review_guide.py",
            label="Review Guide"
        )

    #col2 is the Flashcards
    with col2:
        st.page_link(
            "pages/flashcards.py",
            label="Flashcards"
        )

    #col3 is the Multiple Choice Questions
    with col3:
        st.page_link(
            "pages/multiple_choice.py",
            label="Multiple Choice"
        )

    #col4 is the Short Response Questions
    with col4:
        st.page_link(
            "pages/short_response.py",
            label="Short Response"
        )

    #create two bottoms next to each other
    bottom_col1, bottom_col2 = st.columns(2)

    # Return to the Study Tool Selection Page
    with bottom_col1:
        if st.button("← Study Tools", width="stretch"):
            st.switch_page("pages/study_tools.py")

    # Return to the Landing Page
    with bottom_col2:
        if st.button("Edit Notes", width="stretch"):
            # Open the confirmation dialog instead of navigating immediately.
            confirm_edit_notes()


