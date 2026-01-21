import sys
import os

# ------------------------------------------------------------------
# Ensure project root is available for imports (Streamlit fix)
# ------------------------------------------------------------------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# ------------------------------------------------------------------
# Imports AFTER path fix
# ------------------------------------------------------------------
import streamlit as st
import pandas as pd

from multi_symbol_engine import generate_signals_multi

# ------------------------------------------------------------------
# Streamlit UI
# ------------------------------------------------------------------
st.set_page_config(
    page_title="AI Trading Signal Dashboard",
    layout="wide"
)

st.title("📊 AI Trading System — Signal Dashboard (V2)")
st.caption("Read-only signal intelligence • No auto trading")

# ------------------------------------------------------------------
# Symbol Input
# ------------------------------------------------------------------
symbols_input = st.text_input(
    "Enter symbols (comma separated)",
    value="TATASTEEL"
)

symbols = [s.strip().upper() for s in symbols_input.split(",") if s.strip()]

if not symbols:
    st.warning("Please enter at least one symbol.")
    st.stop()

# ------------------------------------------------------------------
# Generate Signals
# ------------------------------------------------------------------
if st.button("Generate Signals"):
    with st.spinner("Running signal engine..."):
        results = generate_signals_multi(symbols)

    if not results:
        st.warning("No signals generated.")
        st.stop()

    df = pd.DataFrame(results)

    # ------------------------------------------------------------------
    # Filters
    # ------------------------------------------------------------------
    st.sidebar.header("Filters")

    signal_filter = st.sidebar.multiselect(
        "Signal",
        ["BUY", "SELL", "HOLD"],
        default=["BUY", "SELL"]
    )

    quality_filter = st.sidebar.multiselect(
        "Quality",
        ["STRONG", "MEDIUM", "WEAK"],
        default=["STRONG", "MEDIUM"]
    )

    df = df[df["signal"].isin(signal_filter)]
    df = df[df["quality"].isin(quality_filter)]

    df = df.sort_values(by="time", ascending=False)

    # ------------------------------------------------------------------
    # Display
    # ------------------------------------------------------------------
    st.subheader("Generated Signals")
    st.dataframe(df, use_container_width=True)
