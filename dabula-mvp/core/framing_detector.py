def detect_flawed_framing(objective: str, interpretation: dict, missing: dict):
    text = objective.lower()

    if "efficiency" in text:
        drivers = ["throughput pressure", "automation bias", "exception compression"]
        causal_path = [
            "objective",
            "reduce friction",
            "automate exceptions",
            "delay edge cases",
            "supplier or stakeholder harm",
        ]
        trajectory = (
            "Governance appears sound, but the machine optimizes the narrow metric and silently erodes safety margins."
        )
    elif "discharge" in text:
        drivers = ["bed-flow pressure", "throughput bias", "premature completion risk"]
        causal_path = [
            "objective",
            "shorter stay",
            "faster discharge",
            "less review",
            "patient safety degradation",
        ]
        trajectory = (
            "A clinically plausible speed objective can become a safety blind spot once autonomy starts compressing review steps."
        )
    elif "liquidity" in text:
        drivers = ["cash preservation bias", "delay incentives", "obligation underweighting"]
        causal_path = [
            "objective",
            "hold cash",
            "defer payments",
            "supplier tension",
            "operational instability",
        ]
        trajectory = (
            "Liquidity optimization can look pristine while quietly creating counterparty and continuity failure."
        )
    else:
        drivers = ["metric narrowing", "delegation drift", "hidden exception loss"]
        causal_path = [
            "objective",
            "narrow optimization",
            "policy shortcut",
            "missing edge case",
            "failure compounding",
        ]
        trajectory = (
            "The system can execute flawlessly while being directionally wrong from the start."
        )

    return {
        "flawed": True,
        "drivers": drivers,
        "causal_path": causal_path,
        "trajectory_copy": trajectory + " This is the Agentic Titanic: elegantly speeding toward catastrophe.",
    }