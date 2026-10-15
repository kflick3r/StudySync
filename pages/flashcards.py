import streamlit as st

from components import show_study_navigation
from services.gemini import generate_flashcards


st.title("Flashcards")
st.write("Generate flashcards from your NLP course notes.")

# Check whether the student has entered course material
if not st.session_state.get("course_material"):
    st.warning(
        "No course material found. Please return to the "
        "landing page and enter your notes."
    )

else:
    # Initialize storage for generated flashcards
    # Unless the flashcards have been previously built
    if "flashcards" not in st.session_state:
        st.session_state.flashcards = []

    # Track which flashcard the student is viewing
    if "current_flashcard_index" not in st.session_state:
        st.session_state.current_flashcard_index = 0

    # Track whether the answer is visible
    if "show_flashcard_answer" not in st.session_state:
        st.session_state.show_flashcard_answer = False

    # Generate flashcards from the saved course material
    if st.button("Generate Flashcards"):
        with st.spinner("Generating flashcards..."):
            try:
                generated_flashcards = generate_flashcards(
                    st.session_state.course_material
                )

                st.session_state.flashcards = generated_flashcards

                # Start at the first card with the answer hidden
                st.session_state.current_flashcard_index = 0
                st.session_state.show_flashcard_answer = False

                st.success("Flashcards generated successfully!")

            except Exception as error:
                st.error(
                    f"Error generating flashcards: {error}"
                )

    
    # Display one flashcard at a time
    if st.session_state.flashcards:
        st.subheader("Your Flashcards")

        current_flashcard_index = (
            st.session_state.current_flashcard_index
        )

        total_flashcards = len(st.session_state.flashcards)

        current_flashcard = st.session_state.flashcards[
            current_flashcard_index
        ]

        st.write(
            f"Flashcard {current_flashcard_index + 1} "
            f"of {total_flashcards}"
        )

        # Give the flashcard a border
        with st.container(border=True):

            # Display the Question centered
            # ### = Markdown header 3
            st.markdown(
                f"### {current_flashcard['question']}",
                text_alignment="center",
            )

            # Display the answer if it has been revealed
            if st.session_state.show_flashcard_answer:
                st.markdown(
                    current_flashcard["answer"],
                    text_alignment="center"
                )

            # Create three columns to center the buttons
            left_column, center_column, right_column = st.columns([1, 1, 1])

            with center_column:

                # If the answer is visible, show the Hide Answer button
                if st.session_state.show_flashcard_answer:
                    if st.button("Hide Answer", use_container_width=True):
                        st.session_state.show_flashcard_answer = False
                        # Rerun the page to hide the answer
                        st.rerun()

                # Otherwise, show the Reveal Answer button
                else:
                    if st.button("Reveal Answer", use_container_width=True):
                        st.session_state.show_flashcard_answer = True
                        # Rerun the page to show the answer
                        st.rerun()
            
        # Navigation buttons
        previous_column, next_column = st.columns(2)

        with previous_column:
           if st.button(
                "Previous",
                # Disable the "previous" button on the first question
                disabled=(current_flashcard_index == 0)
            ):
                st.session_state.current_flashcard_index -= 1
                st.session_state.show_flashcard_answer = False
                st.rerun()

        with next_column:
            if st.button(
                "Next",
                # Disable the "next" button on the last question
                disabled=(
                    current_flashcard_index == total_flashcards - 1
                )
            ):
                st.session_state.current_flashcard_index += 1
                st.session_state.show_flashcard_answer = False
                st.rerun()

# Page Footer
show_study_navigation()