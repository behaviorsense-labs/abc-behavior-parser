import streamlit as st
from parser import parse_behavior_note

st.set_page_config(page_title="ABC Behavior Parser", page_icon="📝")

st.title("ABC Behavior Parser")

st.write(
    "Educational caregiver-support prototype for organizing child behavior notes "
    "into Antecedent, Behavior, and Consequence structure."
)

note = st.text_area(
    "Enter a behavior observation",
    placeholder="Example: My child got upset when screen time ended and threw the toy.",
)

if st.button("Parse Note"):
    if not note.strip():
        st.warning("Please enter a behavior observation.")
    else:
        result = parse_behavior_note(note)

        st.subheader("ABC Summary")
        st.write(f"**Antecedent:** {result['antecedent']}")
        st.write(f"**Behavior:** {result['behavior']}")
        st.write(f"**Consequence:** {result['consequence']}")
        st.write(f"**Possible Trigger:** {result['possible_trigger']}")
        st.write(f"**Suggested Follow-up Question:** {result['suggested_follow_up_question']}")

st.divider()

st.caption(
    "Disclaimer: This project is for educational and caregiver-support purposes only. "
    "It is not medical advice, diagnosis, treatment, or clinical decision-making."
)
