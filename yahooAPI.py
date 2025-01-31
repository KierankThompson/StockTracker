import yfinance as yf
from datetime import datetime, timedelta
import sys




def getPrice(ticker,date):
    #assume a cleaned input string
    endDate = datetime.strptime(date, '%Y-%m-%d')
    endDate = endDate + timedelta(days=1)
    data = yf.Ticker(ticker).history(start=date, end=endDate)
    try:    
        closingPrice = data['Close'].iloc[0]
    except IndexError:
        print(f"Error with stock: {ticker}")
        print("exiting...")
        exit(1)
    return closingPrice

def getPrices(tickers,date):
    #assume a cleaned input string
    endDate = datetime.strptime(date, '%Y-%m-%d')
    endDate = endDate + timedelta(days=1)
    tickerArr = tickers.split(" ")
    tickerArr = [s for s in tickerArr if s.strip()]
    stockPrices = {}
    for ticker in tickerArr:
        stockPrices[ticker] = getPrice(ticker, date).item()
    return stockPrices


    

def main():
    date = '2025-01-24'
    ticker = 'MRK KO AAPL'
    stocks = getPrices(ticker,date)
    print(stocks)


if __name__ == "__main__":
    main()


