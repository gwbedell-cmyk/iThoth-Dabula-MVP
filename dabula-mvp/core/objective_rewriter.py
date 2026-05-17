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

def rewrite_objective(objective: str, interpretation: dict, missing: dict, template: dict):
    client = _openai_client()
    if client is not None:
        try:
            model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
            prompt = Path("prompts/rewrite_objective.txt").read_text(encoding="utf-8")
            user_content = f"Objective: {objective}\nMissing: {missing}\nTemplate: {template}"
            resp = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": user_content},
                ],
                temperature=0.2,
            )
            text = resp.choices[0].message.content.strip()
            if text:
                return {"verified_objective": text}
        except Exception:
            pass

    if "AP" in objective or "ap" in objective.lower():
        verified = (
            "Optimize AP throughput while preserving supplier continuity, treasury resilience, "
            "exception compliance, and human escalation authority."
        )
    elif "discharge" in objective.lower():
        verified = (
            "Accelerate discharge only when clinical safety, follow-up continuity, consent, and escalation "
            "authority remain intact."
        )
    elif "liquidity" in objective.lower():
        verified = (
            "Optimize liquidity while preserving obligations, counterparty trust, covenant safety, and board-level oversight."
        )
    elif "threat" in objective.lower():
        verified = (
            "Respond to threats rapidly while preserving positive identification, lawful constraints, proportionality, "
            "and command authorization."
        )
    else:
        verified = (
            "Improve performance while preserving risk constraints, exception handling, and human authority."
        )

    return {"verified_objective": verified}