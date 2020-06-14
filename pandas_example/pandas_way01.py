'''
https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/
'''
import pandas as pd
import numpy as np

'''
A Series is essentially a column, and a DataFrame is a multi-dimensional
table made up of a collection of Series.
'''

# one easy way to creat DataFrame is Dict
data = {'apples': [3,2,0,1],
        'oranges': [0,3,7,2]
       }

#purchases = pd.DataFrame(data)

# alternative, to include index column
purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])
print(purchases)

# locate specific customer's order (row)
print(purchases.loc['June'])

# save to csv
purchases.to_csv('purchases.csv')
