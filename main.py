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
        
    def present(self,n):
        return self.data.head(n)  
    
    def backtest(self):
        Trades = [] # lista onde vou guardar os objetos da classe Trade
        hold = False # se estou no modo hold ou nao
        i=0
        while i <= len(self.closes()): # iterar a função strategy sobre o closes
            if strategy(data.present(i),hold) and hold == False:
                a = Trade([self.closes()[i]])
                Trades.append(a)
            elif strategy(i,hold) == False and hold == True:
                pass
            i+=1
