import streamlit as st

from src.persona import detect_persona
from src.rag import load_vector_store
from src.escalation import should_escalate
from src.handoff import generate_summary

st.title(
    "Persona-Aware Support Agent"
)

db = load_vector_store()

query = st.text_input(
    "Enter your issue"
)

if query:

    persona = detect_persona(query)

    docs = db.similarity_search(
        query,
        k=3
    )

    context = "\n".join(
        [d.page_content for d in docs]
    )

    if persona == "Technical Expert":

        response = f"""
Technical Analysis

{context}
"""

    elif persona == "Frustrated User":

        response = f"""
I understand your frustration.

Here is what may help:

{context}
"""

    else:

        response = f"""
Business Summary

{context}
"""

    escalated = should_escalate(
        query,
        docs
    )

    st.write(
        "Persona:",
        persona
    )

    st.write(
        "Response:",
        response
    )

    st.write(
        "Escalated:",
        escalated
    )

    if escalated:

        summary = generate_summary(
            persona,
            query,
            docs
        )

        st.json(summary)