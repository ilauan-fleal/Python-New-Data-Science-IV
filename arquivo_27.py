#Convertendo timestamps() para períodos:

import pandas as pd
import numpy as np

x = pd.date_range('2010-01-02', periods=6, freq='ME')
y = pd.Series(np.random.randn(6), index=x)
z = y.to_period()

print(z)