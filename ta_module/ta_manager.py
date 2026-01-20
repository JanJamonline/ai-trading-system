class TAManager:
    def __init__(self):
        self.last_signal = None

    def compute(self, current_row, previous_row):
        """
        Basic momentum-based TA.
        """
        if current_row["close"] > previous_row["close"]:
            return {
                "signal": "BUY",
                "direction": "BULLISH",
                "confidence": 70,
                "reason": "UP"
            }

        if current_row["close"] < previous_row["close"]:
            return {
                "signal": "SELL",
                "direction": "BEARISH",
                "confidence": 70,
                "reason": "DOWN"
            }

        return {
            "signal": "HOLD",
            "direction": "NEUTRAL",
            "confidence": 0,
            "reason": "FLAT"
        }
