

import pandas as pd

valores = ['2002Q3','2001Q2','2000Q1']

indice = pd.PeriodIndex(valores, freq='Q-DEC')

print(indice)



