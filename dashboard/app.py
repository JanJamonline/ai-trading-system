# dashboard/app.py

import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from multi_symbol_engine import generate_signals_multi

st.set_page_config(layout="wide")

st.title("AI Trading System — PRIMARY SIGNAL VIEW")
st.caption("Read-only decision intelligence • No auto trading")

symbols = st.text_input("Enter symbols (comma separated)", "TATASTEEL")

if st.button("Generate Signals"):
    symbols_list = [s.strip().upper() for s in symbols.split(",")]

    data = generate_signals_multi(symbols_list)
    df = pd.DataFrame(data)

    latest = df.iloc[-1]

    st.subheader("🎯 PRIMARY TRADE DECISION")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("PRIMARY SIGNAL", latest["primary_trade_signal"])
    col2.metric("CONFIDENCE", f'{latest["confidence"]}%')
    col3.metric("CONFIDENCE BUCKET", latest["confidence_bucket"])
    col4.metric("RISK", latest["risk_label"])

    st.divider()
    st.subheader("Signal Breakdown (Review Only)")
    st.dataframe(df, use_container_width=True)
