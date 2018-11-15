import requests
import pandas as pd
import csv
import io
import datetime

now = datetime.datetime.now()
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
today = "%s+%d+%d" % (months[now.month], now.day, now.year)
one_year_ago = "%s+%d+%d" % (months[now.month], now.day, now.year-1)

# @param tickers: list of tickers
# @param startdate: the first date to get stock data for
#                   default is one year ago
# @param enddate: the last date to get stock data for
#                 default is today
# also get dividend data and append as a column
# @return dictionary of pandas dataframes of all historical data for all stocks
def get_bulk_stock_data(tickers = [], startdate = one_year_ago,
                        enddate = today):
    data = {}
    for t in tickers:
        url = "http://finance.google.com/finance/historical?q="+"%s&startdate=%s&enddate=%s&output=csv" % (t, startdate, enddate)
        c = requests.get(url)
        data[t] = pd.read_csv(io.StringIO(c.text))

    return data




# @param stocks: a dictionary of dataframes for stock data
# appends a column of the adjusted closing prices
#def get_dividend_adj_closing_prices(stocks):


stock_tickers = ['MSFT']
stock_data = get_bulk_stock_data(stock_tickers)
print(stock_data)
