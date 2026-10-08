#Fazendo agregação de dados com Séries temporais!

import pandas as pd
import numpy as np
r = pd.date_range('2001-02-03', periods=12, freq='min')
d = pd.Series(np.arange(12), index=r)
print(r)
