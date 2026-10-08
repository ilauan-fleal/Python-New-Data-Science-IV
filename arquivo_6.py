#Cálculo de média ponderada de grupos e correlações:

import pandas as pd
import numpy as np

d = pd.DataFrame({'categoria':['A','A','A','A',
                               'B','B','B','B'],
                    'dados':np.random.randn(8),
                    'pesos':np.random.rand(8)})


print(d)

agrupamento = d.groupby('categoria')

valor = lambda x: np.average(x['dados'], weights=x['pesos'])

k = agrupamento.apply(valor)


print(k)