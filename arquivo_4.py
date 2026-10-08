#Aplicação de group.by em um programa que envolve leitura de arquivo.csv

import pandas as pd

x = pd.read_csv('tips.csv')

x['tip_pct'] = x['tip']/x['total_bill']

agrupamento = x.groupby(['day','smoker'])

y = agrupamento['tip_pct']



s = y.agg(['mean', 'std'])

print(s)

