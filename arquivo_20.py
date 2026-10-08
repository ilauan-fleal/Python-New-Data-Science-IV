#Outro exemplo de operações com fusos horários em Python!

import pandas as pd
import numpy as np



x = pd.date_range('7/6/2026 11:50', periods=7, freq='D', tz='UTC')


y = pd.Series(np.random.randn(len(x)), index=x)


z = y.tz_convert('America/New_York')

print(z)


