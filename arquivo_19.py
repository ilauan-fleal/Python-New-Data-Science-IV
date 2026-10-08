#Localização e conversão de fusos horários!
#Minha implementação

import pandas as pd
import numpy as np


x = pd.date_range('7/6/2026 10:30', periods=7, freq='D', tz='UTC')


y = pd.Series(np.random.randn(len(x)), index=x)

print(y.index)




