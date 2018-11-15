import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from statsmodels.tsa.stattools import adfuller

data = np.asarray(pd.read_csv("FB.csv")['Adj Close'])

rets = np.divide(data[1:] - data[:-1], data[:-1])

m = np.mean(rets)
s = np.std(rets)

print(adfuller(rets)[1])

plt.figure()
plt.hlines(m,0,130,color="blue",linestyle="--")
plt.hlines(m+2*s,0,130, color = "red")
plt.hlines(m-2*s,0,130, color = "red")
plt.scatter(range(len(rets)), rets)
plt.show()
