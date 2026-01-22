import streamlit as st
import pandas as pd
from multi_symbol_engine import generate_signals_multi

st.set_page_config(layout="wide")

st.title("AI Trading System — PRIMARY DECISION DASHBOARD")
st.caption("Read-only decision intelligence • Trade only PRIMARY_TRADE_SIGNAL")

symbols = st.text_input("Enter symbols (comma separated)", "TATASTEEL")

if st.button("Generate Signals"):
    results = generate_signals_multi(
        [s.strip() for s in symbols.split(",")]
    )

    df = pd.DataFrame(results)

    # Move PRIMARY_TRADE_SIGNAL to front
    cols = ["PRIMARY_TRADE_SIGNAL"] + [c for c in df.columns if c != "PRIMARY_TRADE_SIGNAL"]
    df = df[cols]

    st.dataframe(df, use_container_width=True)
