import pandas as pd

class SignalEvaluator:
    def evaluate_primary_signal(self, results):
        df = pd.DataFrame(results)

        actionable = df[df["primary_trade_signal"].isin(["BUY", "SELL"])]

        total = len(actionable)
        wins = len(actionable[actionable["quality"] == "STRONG"])
        losses = total - wins

        flip_rate = (
            (actionable["primary_trade_signal"] != actionable["signal"])
            .mean() if total > 0 else 0
        )

        return {
            "total": total,
            "wins": wins,
            "losses": losses,
            "win_rate": wins / total if total else 0,
            "loss_rate": losses / total if total else 0,
            "flip_rate": flip_rate,
            "verdict": "STABLE" if wins >= losses else "UNSTABLE"
        }
