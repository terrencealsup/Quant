"""
Terrence Alsup

Risk and Portfolio Management with Econometrics
Assignment #1

Prof. Marco Avellaneda
"""

# Import packages.
import requests
import time
import pandas as pd
import csv
import datetime
try:
    # for Python 2.x
    from StringIO import StringIO
except ImportError:
    # for Python 3.x
    from io import StringIO

# Get the current date.
now = datetime.datetime.now()
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
today = "%s+%d+%d" % (months[now.month], now.day, now.year)
one_year_ago = "%s+%d+%d" % (months[now.month], now.day, now.year-1)

"""
Get the data for the list of tickers provided.
"""
def get_data(tickers = [], startdate = one_year_ago, enddate = today):

    # Dummy request to get the crumb (for Yahoo! Finance).
    session = requests.Session()
    r = session.get("https://finance.yahoo.com/lookup?s=bananas")
    str = r.text
    i = str.find("\"CrumbStore\":{\"crumb\":\"")
    crumb = str[i+23:i+34]

    data = {}

    for t in tickers:
        # Get data from Google Finance.
        url = "http://finance.google.com/finance/historical?q="+"%s&startdate=%s&enddate=%s&output=csv" % (t, startdate, enddate)
        c = requests.get(url)

        # It's possible there is no data for this stock during the time period.
        try:
            df1 = pd.read_csv(StringIO(c.text))
        except TypeError:
            df1 = pd.DataFrame(columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])


        # Get dividend data from Yahoo! Finance.
        url1 = "https://query1.finance.yahoo.com/v7/finance/download/%s?period1=%d&period2=%d&interval=1d&events=dividends&crumb=%s" % (t, startdate, enddate, crumb)
        r1 = session.post(url1)

        # It's possible there were no dividends paid.
        try:
            df2 = pd.read_csv(StringIO(r1.text), converters={"Dividends":float})
        except TypeError:
            df2 = pd.DataFrame(columns=['Date', 'Dividends'])

        # Fix Google's date format to match Yahoo!'s.
        for i in xrange(df1.shape[0]):
            temp_d = df1['Date'][i].split('-')
            d = ""
            if int(temp_d[0]) >= 0:
                d = d + "20%d", temp_d[0]


        # Merge the dataframes.



        # Calculate adjusted closing prices and add to the dataframe.




    return data



    print(get_data(['MSFT']))
