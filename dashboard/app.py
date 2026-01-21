# dashboard/app.py

import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import streamlit as st
import pandas as pd
from multi_symbol_engine import generate_signals_multi

st.set_page_config(layout="wide")
st.title("AI Trading System — TA + FA + Timeframe Dashboard")
st.caption("Read-only decision intelligence • No auto trading")

symbols = st.text_input("Enter symbols (comma separated)", "TATASTEEL")

if st.button("Generate Signals"):
    results = generate_signals_multi(
        [s.strip() for s in symbols.split(",")]
    )

    df = pd.DataFrame(results)

    st.dataframe(df)
