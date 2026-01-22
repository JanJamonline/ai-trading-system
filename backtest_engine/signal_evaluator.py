import pandas as pd

class SignalEvaluator:
    """
    Evaluates signal quality, conflicts, and confidence score.
    """

    def calculate_confidence_score(
        self,
        ta_strength: int,
        fa_strength: int,
        ta_signal: str,
        fa_signal: str,
        risk_label: str
    ) -> int:
        """
        Returns confidence score between 0 and 100
        """

        # Base score
        base = (ta_strength + fa_strength) / 2

        # Agreement / conflict adjustment
        if (
            (ta_signal == "BUY" and fa_signal == "BULLISH")
            or (ta_signal == "SELL" and fa_signal == "BEARISH")
        ):
            base += 20
        elif ta_signal in ["BUY", "SELL"] and fa_signal != "NEUTRAL":
            base -= 15

        # Risk adjustment
        if risk_label == "LOW_RISK":
            base += 10
        elif risk_label == "HIGH_RISK":
            base -= 20

        # Clamp
        return int(max(0, min(100, base)))
