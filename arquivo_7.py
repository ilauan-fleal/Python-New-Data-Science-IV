#Correlação de pares e função de regressão linear 

import pandas as pd

d = pd.read_csv('stock_px_2.csv', parse_dates=True, index_col=0)


#pct_change() -> Calcula as mudanças percentuais por ano;

r = d.pct_change().dropna()

ano = lambda z: z.year

por_ano = r.groupby(ano)

u = por_ano.apply(lambda k: k['AAPL'].corr(k['MSFT']))


print(u)