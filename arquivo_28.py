#Como criar um periodIndex, a partir de Arrays!

import pandas as pd

x = pd.read_csv('macrodata.csv')



print(x.head(7))

indice = pd.PeriodIndex.from_fields(year=[2000,2001], month=[1,1], freq='Y')
print(indice)