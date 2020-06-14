'''
https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/
'''
import pandas as pd
import numpy as np

# no assign of index
# df = pd.read_csv('purchases.csv')
# print(df)

df = pd.read_csv('purchases.csv', index_col=0)
print(df)


df2 = pd.read_json("purchases.json")
print(df2)
