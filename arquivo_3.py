#Trabalhando o método group.by com laço for

import pandas as pd
import numpy as np


d = pd.DataFrame({'chave_1':['A','A','B','B','B'],
                  'chave_2':['Um','Dois','Um','Dois','Um'],
                  'dados_1': np.random.randn(5),
                  'dados_2': np.random.randn(5)})


for (x,y), grupos in d.groupby(['chave_1','chave_2']):
    print((x,y))
    print(grupos)



