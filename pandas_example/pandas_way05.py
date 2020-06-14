'''
https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/
'''
import pandas as pd
import numpy as np


movies_df = pd.read_csv("IMDB-Movie-Data.csv", index_col="Title")
'''
Example on how to remove duplicates
'''

temp_df = movies_df.append(movies_df)  # without affecting original
print(temp_df.shape)
print(movies_df.shape)

# Remove duplicates
temp_df = temp_df.drop_duplicates()  # return a copy

# Alternative - direct modify original
#temp_df.drop_duplicates(inplace=True)

print(temp_df)
