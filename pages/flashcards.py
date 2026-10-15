import streamlit as st
import random
from components import show_study_navigation
from services.gemini import generate_flashcards

# ------------------------------------
# Title and Generate Flashcard Button
# ------------------------------------

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


# ----------------------
# Display Flashcards
# ----------------------

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

    # -----------------------------
    # Flashcard # out of # display
    # -----------------------------

        # Display the flashcard number on the left
        # and the Shuffle button on the right
        flashcard_number_column, shuffle_column = st.columns([3, 1])
        
        with flashcard_number_column:
            st.write(
                f"Flashcard {current_flashcard_index + 1} "
                f"of {total_flashcards}"
            )

    # ---------------------------
    # Shuffle Flashcards feature
    # ---------------------------
        with shuffle_column:
            # Shuffle the existing flashcards without generating a new deck
            if st.button("Shuffle Flashcards"):
                random.shuffle(st.session_state.flashcards)

                # Return to the first card and hide its answer
                st.session_state.current_flashcard_index = 0
                st.session_state.show_flashcard_answer = False
                # Rerun the page to shuffle question
                st.rerun()

    # ------------------
    # Flashcard Content
    # ------------------

        # Give the flashcard a border
        with st.container(border=True, height="content"):

            st.space("small")

        # -------------------
        # Flashcard Question
        # -------------------

            # Display the Question centered
            # anchor=False disables the automatic link icon
            st.subheader(
                current_flashcard["question"],
                anchor=False,
                text_alignment="center"
            )

            st.space("medium")

        # -----------------
        # Flashcard Answer
        # -----------------

            # Display the answer if it has been revealed
            if st.session_state.show_flashcard_answer:

                # Add margins to the left and right of the answer
                left_margin, answer_column, right_margin = st.columns([1, 4, 1])

                with answer_column:
                    st.markdown(
                        current_flashcard["answer"],
                        text_alignment="center"
                    )

            st.space("medium")

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

# -------------------
# Navigation buttons
# -------------------       

        # Navigation buttons centered beneath the flashcard
        left_spacer, previous_column, next_column, right_spacer = (
            st.columns([2, 1, 1, 2])
        )

        with previous_column:
           if st.button(
                "Previous",
                # Disable the "previous" button on the first question
                disabled=(current_flashcard_index == 0),
                use_container_width=True
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
                ),
                use_container_width=True
            ):
                st.session_state.current_flashcard_index += 1
                st.session_state.show_flashcard_answer = False
                st.rerun()

# ------------
# Page Footer
# ------------
show_study_navigation()
