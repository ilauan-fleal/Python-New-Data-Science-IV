#Gerando séries temporais mais longas com date_range()


import pandas as pd
import numpy as np

dados = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))

print(dados)