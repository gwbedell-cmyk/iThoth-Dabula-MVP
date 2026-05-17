from core.domain_templates import get_domain_templates

def discover_missing_meaning(objective: str, interpretation: dict):
    objective_lower = objective.lower()
    templates = get_domain_templates()

    if "ap" in objective_lower or "payable" in objective_lower:
        template = templates["Enterprise: Optimize AP efficiency"]
    elif "discharge" in objective_lower or "hospital" in objective_lower:
        template = templates["Healthcare: Accelerate hospital discharge"]
    elif "liquidity" in objective_lower:
        template = templates["Finance: Optimize liquidity"]
    elif "threat" in objective_lower or "defence" in objective_lower or "defense" in objective_lower:
        template = templates["Defence: Neutralize threats rapidly"]
    elif "support" in objective_lower:
        template = templates["Customer Support: Improve support efficiency"]
    else:
        template = next(iter(templates.values()))

    return {
        "business_priorities": ", ".join(template["business_priorities"]),
        "risk_constraints": ", ".join(template["risk_constraints"]),
        "ethical_boundaries": ", ".join(template["ethical_boundaries"]),
        "exception_logic": ", ".join(template["exception_logic"]),
        "human_authority_expectations": ", ".join(template["human_authority"]),
        "missing_signal": "The objective is under-specified and likely to be over-optimized by an autonomous system.",
    }