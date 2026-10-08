#Tabelas de pivoteamento

import pandas as pd

x = pd.read_csv('tips.csv')

x['tip_pct'] = x['tip']/x['total_bill']


k = x.pivot_table(['tip_pct','size'],index=['time','day'],columns='smoker', aggfunc=len, margins=True)

#Tabela de pivô que calcula a frequência dos grupos:

z = pd.crosstab([x.time,x.day],x.smoker, margins=True)


print(k)

print("\n\n")

print(z)