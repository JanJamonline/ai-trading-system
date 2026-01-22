import sys
import os

# ------------------------------------------------------------------
# ENSURE PROJECT ROOT IS IN PYTHON PATH
# ------------------------------------------------------------------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# ------------------------------------------------------------------
# NORMAL IMPORTS (NOW SAFE)
# ------------------------------------------------------------------
import streamlit as st
from multi_symbol_engine import generate_signals_multi

# ------------------------------------------------------------------
# STREAMLIT UI
# ------------------------------------------------------------------
st.set_page_config(
    page_title="AI Trading System — PRIMARY SIGNAL VIEW",
    layout="wide"
)

st.title("AI Trading System — PRIMARY SIGNAL VIEW")
st.caption("Read-only decision intelligence • No auto trading")

symbols = st.text_input(
    "Enter symbols (comma separated)",
    "TATASTEEL"
)

if st.button("Generate Signals"):
    symbols_list = [s.strip().upper() for s in symbols.split(",")]

    df = generate_signals_multi(symbols_list)

    latest = df.iloc[-1]

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("PRIMARY SIGNAL", latest["primary_trade_signal"])
    col2.metric("CONFIDENCE", latest["quality"])
    col3.metric("RISK", latest["risk_label"])
    col4.metric("ACTION", latestToggle := latest["primary_trade_signal"])

    st.divider()
    st.subheader("Signal Breakdown (Review Only)")
    st.dataframe(df, use_container_width=True)
