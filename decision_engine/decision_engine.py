from signal_fusion.fusion_engine import SignalFusionEngine


class DecisionEngine:
    def __init__(self):
        self.fusion = SignalFusionEngine()

    def decide(self, ta_result, fa_result):
        return self.fusion.fuse(ta_result, fa_result)
