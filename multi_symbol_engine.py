import pandas as pd
from ta_module.ta_manager import TAManager
from fa_module.fa_manager import FAManager
from signal_fusion.fusion_engine import FusionEngine

def generate_signals_multi(symbols):
    results = []

    for symbol in symbols:
        price_df = pd.read_csv(f"data/{symbol}_5m.csv")

        ta = TAManager()
        fa = FAManager("data/fa_data.csv")
        fusion = FusionEngine()

        for i in range(1, len(price_df)):
            ta_signal, ta_strength = ta.evaluate(price_df, i)
            fa_signal, fa_strength = fa.evaluate(symbol)

            fused = fusion.combine(
                ta_signal, ta_strength,
                fa_signal, fa_strength
            )

            results.append({
                "time": price_df.iloc[i]["time"],
                "symbol": symbol,
                "price": price_df.iloc[i]["close"],
                "ta_signal": ta_signal,
                "ta_strength": ta_strength,
                "fa_signal": fa_signal,
                "fa_strength": fa_strength,
                "signal": fused["signal"],
                "quality": fused["quality"],
                "action": fused["action"]
            })

    return pd.DataFrame(results)
