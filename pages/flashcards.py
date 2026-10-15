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

        st.markdown(
            f"### {current_flashcard['question']}"
        )

        # Reveal or hide the answer
        if st.session_state.show_flashcard_answer:
            st.write(current_flashcard["answer"])

            if st.button("Hide Answer"):
                st.session_state.show_flashcard_answer = False
                st.rerun()

        else:
            if st.button("Reveal Answer"):
                st.session_state.show_flashcard_answer = True
                st.rerun()

        st.divider()

        # Navigation buttons
        previous_column, next_column = st.columns(2)

        with previous_column:
           if st.button(
                "Previous",
                disabled=(current_flashcard_index == 0)
            ):
                st.session_state.current_flashcard_index -= 1
                st.session_state.show_flashcard_answer = False
                st.rerun()

        with next_column:
            if st.button(
                "Next",
                disabled=(
                    current_flashcard_index == total_flashcards - 1
                )
            ):
                st.session_state.current_flashcard_index += 1
                st.session_state.show_flashcard_answer = False
                st.rerun()



# Page Footer
show_study_navigation()