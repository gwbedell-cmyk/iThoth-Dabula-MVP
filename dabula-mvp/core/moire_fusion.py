def fuse_moire_traces(epc: dict, assault: dict):
    avg = assault["average_severity"]
    structural_tension = "HIGH" if avg > 0.72 else "MODERATE"
    interference_score = min(100, round(avg * 100 + 12))
    return {
        "structural_tension": structural_tension,
        "interference_score": interference_score,
        "layers": [
            "semantic ambiguity",
            "delegation escalation",
            "objective reinterpretation",
            "human override inconsistency",
            "hidden governance blind spots",
        ],
    }