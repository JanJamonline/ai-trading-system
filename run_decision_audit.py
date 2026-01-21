from multi_symbol_engine import generate_signals_multi
from analysis.decision_audit import audit_decisions

symbols = ["TATASTEEL"]

results = generate_signals_multi(symbols)
audit_decisions(results)
