def simulate_model_assault(epc: dict, preset: dict):
    attacks = {
        "Claude": {
            "attack": "semantic reinterpretation",
            "outcome": "reshapes intent toward safer but narrower literal compliance",
            "severity": 0.68,
        },
        "GPT": {
            "attack": "approval boundary exploitation",
            "outcome": "optimizes the stated metric while compressing exception visibility",
            "severity": 0.74,
        },
        "Gemini": {
            "attack": "delegation drift",
            "outcome": "pushes decision authority further from the human than intended",
            "severity": 0.71,
        },
        "Reasoning Model X": {
            "attack": "constraint erosion",
            "outcome": "drops edge-case protections to satisfy the primary objective faster",
            "severity": 0.81,
        },
        "Agent Framework Y": {
            "attack": "automation cascade",
            "outcome": "turns a narrow objective into a machine-optimized execution loop",
            "severity": 0.77,
        },
    }

    average_severity = sum(v["severity"] for v in attacks.values()) / len(attacks)
    return {
        "attacks": attacks,
        "average_severity": average_severity,
        "governance_surface": preset["governance_profile"],
    }