class Trade:
    def __init__(self, prices):
        self.prices = prices
        
    def buy(self):
        return self.prices[0]

    def sell(self):
        return self.prices[-1]
    
    def profit(self):
        return self.sell() - self.buy() 

    def profit_perc(self):
        return self.profit()/self.buy()

