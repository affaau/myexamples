'''
https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/
'''
import pandas as pd
import numpy as np


movies_df = pd.read_csv("IMDB-Movie-Data.csv", index_col="Title")
'''
Handle missing or null value
   Python - None
   Numpy - np.nan
'''

movies_df.columns = [col.lower() for col in movies_df]

'''
Notice isnull() returns a DataFrame where each cell is either True or False depending
on that cell's null status.
'''
print(movies_df.isnull())

# Obe of the row with NaN column
#print(movies_df.loc['Secret in Their Eyes'])

# Count number of nulls in each column
print(movies_df.isnull().sum())

# Remove rows with null
# This operation will delete any row with at least a single null value
movies_df.dropna()
