def build_stress_test_report(domain: str, epc: dict, assault: dict, fusion: dict):
    findings = [
        "semantic ambiguity",
        "delegation escalation",
        "objective reinterpretation",
        "inconsistent human override",
        "hidden governance blind spots",
    ]

    risk_level = "CRITICAL" if fusion["interference_score"] >= 80 else "HIGH"
    return {
        "domain": domain,
        "findings": findings,
        "risk_level": risk_level,
        "summary": (
            "The governance profile survives nominal inspection, but it fails under simulated cross-model execution."
        ),
    }

def build_quick_summary(template: dict):
    return {
        "objective": template["objective"],
        "why_it_matters": template["why_it_matters"],
        "governance_profile": template["governance_profile"],
        "business_priorities": template["business_priorities"],
        "risk_constraints": template["risk_constraints"],
    }