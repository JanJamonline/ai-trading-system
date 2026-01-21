class FlipAnalysis:
    def analyze(self, signals):
        flips = 0

        for i in range(2, len(signals)):
            if signals[i]["signal"] == signals[i - 2]["signal"] and \
               signals[i]["signal"] != signals[i - 1]["signal"]:
                flips += 1

        return {
            "flip_count": flips,
            "total_signals": len(signals),
            "flip_rate": round(flips / max(len(signals), 1), 3),
        }
