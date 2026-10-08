#Outro exemplo de código, com operação de fusos horários!

from pandas.tseries.offsets import Hour

import pandas as pd

x = pd.Timestamp('2010-02-12  08:30', tz='US/Eastern')

print(x)


print(x + Hour())

