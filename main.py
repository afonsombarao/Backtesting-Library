import yfinance as yf
import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

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

class Backtest:
    def __init__(self, strategy, data):
        self.data = data
        self.strategy = strategy

    def closes(self):
        return self.data['Close'].to_numpy()
