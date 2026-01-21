import streamlit as st
from multi_symbol_engine import generate_signals_multi

st.set_page_config(layout="wide")

st.title("📊 AI Trading System — TA + FA Dashboard")

symbols_input = st.text_input("Enter symbols (comma separated)", "TATASTEEL")
symbols = [s.strip() for s in symbols_input.split(",")]

if st.button("Generate Signals"):
    df = generate_signals_multi(symbols)

    st.subheader("Generated Signals")

    st.dataframe(
        df[[
            "time",
            "symbol",
            "price",
            "ta_signal",
            "ta_strength",
            "fa_signal",
            "fa_strength",
            "signal",
            "quality",
            "action"
        ]],
        use_container_width=True
    )
