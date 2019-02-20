#!/usr/bin/python3
# coding: utf-8

## Following Mastering Python for Finance

import matplotlib.pyplot as plt
import pandas_datareader as web
import datetime

start = datetime.datetime(2017, 11, 1)
end = datetime.datetime(2019, 2, 19)
Razer = "1337.HK"
df = web.DataReader(Razer, 'yahoo', start, end)
print(df.head())

plt.figure()
df['Close'].plot(title="Razer", legend=True)
df['Open'].plot(legend=True)

start2 = datetime.datetime(2017, 11, 1)
end2 = datetime.datetime(2019, 2, 19)
HSBC = "0005.HK"
df2 = web.DataReader(HSBC, 'yahoo', start2, end2)
print(df2.tail())

# figsize(width, height) in terms of inch/cm !?
plt.figure(figsize=(10,5))
df2['Close'].plot(title="HSBC", legend=True)

plt.show()