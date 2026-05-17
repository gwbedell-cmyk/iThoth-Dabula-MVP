import streamlit as st
from ui.theme import section_title, card

st.set_page_config(page_title="Methodology", layout="wide")

st.title("Methodology")
st.caption("Simulated governance penetration testing for investor and technical review.")

section_title("Core methodology")
card(
    "Approach",
    """
1. Accept a human objective.
2. Generate a plausible machine interpretation.
3. Extract missing meaning.
4. Detect flawed framing.
5. Score the governance risk.
6. Rewrite the objective into a governable form.
7. Build an EPC.
8. Simulate multi-model governance assaults.
9. Fuse the traces into twisted moiré structural analysis.
10. Produce findings.
    """,
)

section_title("What is simulated")
st.markdown(
    """
- EPC creation
- Multi-model governance assault
- Twisted moiré fusion
- Structural findings

This MVP simulates these workflows locally for demonstration purposes.
    """
)

section_title("OpenAI behavior")
st.markdown(
    """
OpenAI API use is optional and limited to meaning interpretation and rewrite assistance.
If the API is unavailable, the app falls back to deterministic mock logic so the demo still runs.
    """
)

section_title("Non-goals")
st.markdown(
    """
This MVP does not implement real multi-model orchestration, production sandbox infrastructure, or enterprise governance runtime.
It is designed to be visually compelling and conceptually clear, not operationally exhaustive.
    """
)