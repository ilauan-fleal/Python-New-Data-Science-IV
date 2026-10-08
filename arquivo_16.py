#Fazendo deslocamento de datas com o Python(pandas)

import pandas as pd
import numpy  as np

t = pd.Series(np.random.randn(5), index=pd.date_range('1/1/2007', periods=5, freq='ME'))

print(t)