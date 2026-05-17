import streamlit as st
from core.domain_templates import get_domain_templates
from ui.theme import section_title, card

st.set_page_config(page_title="Use Cases", layout="wide")

st.title("Use Cases")
st.caption("Dabula is designed to make meaning risk obvious before autonomy begins.")

templates = get_domain_templates()

section_title("Supported demo presets")
for name, data in templates.items():
    card(
        name,
        f"""
**Objective:** {data["objective"]}

**Why it matters:** {data["why_it_matters"]}
        """,
    )

section_title("How to present it")
st.markdown(
    """
- Start with the Agentic Titanic framing.
- Show a plausible enterprise objective.
- Reveal the machine interpretation.
- Surface hidden assumptions.
- Rewrite it into a governable objective.
- Run the governance penetration test.
- End with the structural failure report.
    """
)

section_title("Investor takeaway")
st.markdown(
    """
The product is not about flashy AI output.
It is about exposing the mismatch between intended meaning and executable meaning before autonomy amplifies the mistake.
    """
)