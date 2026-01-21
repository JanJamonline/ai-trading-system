import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from multi_symbol_engine import generate_signals_multi

st.title("AI Trading System — TA + FA Dashboard")

symbols_input = st.text_input("Enter symbols (comma separated)", "TATASTEEL")

if st.button("Generate Signals"):
    symbols = [s.strip() for s in symbols_input.split(",")]
    results = generate_signals_multi(symbols)

    df = pd.DataFrame(results)
    st.dataframe(df)
