import sys
import os

# --------------------------------------------------
# FIX PYTHON IMPORT ROOT (DO NOT REMOVE)
# --------------------------------------------------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
# --------------------------------------------------

import streamlit as st
import pandas as pd

from multi_symbol_engine import generate_signals_multi

st.set_page_config(page_title="AI Trading System — PRIMARY SIGNAL VIEW", layout="wide")

st.title("AI Trading System — PRIMARY SIGNAL VIEW")
st.caption("Read-only decision intelligence • No auto trading")

symbols_input = st.text_input(
    "Enter symbols (comma separated)",
    value="TATASTEEL"
)

if st.button("Generate Signals"):
    symbols_list = [s.strip().upper() for s in symbols_input.split(",") if s.strip()]

    if not symbols_list:
        st.warning("Please enter at least one symbol.")
    else:
        with st.spinner("Generating signals..."):
            results = generate_signals_multi(symbols_list)
            df = pd.DataFrame(results)

        if df.empty:
            st.error("No data returned.")
        else:
            latest = df.iloc[-1]

            st.subheader("🎯 PRIMARY TRADE DECISION")

            col1, col2, col3, col4 = st.columns(4)
            col1.metric("PRIMARY SIGNAL", latest["primary_trade_signal"])
            col2.metric("CONFIDENCE", f"{latest['confidence_score']}%")
            col3.metric("RISK", latest["risk_label"])
            col4.metric("ACTION", latest["signal"])

            st.divider()
            st.subheader("Signal Breakdown (Review Only)")
            st.dataframe(df, use_container_width=True)
