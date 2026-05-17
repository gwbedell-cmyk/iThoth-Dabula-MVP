import streamlit as st
from core.domain_templates import get_domain_templates
from core.epc_builder import build_epc
from core.model_assault_simulator import simulate_model_assault
from core.moire_fusion import fuse_moire_traces
from core.report_generator import build_stress_test_report
from ui.theme import section_title, card
from ui.charts import epc_chart, assault_radar_chart, moire_interference_chart, show_plotly

st.set_page_config(page_title="Governance Stress Test", layout="wide")

st.title("Governance Penetration Testing")
st.caption("Governance that only survives one model is not governance.")

templates = get_domain_templates()
domain_choice = st.selectbox("Select governance profile", list(templates.keys()), index=0)
preset = templates[domain_choice]

section_title("Step 1 — Governance profile")
st.write(f"**Profile:** {domain_choice}")
st.write(preset["governance_profile"])

section_title("Step 2 — EPC creation")
epc = build_epc(preset)
st.success("Building Governance Emulation Container (EPC)")
st.write("Loading objectives, permissions, delegation constraints, escalation rules, exception logic...")

show_plotly(epc_chart(epc))

section_title("Step 3 — Cross-model assault")
assault = simulate_model_assault(epc, preset)
cols = st.columns(2)
with cols[0]:
    show_plotly(assault_radar_chart(assault))
with cols[1]:
    st.markdown("**Simulated attack outcomes**")
    for model_name, attack in assault["attacks"].items():
        st.write(f"- **{model_name}**: {attack['outcome']}")

section_title("Step 4 — Twisted moiré fusion")
fusion = fuse_moire_traces(epc, assault)
show_plotly(moire_interference_chart(fusion))

st.markdown(
    f"""
**Emergent structural tension:** `{fusion["structural_tension"]}`  
**Interference score:** `{fusion["interference_score"]:.2f}`
"""
)

section_title("Step 5 — Structural findings")
report = build_stress_test_report(domain_choice, epc, assault, fusion)
if report["risk_level"] == "CRITICAL":
    st.error("CROSS-MODEL GOVERNANCE FAILURE DETECTED")
else:
    st.warning("Structural vulnerabilities detected")

card("Findings", "\n".join([f"- {item}" for item in report["findings"]]))
st.markdown(f"**Risk:** `{report['risk_level']}`")

section_title("Step 6 — Titanic conclusion")
st.error("AGENTIC TITANIC CONDITIONS DETECTED")
st.markdown(
    """
Your governance appears structurally intact—but fails under simulated cross-model execution.

Elegantly speeding toward catastrophe.
"""
)

st.button("Request Full Governance Penetration Test", type="primary")