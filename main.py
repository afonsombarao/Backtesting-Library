class Trade:
    def __init__(self, buy, sell, time, stop_loss=None, take_profit=None):
        self.buy = buy
        self.sell = sell
        self.time = time
        self.stop_loss = stop_loss if stop_loss is not None else None
        self.take_profit = take_profit if take_profit is not None else None
        
    def profit(self):
        return self.sell - self.buy

    def profit_perc(self):
        return (self.sell - self.buy)/self.buy
