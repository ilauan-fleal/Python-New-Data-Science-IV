#Exemplo de DataFrame , com indexação em suas linhas!

import pandas as pd
import numpy as np


dados = pd.date_range('1/1/2000', periods=1000, freq='W-WED')


novo_dataframe = pd.DataFrame(np.random.randn(1000,4), index=dados, columns=['Alpha','Gama','Beta','Delta'])

print(novo_dataframe)