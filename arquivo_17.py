#Deslocando datas com  offsets!

from pandas.tseries.offsets import MonthEnd
from datetime import datetime
import pandas as pd
import numpy as np

hoje =  datetime(2026, 9, 27)

print(hoje)


x = hoje + MonthEnd()

y = hoje + MonthEnd(2)

z =  MonthEnd()

print(x)

print(y)

k  = z.rollforward(hoje)
u = z.rollback(hoje)
print(k)
print(u)

print('\n\n')

h = pd.Series(np.random.randn(15), index=pd.date_range('7/12/2012', periods=15, freq='5D'))

print(h)

print('\n\n')

g = h.resample('ME').mean()

print(g)

