# timeframe_engine/timeframe_validator.py

class TimeframeValidator:
    def validate(self, signal_5m, signal_15m):
        if signal_15m is None:
            return "UNKNOWN"

        if signal_5m == signal_15m:
            return "CONFIRMED"

        return "CONFLICT"
