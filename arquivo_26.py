
import pandas as pd
import numpy  as np


x  = pd.period_range('2010Q1', '2011Q2', freq='Q-JAN')

s = pd.Series(np.arange(len(x)), index=x)

r  = (x.asfreq('B', 'e') - 1).asfreq('D','s') + 16 * 60

q = r.to_timestamp()

print(q)
