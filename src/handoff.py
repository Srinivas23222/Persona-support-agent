def generate_summary(
    persona,
    query,
    docs
):

    return {
        "persona": persona,
        "issue": query,
        "documents_used": [
            d.metadata.get("source", "")
            for d in docs
        ],
        "recommendation":
            "Human support required"
    }