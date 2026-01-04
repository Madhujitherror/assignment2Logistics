def classify_intent(message: str) -> str:
    message = message.lower()

    if "cancel" in message:
        return "CANCEL_ORDER"
    if "status" in message or "where" in message:
        return "ORDER_STATUS"

    return "UNKNOWN"
