'''
https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/
'''
import pandas as pd
import numpy as np


movies_df = pd.read_csv("IMDB-Movie-Data.csv", index_col="Title")
'''
Example on how to cleanup
'''

# Print out column names
print(movies_df.columns)

# Rename column names
movies_df.rename(columns={
                 'Runtime (Minutes)': 'Runtime',
                 'Revenue (Millions)': 'Revenue_millions'
                }, inplace=True)

print(movies_df.columns)

# Directly change the whole columns
# movies_df.columns = ['rank', 'genre', 'description', 'director', 'actors', 'year',\
                     # 'runtime', 'rating', 'votes', 'revenue_millions', 'metascore']

# Alternately
movies_df.columns = [col.lower() for col in movies_df]

print(movies_df.columns)
