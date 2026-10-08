import pandas as pd

x = pd.Period(2009,  freq='Y-DEC')

print(x)

r = pd.period_range('2000-01-02','2000-06-30',freq='M')

print(r)


