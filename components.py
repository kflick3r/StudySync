import streamlit as st


# AI Content Warning with CSS Styling to be used in footer
def show_ai_disclaimer():
    st.markdown(
        """
        <div style="
            text-align: center;
            font-size: 0.90rem;
            color: #A8A8A8;
            margin: 1.5rem auto 0 auto;
            max-width: 550px;
            line-height: 1.4;
        ">
            <strong style="color: #D0D0D0;">AI-Generated Content Notice</strong>
            <br>
            StudySync's flashcards and practice questions are generated
            from your notes and are not independently fact-checked.
            Use the Review Guide to flag <strong>potential</strong> inaccuracies,
            and always verify important information with trusted sources.
        </div>
        """,
        unsafe_allow_html=True
    )



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

    # Edit Notes
    with bottom_col2:
        if st.button("Edit Notes", width="stretch"):
            # Open the confirmation dialog instead of navigating immediately.
            confirm_edit_notes()

    #AI Content Warning
    show_ai_disclaimer()
