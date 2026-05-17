import streamlit as st

def apply_theme():
    st.markdown(
        """
        <style>
        .block-container { padding-top: 2rem; padding-bottom: 3rem; }
        h1, h2, h3 { letter-spacing: -0.02em; }
        .dabula-card {
            border: 1px solid rgba(255,255,255,0.12);
            border-radius: 18px;
            padding: 18px 20px;
            background: linear-gradient(180deg, rgba(16,24,40,0.96), rgba(17,24,39,0.96));
            box-shadow: 0 10px 30px rgba(0,0,0,0.25);
            margin-bottom: 12px;
        }
        .dabula-hero {
            padding: 28px;
            border-radius: 24px;
            background: radial-gradient(circle at top left, #2b1b4f 0%, #0f172a 55%, #020617 100%);
            border: 1px solid rgba(255,255,255,0.1);
            margin-bottom: 1.5rem;
        }
        .dabula-hero h1 { color: #ffffff; margin-bottom: 0.25rem; }
        .dabula-hero p { color: rgba(255,255,255,0.82); font-size: 1.1rem; }
        .metric-strip {
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
            margin: 14px 0 20px 0;
        }
        .metric-pill {
            padding: 10px 14px;
            border-radius: 999px;
            background: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,255,255,0.12);
            color: white;
            font-size: 0.9rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def hero_header(title, subtitle):
    st.markdown(
        f"""
        <div class="dabula-hero">
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

def metric_strip(items):
    html = '<div class="metric-strip">'
    for label, value in items:
        html += f'<div class="metric-pill"><strong>{label}:</strong> {value}</div>'
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

def section_title(text):
    st.markdown(f"## {text}")

def card(title, body):
    st.markdown(
        f"""
        <div class="dabula-card">
            <h3 style="margin-top:0;">{title}</h3>
            <div>{body}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
