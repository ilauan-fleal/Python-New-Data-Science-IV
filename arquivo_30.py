import pandas as pd
import numpy as np


#Upsampling e interpolação

dados  = pd.DataFrame(np.random.randn(3,5),
                      index=pd.date_range('1/1/2001', periods=3, freq='W-WED'),
                      columns=['Alpha','Beta','Gama','Delta', 'Sigma'])


print(dados)

x = dados.resample('D').ffill()

print('\n\n')

print(x)
