# -*- coding: utf-8 -*-
import pandas as pd
from datetime import datetime
import numpy as np

dates = pd.date_range('20141001', periods=7)   # any specified date
print(dates)

dates = pd.date_range(datetime.today().strftime('%Y%m%d'), periods=7) # from today
print(dates)

# into DataFrame
dates = pd.DataFrame(np.random.randn(7,3), index=dates, columns = list('ABC'))

print(dates)
print(type(dates))