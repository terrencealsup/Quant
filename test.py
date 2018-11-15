import requests
import time
import datetime
import pandas as pd
import csv
from matplotlib import pyplot as plt
import numpy as np
try:
    # for Python 2.x
    from StringIO import StringIO
except ImportError:
    # for Python 3.x
    from io import StringIO


def get_bulk_dividends(tickers=[], startdate=1486357200, enddate=1517893200):

    # dummy request to get the crumb
    session = requests.Session()
    r = session.get("https://finance.yahoo.com/lookup?s=bananas")
    str = r.text
    i = str.find("\"CrumbStore\":{\"crumb\":\"")
    crumb = str[i+23:i+34]

    # the list of dataframes
    data = {}

    for t in tickers:
        url = "https://query1.finance.yahoo.com/v7/finance/download/%s?period1=%d&period2=%d&interval=1d&events=historical&crumb=%s" % (t, startdate, enddate, crumb)
        r1 = session.post(url)
        temp = r1.text
        csvfile = StringIO(temp)
        data[t] = pd.read_csv(csvfile, converters={"Adj Close":float})

    return data



data = get_bulk_dividends(tickers=['MSFT'])
y = np.asarray(data['MSFT']['Adj Close'])



plt.figure()
plt.plot(y)
plt.show()
