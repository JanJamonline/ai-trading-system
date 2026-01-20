class TAManager:
    def compute(self, prices, index):
        if index == 0:
            return "WARMUP"

        if prices[index] > prices[index - 1]:
            return "UP"
        elif prices[index] < prices[index - 1]:
            return "DOWN"
        else:
            return "FLAT"
