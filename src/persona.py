def detect_persona(query):

    q = query.lower()

    if any(word in q for word in [
        "api",
        "token",
        "configuration",
        "logs",
        "endpoint"
    ]):
        return "Technical Expert"

    elif any(word in q for word in [
        "frustrated",
        "angry",
        "nothing works",
        "urgent",
        "terrible"
    ]):
        return "Frustrated User"

    elif any(word in q for word in [
        "business",
        "impact",
        "operations",
        "revenue",
        "management"
    ]):
        return "Business Executive"

    return "Business Executive"