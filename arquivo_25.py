import pandas as pd
import numpy  as np


x  = pd.period_range('2010Q1', '2010Q2', freq='Q-JAN')

s = pd.Series(np.arange(len(x)), index=x)

print(s)