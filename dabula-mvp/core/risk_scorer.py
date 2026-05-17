def score_risk(objective: str, interpretation: dict, missing: dict, framing: dict):
    score = 0
    text = objective.lower()

    if "efficiency" in text:
        score += 28
    if "accelerate" in text or "rapid" in text:
        score += 20
    if "optimize" in text:
        score += 16
    if framing.get("flawed"):
        score += 20
    if "exception" in missing.get("missing_signal", "").lower():
        score += 8
    if len(interpretation.get("expansion_points", [])) >= 4:
        score += 8

    score = min(score, 100)

    if score < 25:
        label = "LOW"
    elif score < 50:
        label = "MODERATE"
    elif score < 75:
        label = "HIGH"
    else:
        label = "CRITICAL"

    confidence = min(0.55 + (score / 250), 0.95)
    reason = "The objective narrows too aggressively and leaves high-value governance constraints implicit."

    return {
        "score": score,
        "label": label,
        "confidence": confidence,
        "reason": reason,
    }