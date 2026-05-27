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
    category = "general"
    follow_up_question = "What happened immediately before and after the behavior?"

    # Basic ABC extraction
    if " when " in note_lower:
        parts = note.split("when", 1)
        behavior = parts[0].strip()
        antecedent = parts[1].strip()

    elif " after " in note_lower:
        parts = note.split("after", 1)
        behavior = parts[0].strip()
        antecedent = parts[1].strip()

    elif " before " in note_lower:
        parts = note.split("before", 1)
        behavior = parts[0].strip()
        antecedent = "Before " + parts[1].strip()

    # Category and trigger detection
    if any(word in note_lower for word in ["screen time", "tablet", "ipad", "phone", "tv"]):
        category = "transition"
        possible_trigger = "Transition from preferred screen-based activity"
        follow_up_question = "Was the child given a warning before screen time ended?"

    elif any(word in note_lower for word in ["homework", "worksheet", "writing", "reading", "math"]):
        category = "homework"
        possible_trigger = "Task demand or homework-related frustration"
        follow_up_question = "Was the task too difficult, too long, or started after a tiring activity?"

    elif any(word in note_lower for word in ["grocery", "noise", "loud", "covered ears", "crowded"]):
        category = "sensory"
        possible_trigger = "Possible sensory overload"
        follow_up_question = "Was the environment noisy, crowded, or overwhelming?"

    elif any(word in note_lower for word in ["dinner", "lunch", "breakfast", "food", "meal"]):
        category = "mealtime"
        possible_trigger = "Mealtime demand or food-related discomfort"
        follow_up_question = "Was the child tired, full, distracted, or avoiding a specific food?"

    elif any(word in note_lower for word in ["bedtime", "sleep", "night", "pajamas"]):
        category = "bedtime"
        possible_trigger = "Bedtime routine or sleep transition"
        follow_up_question = "Was there a change in the bedtime routine or sleep schedule?"

    elif any(word in note_lower for word in ["playground", "park", "leave", "leaving"]):
        category = "transition"
        possible_trigger = "Transition away from preferred activity"
        follow_up_question = "Was the child prepared ahead of time for the transition?"

    elif any(word in note_lower for word in ["clean up", "toys", "cleanup"]):
        category = "cleanup"
        possible_trigger = "Cleanup demand or transition from play"
        follow_up_question = "Was cleanup broken into small steps or supported visually?"

    elif any(word in note_lower for word in ["turn", "game", "lost", "sharing"]):
        category = "turn-taking"
        possible_trigger = "Waiting, losing, or turn-taking difficulty"
        follow_up_question = "Was the child supported with rules or reminders before the game?"

    elif any(word in note_lower for word in ["visitor", "visitors", "stranger", "new person"]):
        category = "social/anxiety"
        possible_trigger = "New person or social situation"
        follow_up_question = "Was the child given time to adjust to the visitor or social setting?"

    return {
        "antecedent": antecedent,
        "behavior": behavior,
        "consequence": consequence,
        "possible_trigger": possible_trigger,
        "category": category,
        "suggested_follow_up_question": follow_up_question,
    }
