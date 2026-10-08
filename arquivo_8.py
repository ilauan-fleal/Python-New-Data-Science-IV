#Implementando função de regressão linear
import statsmodels.api as s

import pandas as pd

def regressao_linear(dados, y, x):
    var_1 = dados[y]
    var_2 = dados[x]
    var_2['intercept'] = 1
    resultado = s.OLS(var_1,var_2).fit()
    return resultado.params


d = pd.read_csv('stock_px_2.csv', parse_dates=True, index_col=0)


#pct_change() -> Calcula as mudanças percentuais por ano;

r = d.pct_change().dropna()

ano = lambda z: z.year

por_ano = r.groupby(ano)

u = por_ano.apply(lambda k: k['AAPL'].corr(k['MSFT']))

k = por_ano.apply(regressao_linear,'AAPL',['SPX'])

print(u)

print(k)


