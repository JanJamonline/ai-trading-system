class SignalAccuracy:
    def compute(self, signals):
        stats = {
            "BUY": {"correct": 0, "total": 0},
            "SELL": {"correct": 0, "total": 0},
            "HOLD": {"correct": 0, "total": 0},
        }

        for s in signals:
            sig = s["signal"]
            if sig not in stats:
                continue

            stats[sig]["total"] += 1
            if s.get("outcome") == "CORRECT":
                stats[sig]["correct"] += 1

        return stats
