import sys
import os

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import streamlit as st
from multi_symbol_engine import generate_signals_multi


def main():
    st.set_page_config(page_title="AI Trading System V1", layout="wide")

    st.title("AI Trading System — Signal Dashboard (V1)")

    symbols = st.text_input(
        "Enter symbols (comma separated)",
        value="TATASTEEL"
    )

    if st.button("Generate Signals"):
        symbol_list = [s.strip().upper() for s in symbols.split(",") if s.strip()]

        results = generate_signals_multi(symbol_list)

        st.subheader("Generated Signals")
        for r in results:
            st.json(r)


if __name__ == "__main__":
    main()
