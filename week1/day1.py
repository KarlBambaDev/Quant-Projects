'''
Day 1 Karl Bamba
Market Data analysis 1
11-17-2025
'''
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path 
def fetch_stock_data(ticker, start_date='2020-01-01'):
    #fetches the historical stock data
    #arguments: ticker() = stock symbol
    #returns dataframe: stock price data
    print(f'Fetching data for {ticker}')
    data = yf.download(ticker, start=start_date, end='2024-12-15')
    print(f'Downloaded {len(data)} days of data')
    return data
ticker = 'RTX'
fetch_stock_data(ticker)
