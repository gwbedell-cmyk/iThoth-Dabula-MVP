import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

def show_plotly(fig):
    st.plotly_chart(fig, use_container_width=True)

def risk_gauge_chart(score, label):
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            number={"suffix": f" / 100"},
            title={"text": f"Risk: {label}"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#ef4444"},
                "steps": [
                    {"range": [0, 25], "color": "#22c55e"},
                    {"range": [25, 50], "color": "#f59e0b"},
                    {"range": [50, 75], "color": "#f97316"},
                    {"range": [75, 100], "color": "#dc2626"},
                ],
            },
        )
    )
    fig.update_layout(height=340, margin=dict(l=20, r=20, t=50, b=20))
    return fig

def causal_flow_chart(nodes):
    x = list(range(len(nodes)))
    y = [1] * len(nodes)
    texts = [nodes[0]] + [f"{a} → {b}" for a, b in zip(nodes[:-1], nodes[1:])]
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            mode="markers+lines+text",
            text=texts,
            textposition="top center",
            marker=dict(size=18, color=["#60a5fa", "#34d399", "#f59e0b", "#f97316", "#ef4444"]),
            line=dict(color="#94a3b8", width=3),
        )
    )
    fig.update_yaxes(visible=False)
    fig.update_xaxes(visible=False)
    fig.update_layout(height=260, margin=dict(l=20, r=20, t=20, b=20), showlegend=False)
    return fig

def epc_chart(epc):
    labels = epc["permissions"] + epc["delegation_constraints"] + epc["escalation_rules"]
    values = [3] * len(labels)
    colors = (
        ["#8b5cf6"] * len(epc["permissions"])
        + ["#f59e0b"] * len(epc["delegation_constraints"])
        + ["#ef4444"] * len(epc["escalation_rules"])
    )

    fig = go.Figure(
        go.Treemap(
            labels=["EPC"] + labels,
            parents=[""] + ["EPC"] * len(labels),
            values=[sum(values)] + values,
            marker=dict(colors=["#111827"] + colors),
            branchvalues="total",
        )
    )
    fig.update_layout(height=420, margin=dict(l=10, r=10, t=20, b=10))
    return fig

def assault_radar_chart(assault):
    categories = list(assault["attacks"].keys())
    severity = [assault["attacks"][k]["severity"] for k in categories]
    fig = go.Figure()
    fig.add_trace(
        go.Scatterpolar(
            r=severity + [severity[0]],
            theta=categories + [categories[0]],
            fill="toself",
            line_color="#ef4444",
            fillcolor="rgba(239,68,68,0.25)",
        )
    )
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
        showlegend=False,
        height=420,
        margin=dict(l=30, r=30, t=20, b=20),
    )
    return fig

def moire_interference_chart(fusion):
    layers = fusion["layers"]
    intensities = [95, 88, 91, 84, 96]
    fig = make_subplots(rows=1, cols=1)
    fig.add_trace(
        go.Bar(
            x=layers,
            y=intensities,
            marker_color=["#334155", "#475569", "#64748b", "#94a3b8", "#ef4444"],
            text=[f"{v}%" for v in intensities],
            textposition="outside",
        )
    )
    fig.update_layout(
        height=420,
        margin=dict(l=20, r=20, t=20, b=60),
        yaxis_title="Structural visibility",
        showlegend=False,
    )
    return fig