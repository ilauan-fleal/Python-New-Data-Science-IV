#Exemplo de programa em Python com série temporal!

from datetime import datetime
import pandas as pd
import numpy as np


dados = [datetime(2020,7,8), datetime(2021,4,5),datetime(2022,1,1)]

d = pd.Series(np.random.randn(3), index=dados)
print(d)
