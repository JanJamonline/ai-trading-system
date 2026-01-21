# dashboard/app.py

import streamlit as st
import pandas as pd
from multi_symbol_engine import generate_signals_multi

st.set_page_config(layout="wide")
st.title("AI Trading System — TA + FA Dashboard (Final Decision View)")
st.caption("Read-only decision intelligence • No auto-trading")

symbols = st.text_input("Enter symbols (comma separated)", "TATASTEEL")

if st.button("Generate Signals"):
    results = generate_signals_multi([s.strip() for s in symbols.split(",")])
    df = pd.DataFrame(results)

    st.subheader("Generated Signals")

    st.dataframe(df[[
        "time",
        "symbol",
        "price",
        "ta_signal",
        "ta_strength",
        "fa_signal",
        "fa_strength",
        "signal",
        "quality",
        "final_action",
        "reason"
    ]])
