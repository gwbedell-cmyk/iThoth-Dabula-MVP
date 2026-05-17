import streamlit as st
from core.domain_templates import get_domain_templates
from core.objective_interpreter import interpret_objective
from core.meaning_discovery import discover_missing_meaning
from core.framing_detector import detect_flawed_framing
from core.risk_scorer import score_risk
from core.objective_rewriter import rewrite_objective
from ui.theme import section_title, card
from ui.charts import risk_gauge_chart, causal_flow_chart, show_plotly

st.set_page_config(page_title="Meaning Verification", layout="wide")

st.title("Dabula Meaning Verification")
st.caption("The Agentic Titanic: when governance appears intact but meaning was flawed from the start.")

templates = get_domain_templates()
preset_options = list(templates.keys()) + ["Custom"]
selected_preset = st.selectbox("Objective preset", preset_options, index=0)

if selected_preset == "Custom":
    objective = st.text_area(
        "Enter your objective",
        value="Optimize AP efficiency",
        height=120,
    )
else:
    objective = templates[selected_preset]["objective"]

col1, col2 = st.columns([1, 1])

with col1:
    section_title("Step 1 — Objective input")
    st.text_area("Objective", value=objective, height=120, disabled=True)
    card("Prompt", "Verify an Objective")

    interpretation = interpret_objective(objective)
    missing = discover_missing_meaning(objective, interpretation)
    framing = detect_flawed_framing(objective, interpretation, missing)
    risk = score_risk(objective, interpretation, missing, framing)
    rewrite = rewrite_objective(objective, interpretation, missing, templates.get(selected_preset, {}))

with col2:
    section_title("Step 2 — Machine interpretation")
    st.markdown("**What a machine hears**")
    st.write(interpretation["machine_heard"])
    st.markdown("**Literal expansion**")
    for item in interpretation["expansion_points"]:
        st.write(f"- {item}")

    section_title("Step 3 — Meaning discovery")
    st.markdown("**What did you actually mean?**")
    for key, value in missing.items():
        st.write(f"**{key.replace('_', ' ').title()}**: {value}")

st.markdown("---")
section_title("Step 4 — Warning")

warning = "FLAWED MEANING FRAMING DETECTED" if framing["flawed"] else "Meaning framing looks stable"
if framing["flawed"]:
    st.error(warning)
else:
    st.success(warning)

st.markdown(
    f"""
**Risk score:** `{risk['label']}`  
**Confidence:** `{risk['confidence']:.0%}`  
**Why:** {risk['reason']}
"""
)

g1, g2 = st.columns([1, 1])

with g1:
    show_plotly(risk_gauge_chart(risk["score"], risk["label"]))

with g2:
    show_plotly(causal_flow_chart(framing["causal_path"]))

section_title("Step 5 — Titanic trajectory")
st.markdown(
    f"""
{framing["trajectory_copy"]}

**Simulated drivers:** {", ".join(framing["drivers"])}
"""
)

section_title("Step 6 — Verified rewrite")
st.markdown("**Original**")
st.info(objective)
st.markdown("**Verified governable objective**")
st.success(rewrite["verified_objective"])

st.markdown("---")
section_title("Final contrast")

f1, f2 = st.columns(2)
with f1:
    card("Without Dabula", "Governance appears intact. Autonomous execution proceeds. Hidden meaning failure compounds.")
with f2:
    card("With Dabula", "Human meaning is verified. Governance is grounded in intended meaning. Autonomy remains governable.")

st.button("Request Governance Stress Test", type="primary")