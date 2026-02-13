def check_escalation(intent: str, extracted: dict):

    if intent == "Emergency":
        return True

    if extracted.get("urgency") == "high":
        return True

    return False
