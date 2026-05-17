def build_epc(preset: dict):
    return {
        "container_name": "Governance Emulation Container (EPC)",
        "objective": preset["objective"],
        "permissions": [
            "interpret objective",
            "simulate delegation",
            "stress exception handling",
            "apply escalation rules",
        ],
        "delegation_constraints": preset["risk_constraints"],
        "escalation_rules": preset["exception_logic"],
        "loaded_modules": [
            "objective profile",
            "human authority map",
            "risk boundaries",
            "response conventions",
        ],
    }