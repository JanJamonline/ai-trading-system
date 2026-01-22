class SignalEvaluator:
    """
    Evaluates agreement between multiple timeframes
    """

    def timeframe_agreement(self, signal_5m: str, signal_15m: str):
        if signal_5m == signal_15m and signal_5m in ["BUY", "SELL"]:
            return True, signal_5m

        if signal_5m == "HOLD" or signal_15m == "HOLD":
            return False, "HOLD"

        return False, "HOLD"
