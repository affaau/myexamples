'''
https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/
'''
import pandas as pd
import numpy as np


movies_df = pd.read_csv("IMDB-Movie-Data.csv", index_col="Title")
print(movies_df.head())  # default first 5 rows
print(movies_df.tail(2))

# show essential details of dataset
print(movies_df.info())

# shows (rows, columns)
print(movies_df.shape)
