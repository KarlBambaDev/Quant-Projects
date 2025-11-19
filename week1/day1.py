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

def plot_stock_price(data,ticker):
    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'], linewidth =2)
    plt.title(f'{ticker} Stock Price', fontsize=16)
    plt.xlabel('Date')
    plt.ylabel('Price($)')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    output_path = Path(__file__).parent.parent/'outputs'/f'{ticker}_price.png'
    output_path.parent.mkdir(exist_ok=True)
    plt.savefig(output_path)
    print(f'saved chart as {output_path}')


def main(ticker):
    