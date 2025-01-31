import yfinance as yf
from datetime import datetime, timedelta




def getPrice(ticker,date):
    #assume a cleaned input string
    endDate = datetime.strptime(date, '%Y-%m-%d')
    endDate = endDate + timedelta(days=1)
    data = yf.Ticker(ticker).history(start=date, end=endDate)
    closingPrice = data['Close'].iloc[0]
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
    print(stockPrices)


    

def main():
    date = '2025-01-24'
    ticker = 'AAPL MRK KO'
    getPrices(ticker,date)


if __name__ == "__main__":
    main()


