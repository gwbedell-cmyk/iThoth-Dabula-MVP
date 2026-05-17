# Dabula Meaning Engine™

## Meaning Verification + Governance Penetration Testing for Autonomous Systems

Dabula is an investor-demo MVP that shows why autonomous systems can fail even when they appear operationally correct: the objective was framed badly from the start.

The product is built around two demo experiences:

1. **Meaning Verification**
   - Convert a human objective into a plausible machine interpretation.
   - Surface the missing business priorities, risk constraints, ethical boundaries, exception logic, and human authority expectations.
   - Rewrite the objective into a governable version.

2. **Governance Penetration Testing**
   - Simulate a governance emulation container.
   - Stress-test the objective across multiple simulated model behaviors.
   - Fuse the attack traces into a twisted moiré structural analysis.
   - Produce a red-flag findings report.

## The point

The core message is simple:

> Meaning verification is mandatory before autonomy.

Dabula is not production infrastructure. It is persuasion architecture for investors, operators, and governance leaders.

## Run locally

### 1) Create an environment
```bash
python -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) Configure optional OpenAI access
Copy `.env.example` to `.env` and fill in your key if desired.

### 4) Launch the app
```bash
streamlit run app.py
```

## Notes

- The app runs fully with mocked logic if OpenAI is unavailable.
- No live Claude/Gemini integrations are required.
- The governance stress test is simulated for demo purposes.
- Visuals are rendered with Plotly.