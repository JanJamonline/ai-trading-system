import sys
import os
import streamlit as st
import pandas as pd

# -------------------------------------------------------
# Ensure project root is in PYTHONPATH (SAFE)
# -------------------------------------------------------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from multi_symbol_engine import generate_signals_multi

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------
st.set_page_config(
    page_title="AI Trading System — PRIMARY SIGNAL VIEW",
    layout="wide"
)

st.title("AI Trading System — PRIMARY SIGNAL VIEW")
st.caption("Read-only decision intelligence • No auto trading")

# -------------------------------------------------------
# USER INPUT
# -------------------------------------------------------
symbols_input = st.text_input(
    "Enter symbols (comma separated)",
    value="TATASTEEL"
)

generate = st.button("Generate Signals")

# -------------------------------------------------------
# MAIN LOGIC
# -------------------------------------------------------
if generate:
    symbols_list = [s.strip().upper() for s in symbols_input.split(",") if s.strip()]

    if not symbols_list:
        st.warning("Please enter at least one symbol.")
        st.stop()

    with st.spinner("Generating signals..."):
        results = generate_signals_multi(symbols_list)

    if results is None or len(results) == 0:
        st.error("No data returned from engine.")
        st.stop()

    # ---------------------------------------------------
    # 🔧 CRITICAL FIX: NORMALIZE RESULT TYPE
    # ---------------------------------------------------
    if isinstance(results, list):
        df = pd.DataFrame(results)
    else:
        df = results

    if df.empty:
        st.error("Signal DataFrame is empty.")
        st.stop()

    # ---------------------------------------------------
    # SORT SAFELY
    # ---------------------------------------------------
    df = df.sort_values(["symbol", "time"]).reset_index(drop=True)

    # ===================================================
    # PRIMARY TRADE DECISION — PER SYMBOL
    # ===================================================
    st.markdown("---")
    st.subheader("🎯 PRIMARY TRADE DECISION (Per Symbol)")

    for symbol in symbols_list:
        df_symbol = df[df["symbol"] == symbol]

        if df_symbol.empty:
            st.warning(f"No data available for {symbol}")
            continue

        latest = df_symbol.iloc[-1]

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                label=f"{symbol} — PRIMARY SIGNAL",
                value=latest["primary_trade_signal"]
            )

        with col2:
            st.metric(
                label="CONFIDENCE",
                value=f"{latest['confidence']}%"
            )

        with col3:
            st.metric(
                label="CONFIDENCE BUCKET",
                value=latest["confidence_bucket"]
            )

        with col4:
            st.metric(
                label="RISK",
                value=latest["risk_label"]
            )

        st.markdown("---")

    # ===================================================
    # SIGNAL BREAKDOWN TABLE (READ ONLY)
    # ===================================================
    st.subheader("Signal Breakdown (Review Only)")
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )
