import streamlit as st
from ui.theme import apply_theme, hero_header, metric_strip, section_title, card
from core.domain_templates import get_domain_templates
from core.report_generator import build_quick_summary

st.set_page_config(
    page_title="Dabula Meaning Engine™",
    page_icon="⚓",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_theme()

st.sidebar.title("Dabula Meaning Engine™")
st.sidebar.caption("Meaning Verification + Governance Penetration Testing")
st.sidebar.markdown("---")

templates = get_domain_templates()
domain_choice = st.sidebar.selectbox(
    "Demo preset",
    list(templates.keys()),
    index=0,
)

st.sidebar.info(
    "This MVP simulates governance penetration testing. It does not call live Claude/Gemini APIs."
)

hero_header(
    "THE AGENTIC TITANIC",
    "Governance built on flawed meaning is elegantly speeding toward catastrophe."
)

left, right = st.columns([1.25, 1])

with left:
    section_title("What Dabula does")
    st.markdown(
        """
Dabula verifies what a human actually meant before autonomous action begins.
It exposes the gap between a plausible machine interpretation and the governable objective the organization truly intended.
        """
    )

    metric_strip(
        [
            ("Meaning risk", "High signal"),
            ("Governance", "Stress-tested"),
            ("Autonomy", "Only after verification"),
        ]
    )

    st.markdown("---")
    st.subheader("Two demo experiences")
    st.markdown(
        """
1. **Meaning Verification** — reveals flawed meaning framing and rewrites the objective.
2. **Governance Penetration Testing** — simulates EPC creation, multi-model assault, twisted moiré fusion, and structural findings.
        """
    )

with right:
    section_title("Investor narrative")
    card(
        "Why this matters",
        """
Autonomous systems often fail not because they lack capability, but because the human objective was incomplete, ambiguous, or dangerously over-optimized.
Dabula makes that failure mode visceral in under two minutes.
        """,
    )
    card(
        "Core message",
        """
If meaning is wrong, governance is theater.
Dabula turns that abstract risk into a visible operational story.
        """,
    )

st.markdown("---")
section_title("Selected preset")
summary = build_quick_summary(templates[domain_choice])
st.json(summary)

st.markdown(
    """
### Navigation
Use the left sidebar or the page menu to move through:
- Meaning Verification
- Governance Penetration Testing
- Use Cases
- Methodology
    """
)
