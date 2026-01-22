# signal_fusion/fusion_engine.py

class FusionEngine:
    """
    Combines TA + FA signals into:
    - final signal
    - quality
    - risk label
    - numeric confidence
    - confidence bucket (A.14)
    """

    def __init__(self):
        pass

    def _confidence_bucket(self, confidence: float) -> str:
        """
        A.14 CONFIDENCE BUCKETS
        """
        if confidence >= 75:
            return "STRONG"
        elif confidence >= 50:
            return "MODERATE"
        elif confidence >= 25:
            return "WEAK"
        else:
            return "VERY_WEAK"

    def fuse(
        self,
        ta_signal: str,
        ta_strength: float,
        fa_signal: str,
        fa_strength: float
    ):
        """
        Core fusion logic (unchanged)
        """

        # --- SIGNAL ---
        if ta_signal == "BUY" and fa_signal in ["BUY", "NEUTRAL"]:
            signal = "BUY"
        elif ta_signal == "SELL" and fa_signal in ["SELL", "NEUTRAL"]:
            signal = "SELL"
        else:
            signal = "HOLD"

        # --- QUALITY ---
        quality = "STRONG" if ta_strength >= 70 else "WEAK"

        # --- RISK ---
        risk_label = "LOW_RISK" if quality == "STRONG" else "HIGH_RISK"

        # --- CONFIDENCE SCORE (NUMERIC) ---
        confidence = round((ta_strength * 0.7) + (fa_strength * 0.3), 2)

        # --- A.14 CONFIDENCE BUCKET ---
        confidence_bucket = self._confidence_bucket(confidence)

        return {
            "signal": signal,
            "quality": quality,
            "risk_label": risk_label,
            "confidence": confidence,
            "confidence_bucket": confidence_bucket
        }
