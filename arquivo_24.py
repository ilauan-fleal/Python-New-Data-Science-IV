import pandas as pd
import numpy as np


x = pd.period_range('2006','2010', freq='Y-DEC')

y =  pd.Series(np.random.randn(len(x)), index=x)


z = y.asfreq('M', how='end')

print(y)

print(z)

