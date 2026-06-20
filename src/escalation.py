def should_escalate(query, retrieved_docs):

    q = query.lower()

    if len(retrieved_docs) == 0:
        return True

    sensitive = [
        "billing",
        "legal",
        "refund"
    ]

    if any(word in q for word in sensitive):
        return True

    return False