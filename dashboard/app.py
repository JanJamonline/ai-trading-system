# dashboard/app.py

import sys
from pathlib import Path

# ============================================================
# FORCE PROJECT ROOT INTO PYTHON PATH (STREAMLIT SAFE)
# ============================================================
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

# ============================================================
# STANDARD IMPORTS
# ============================================================
import streamlit as st
import pandas as pd

from multi_symbol_engine import generate_signals_multi

# ============================================================
# STREAMLIT PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="AI Trading System — PRIMARY SIGNAL VIEW",
    layout="wide"
)

# ============================================================
# HEADER
# ============================================================
st.title("AI Trading System — PRIMARY SIGNAL VIEW")
st.caption("Read-only decision intelligence • No auto trading")

# ============================================================
# USER INPUT
# ============================================================
symbols_input = st.text_input(
    "Enter symbols (comma separated)",
    value="TATASTEEL"
)

symbols_list = [s.strip().upper() for s in symbols_input.split(",") if s.strip()]

# ============================================================
# GENERATE SIGNALS
# ============================================================
if st.button("Generate Signals"):
    if not symbols_list:
        st.warning("Please enter at least one symbol.")
    else:
        try:
            results = generate_signals_multi(symbols_list)

            if not results:
                st.warning("No data returned.")
            else:
                df = pd.DataFrame(results)

                # ====================================================
                # PRIMARY SIGNAL CARD (LATEST ROW)
                # ====================================================
                latest = df.iloc[-1]

                st.markdown("## 🎯 PRIMARY TRADE DECISION")

                col1, col2, col3, col4 = st.columns(4)

                col1.metric(
                    "PRIMARY SIGNAL",
                    latest.get("primary_trade_signal", "HOLD")
                )

                col2.metric(
                    "CONFIDENCE",
                    latest.get("quality", "UNKNOWN")
                )

                col3.metric(
                    "RISK",
                    latest.get("risk_label", "UNKNOWN")
                )

                col4.metric(
                    "ACTION",
                    latest.get("final_action", "WAIT")
                )

                st.divider()

                # ====================================================
                # FULL TABLE (REVIEW ONLY)
                # ====================================================
                st.markdown("### Signal Breakdown (Review Only)")
                st.dataframe(df, use_container_width=True)

        except Exception as e:
            st.error(str(e))
