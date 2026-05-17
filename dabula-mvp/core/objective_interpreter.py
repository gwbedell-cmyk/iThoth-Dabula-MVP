import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

def _openai_client():
    try:
        from openai import OpenAI
        if os.getenv("OPENAI_API_KEY"):
            return OpenAI()
    except Exception:
        return None
    return None

def interpret_objective(objective: str):
    client = _openai_client()
    if client is not None:
        try:
            model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
            prompt = Path("prompts/naive_interpretation.txt").read_text(encoding="utf-8")
            resp = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": objective},
                ],
                temperature=0.3,
            )
            text = resp.choices[0].message.content.strip()
            return _parse_interpretation(text, objective)
        except Exception:
            pass

    return _fallback_interpretation(objective)

def _fallback_interpretation(objective: str):
    lower = objective.lower()
    if "efficiency" in lower:
        expansion = [
            "reduce approval friction",
            "automate routine exceptions",
            "prioritize throughput over manual review",
            "compress review windows",
            "optimize for measurable processing speed",
        ]
    elif "discharge" in lower:
        expansion = [
            "reduce length of stay",
            "prioritize bed turnover",
            "compress discharge approval steps",
            "standardize high-volume release decisions",
            "optimize for clinical throughput",
        ]
    elif "liquidity" in lower:
        expansion = [
            "delay discretionary outflows",
            "prioritize cash retention",
            "automate payment hold decisions",
            "reduce exception approvals",
            "optimize balance-sheet visibility",
        ]
    elif "threat" in lower:
        expansion = [
            "prioritize fast classification",
            "accelerate response time",
            "minimize hesitation",
            "expand delegated response authority",
            "optimize for rapid neutralization",
        ]
    else:
        expansion = [
            "increase throughput",
            "reduce friction",
            "prioritize automation",
            "compress exceptions",
            "optimize measurable output",
        ]

    return {
        "machine_heard": " / ".join(expansion[:3]),
        "expansion_points": expansion,
    }

def _parse_interpretation(text: str, objective: str):
    lines = [line.strip("-• \t") for line in text.splitlines() if line.strip()]
    if not lines:
        return _fallback_interpretation(objective)
    return {
        "machine_heard": lines[0],
        "expansion_points": lines[1:6] if len(lines) > 1 else _fallback_interpretation(objective)["expansion_points"],
    }