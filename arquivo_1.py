#Explorando o método group.by

import pandas as pd
import numpy as np

d = pd.DataFrame({'chave_1':['A','A','B','B','B'],
                  'chave_2':['Um','Dois','Um','Dois','Um'],
                  'dados_1': np.random.randn(5),
                  'dados_2': np.random.randn(5)})

grupo = d['dados_1'].groupby(d['chave_1'])

print(grupo.mean())