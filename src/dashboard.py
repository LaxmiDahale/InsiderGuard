import streamlit as st

import pandas as pd


st.set_page_config(
    page_title="InsiderGuard",
    layout="wide"
)


st.title(
    "🛡️ InsiderGuard Security Dashboard"
)


df = pd.read_csv(
    "data/alerts.csv"
)


# Metrics

total_events = len(df)

suspicious_events = len(
    df[
        df["status"]
        == "Suspicious"
    ]
)

critical_events = len(
    df[
        df["severity"]
        == "Critical"
    ]
)


col1, col2, col3 = st.columns(3)


col1.metric(
    "Total Events",
    total_events
)


col2.metric(
    "Suspicious Events",
    suspicious_events
)


col3.metric(
    "Critical Alerts",
    critical_events
)


st.subheader(
    "Security Alerts"
)


alerts = df[
    df["severity"].isin(
        ["High", "Critical"]
    )
]


st.dataframe(
    alerts
)


st.subheader("Risk Score Distribution")

risk_distribution = (
    df["risk_score"]
    .value_counts()
    .sort_index()
)

st.bar_chart(risk_distribution)
