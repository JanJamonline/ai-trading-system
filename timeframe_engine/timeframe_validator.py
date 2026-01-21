class TimeframeValidator:
    """
    Validates signal confirmation across multiple timeframes.
    This version is LOGIC-ONLY and does not alter execution yet.
    """

    def __init__(self):
        pass

    def validate(self, lower_tf_signal: str, higher_tf_signal: str) -> bool:
        """
        Returns True if signals are aligned, else False.

        BUY + BUY   → True
        SELL + SELL → True
        Anything else → False
        """

        if lower_tf_signal == higher_tf_signal:
            return True

        return False
