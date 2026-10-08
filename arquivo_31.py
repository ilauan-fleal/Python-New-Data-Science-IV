#Fazendo reamostragem de dados com períodos!

import pandas as pd
import numpy as np

matriz = pd.DataFrame(np.random.randn(24,4),
                      index=pd.period_range('1-2000', '12-2001', freq='M'),
                      columns=['Alpha', 'Beta', 'Gama', 'Delta'])

x = matriz[:5]

y = matriz.resample('Y-DEC').mean()

z =  y.resample('Q-DEC', convention='end').ffill()

print(x)

print('\n\n')

print(y)

print('\n\n')

print(z)