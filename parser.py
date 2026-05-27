def parse_behavior_note(note: str) -> dict:
    """
    Simple educational ABC parser.
    This is rule-based and intended only for caregiver-support examples.
    """

    note_lower = note.lower()

    antecedent = "Not clearly mentioned"
    behavior = "Not clearly mentioned"
    consequence = "Not clearly mentioned"
    possible_trigger = "Not clearly identified"
    follow_up_question = "What happened immediately before and after the behavior?"

    if "when" in note_lower:
        parts = note.split("when", 1)
        behavior = parts[0].strip()
        antecedent = parts[1].strip()

    if "after" in note_lower:
        parts = note.split("after", 1)
        behavior = parts[0].strip()
        antecedent = parts[1].strip()

    if "screen time" in note_lower or "tablet" in note_lower or "ipad" in note_lower:
        possible_trigger = "Transition from preferred screen-based activity"
        follow_up_question = "Was the child given a warning before screen time ended?"

    elif "homework" in note_lower or "worksheet" in note_lower or "writing" in note_lower:
        possible_trigger = "Task demand or homework-related frustration"
        follow_up_question = "Was the task too difficult, too long, or started after a tiring activity?"

    elif "grocery" in note_lower or "noise" in note_lower or "covered ears" in note_lower:
        possible_trigger = "Possible sensory overload"
        follow_up_question = "Was the environment noisy, crowded, or overwhelming?"

    return {
        "antecedent": antecedent,
        "behavior": behavior,
        "consequence": consequence,
        "possible_trigger": possible_trigger,
        "suggested_follow_up_question": follow_up_question,
    }
