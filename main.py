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

    def append_price(self, price):
        return self.prices.append(price)

class Backtest:
    def __init__(self, strategy, data):
        self.data = data
        self.strategy = strategy

    #trasnformar os closes do df data num array np
    def closes(self):
        list = self.data['Close'].to_numpy().tolist()
        return [x[0] for x in list]
    
    def present(self,n):
        return self.data.head(n+1) 
    
    def backtest(self):
        Trades = [] # lista onde vou guardar os objetos da classe Trade
        hold = False # se estou no modo hold ou nao
        for i, _ in enumerate(self.closes()):
            s = self.strategy(self.present(i), hold)

            if s and not hold: # buy signal == True
                a = Trade([self.closes()[i]])
                Trades.append(a)
                hold = True
                
            elif not s and not hold: # buy signal == False
                continue
                
            elif not s and hold: # caso sell signal == False
                a.append_price(self.closes()[i])
            
            else: # sell signal == True
                a.append_price(self.closes()[i])
                hold = False
            
        return Trades

    def num_trades(self):
        return len(self.backtest())

    def winning_trades(self):
        return len([1 for i in self.backtest() if i.profit() > 0])

    def win_rate(self):
        return self.winning_trades()/self.num_trades()
        
# Algumas estratégias que eu implementei para experimentar:

def strategy1(data, hold):
    if hold:
        return data.iloc[-1,0].item() > 170 
    else:
        return data.iloc[-1,0].item() < 140

def strategy2(data, hold):
    if not hold:
        return len(data)%10 == 0
    else:
        return (len(data)-5)%10 == 0
