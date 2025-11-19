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
    output_path = Path(__file__).parent/'outputs'/f'{ticker}_price.png'
    output_path.parent.mkdir(exist_ok=True)
    plt.savefig(output_path)
    print(f'saved chart as {output_path}')
    plt.show()


def main():
    #list called tickers
    tickers = ['AAPL', 'MSFT', 'GOOGL', 'TSLA']
#loops through the tickers in the list of tickers and executes the following code
    for ticker in tickers:
        #data variable runs the ticker function that gets the stock data
        data = fetch_stock_data(ticker)
        #prints the ticker name on a new line. saying its the summary useless code basically just names the graph
        print(f'\n{ticker} Summary:')
        #this shows the start price of ticker using the data from the fetch data function. it gets the start price from the first line of the data 
        #this 'finds' this first line using .iloc it starts from 0 since python iterates from 0 as 1
        print(f'Start Price: ${data['Close'].iloc[0].item():.2f}')
        #this find the last line of the data showing the ending price of the stock it starts indexing at the last line 
        print(f'end price: ${data['Close'].iloc[-1].item():.2f}')
        #this is the arithmetic done to get the total returns made on the stock
        print(f'return: {(data['Close'].iloc[-1].item()/data['Close'].iloc[0].item()-1)*100:.2f}%')
        plot_stock_price(data,ticker)
        print('-'*50)
main()