import streamlit as st

from components import show_study_navigation, track_page_navigation
from services.gemini import (
    generate_short_response,
    evaluate_short_response,
)

track_page_navigation("short_response")


# ------------------------------------
# Helper Functions
# ------------------------------------

def clear_question_widgets():
    """Remove widget state associated with the previous question set."""
    for key in list(st.session_state.keys()):
        if key.startswith(("sr_answer_", "sr_point_")):
            del st.session_state[key]


def reset_attempt():
    """Restart the existing question set without calling Gemini."""
    st.session_state.sr_current_index = 0
    st.session_state.sr_answers = {}
    st.session_state.sr_revealed = {}
    st.session_state.sr_covered = {}
    st.session_state.sr_evaluations = {}
    st.session_state.sr_show_results = False
    clear_question_widgets()


def generate_questions():
    """Generate a fresh set of short response questions."""
    with st.spinner("Generating questions..."):
        try:
            questions = generate_short_response(st.session_state.course_material)
        except Exception as error:
            if getattr(error, "code", None) == 503:
                st.warning("Sorry, we're busy right now. Try again soon!")
            else:
                st.error(f"Error generating questions: {error}")
            return

    # Only reset the previous attempt after generation succeeds.
    st.session_state.sr_questions = questions
    reset_attempt()
    st.success("Questions generated successfully!")

@st.dialog("Generate new questions?")
def confirm_regenerate():
    st.write(
        "This will replace your current questions and reset "
        "your answers, self-assessments, and evaluations."
    )

    cancel_col, confirm_col = st.columns(2)

    with cancel_col:
        if st.button("Cancel", width="stretch"):
            st.rerun()

    with confirm_col:
        if st.button("Regenerate", type="primary", width="stretch"):
            st.session_state.sr_regenerate = True
            st.rerun()

@st.dialog("Try these questions again?")
def confirm_try_again():
    st.write(
        "This will reset your answers, self-assessments, and "
        "Gemini evaluations so you can retry the same questions."
    )

    cancel_col, confirm_col = st.columns(2)

    with cancel_col:
        if st.button("Cancel", width="stretch"):
            st.rerun()

    with confirm_col:
        if st.button("Try Again", type="primary", width="stretch"):
            reset_attempt()
            st.rerun()


def save_answer_change(index):
    """Save an edited answer and invalidate its previous evaluation."""

    answer = st.session_state[f"sr_answer_{index}"]

    if answer != st.session_state.sr_answers.get(index, ""):
        st.session_state.sr_answers[index] = answer
        st.session_state.sr_evaluations.pop(index, None)


def evaluate_questions(message_container):
    """Evaluate checked answers, retaining successful results if a call fails."""
    questions = st.session_state.sr_questions

    if len(st.session_state.sr_revealed) != len(questions):
        st.warning("Please check all your answers before viewing results.")
        return
    
    pending = [
        i for i in range(len(questions))
        if i not in st.session_state.sr_evaluations
    ]

    if not pending:
        st.session_state.sr_show_results = True
        return

    with message_container.container():
        with st.spinner("Evaluating your answers with Gemini..."):
            for i in pending:
                question = questions[i]
                try:
                    # One automatic retry for Gemini errors
                    for attempt in range(2):
                        try:
                            evaluation = evaluate_short_response(
                                question["question"],
                                st.session_state.sr_answers[i],
                                question["sample_answer"],
                                question["key_points"],
                            )
                            break

                        except ValueError:
                            if attempt == 1:
                                raise
                except Exception as error:
                    if getattr(error, "code", None) == 503:
                        message_container.warning(
                            "Gemini is busy right now. Please try View Results again soon!"
                        )
                    else:
                        message_container.error(
                            f"Could not evaluate question {i + 1}: {error}"
                        )
                    return

                st.session_state.sr_evaluations[i] = evaluation

    message_container.empty()
    st.session_state.sr_show_results = True


def show_results():
    """Show Gemini feedback and compare it with the student's self-assessment."""
    questions = st.session_state.sr_questions
    evaluations = st.session_state.sr_evaluations
    scores = [evaluations[i]["score"] for i in range(len(questions))]

    st.markdown("### Your Results")
    st.markdown("#### Average Gemini Score:")
    st.metric(
        label="",
        value=f"{sum(scores) / len(scores):.1f} / 5",
        label_visibility="collapsed"
    )
    st.caption("Gemini's evaluations are study feedback, not definitive grades.")

    st.divider()

    st.caption("For more detailed feedback, expand the questions below.")

    for i, question in enumerate(questions):
        evaluation = evaluations[i]
        points = question["key_points"]
        student_checks = st.session_state.sr_covered.get(i, {})
        gemini_checks = evaluation["key_point_evaluations"]
        self_count = sum(bool(student_checks.get(j, False)) for j in range(len(points)))
        gemini_count = sum(gemini_checks)

        with st.expander(
            f"**Question {i + 1}:**  {evaluation['score']}/5 — *{question['question']}*",
            expanded=False,
        ):
            st.markdown("**Your Answer**")
            st.write(st.session_state.sr_answers[i])
            st.write("**Stronger Example Answer**")
            st.write(evaluation["stronger_answer"])

            st.subheader(
                f"Gemini Evaluation: {evaluation['score']}/5",
                anchor=False
            )
            st.write("**What You Got Right**")
            st.write(evaluation["strengths"])
            st.write("**What Could Be Improved**")
            st.write(evaluation["improvements"])
            st.write("**Overall Assessment**")
            st.write(evaluation["overall_assessment"])

            st.divider()

            st.markdown("**Optional Self-Assessment vs. Gemini**")
            st.caption(
                "This comparison shows which key points you selected "
                "and which ones Gemini identified in your answer. "
                "Unchecked points may mean you didn't cover them "
                "or chose not to assess them."
            )
            left, right = st.columns(2)
            left.metric("Your Key Points", f"{self_count}/{len(points)}")
            right.metric("Gemini's Key Points", f"{gemini_count}/{len(points)}")

            # Build the self-assessment comparison table
            comparison_data = []

            for j, point in enumerate(points):
                student = bool(student_checks.get(j, False))
                gemini = gemini_checks[j]

                comparison_data.append({
                    "Key Point": point,
                    "You": "✓" if student else "—",
                    "Gemini": "✓" if gemini else "—"
                })

            st.table(comparison_data)

    retry_col, regenerate_col, back_col = st.columns(3)
    with retry_col:
        if st.button("Try Again", width="stretch"):
            confirm_try_again()

    with regenerate_col:
        if st.button("Regenerate Questions", width="stretch"):
            confirm_regenerate()

    with back_col:
        if st.button("Back to Questions", width="stretch"):
            st.session_state.sr_show_results = False
            st.rerun()


# ------------------------------------
# Page Title and Session State
# ------------------------------------

st.title("Short Response Questions")
st.write("Practice explaining concepts from your course notes.")

initial_state = {
    "sr_questions": [],
    "sr_current_index": 0,
    "sr_answers": {},
    "sr_revealed": {},
    "sr_covered": {},
    "sr_evaluations": {},
    "sr_show_results": False,
    "sr_regenerate": False,
}
for key, default in initial_state.items():
    if key not in st.session_state:
        st.session_state[key] = default

# ------------------------------------
# Generate Questions / Results
# ------------------------------------

if not st.session_state.get("course_material"):

    st.warning(
        "No course material found. Please return to the "
        "landing page and enter your notes."
    )

else:
    # Handle confirmed regeneration from either page
    if st.session_state.sr_regenerate:
        st.session_state.sr_regenerate = False
        generate_questions()

        # Refresh the page after successful generation
        st.rerun()

    if st.session_state.sr_show_results and st.session_state.sr_questions:
        show_results()
    else:
        label = (
            "Regenerate Questions"
            if st.session_state.sr_questions
            else "Generate Questions"
        )

        if st.button(label):
            if st.session_state.sr_questions:
                confirm_regenerate()
            else:
                generate_questions()

        if st.session_state.sr_questions:
            questions = st.session_state.sr_questions
            current_index = st.session_state.sr_current_index
            question = questions[current_index]

            st.subheader("Your Questions")
            st.write(f"Question {current_index + 1} of {len(questions)}")

            checked_count = len(st.session_state.sr_revealed)
            st.progress(
                checked_count / len(questions),
                text=f"{checked_count} of {len(questions)} questions checked",
            )

            with st.container(border=True):
                st.subheader(question["question"], anchor=False)
                revealed = current_index in st.session_state.sr_revealed
                answer_key = f"sr_answer_{current_index}"

                # Widget state preserves typed answers during question navigation.
                if answer_key not in st.session_state:
                    st.session_state[answer_key] = st.session_state.sr_answers.get(
                        current_index, ""
                    )

                answer = st.text_area(
                    "Respond with 2-4 sentences:",
                    key=answer_key,
                    height=150,
                    disabled=revealed,
                    on_change=save_answer_change,
                    args=(current_index,),
                )
                if not revealed:
                    st.session_state.sr_answers[current_index] = answer
                    if st.button(
                        "Check Answer",
                        width="stretch",
                    ):
                        if not answer.strip():
                            st.warning("Please enter an answer before checking.")
                        else:
                            st.session_state.sr_answers[current_index] = answer
                            st.session_state.sr_revealed[current_index] = True
                            st.rerun()
                else:
                    st.markdown("**Sample Answer:**")
                    st.write(question["sample_answer"])
                    st.markdown("**Key Points: Tick the ones your answer covered**")

                    covered = st.session_state.sr_covered.setdefault(current_index, {})
                    for j, point in enumerate(question["key_points"]):
                        point_key = f"sr_point_{current_index}_{j}"
                        if point_key not in st.session_state:
                            st.session_state[point_key] = covered.get(j, False)
                        covered[j] = st.checkbox(point, key=point_key)

                    st.write(
                        f"You identified {sum(covered.values())} of "
                        f"{len(question['key_points'])} key points in your self-assessment."
                    )
                    if st.button("Edit Answer", key=f"sr_edit_{current_index}"):
                        st.session_state.sr_revealed.pop(current_index, None)
                        st.session_state.sr_evaluations.pop(current_index, None)
                        st.session_state.sr_covered.pop(current_index, None)

                        for key in list(st.session_state.keys()):
                            if key.startswith(f"sr_point_{current_index}_"):
                                del st.session_state[key]

                        st.rerun()

            evaluation_message = st.empty()

            left_spacer, previous_column, next_column, right_spacer = st.columns(
                [2, 1, 1, 2]
            )
            with previous_column:
                if st.button(
                    "Previous", disabled=current_index == 0, width="stretch"
                ):
                    st.session_state.sr_current_index -= 1
                    st.rerun()
            with next_column:
                is_last_question = current_index == len(questions) - 1
                all_checked = checked_count == len(questions)

                if is_last_question:
                    if st.button(
                        "View Results",
                        disabled=not all_checked,
                        width="stretch"
                    ):
                        evaluate_questions(evaluation_message)

                        if st.session_state.sr_show_results:
                            st.rerun()

                else:
                    if st.button("Next", width="stretch"):
                        st.session_state.sr_current_index += 1
                        st.rerun()


# ------------
# Page Footer
# ------------

show_study_navigation()