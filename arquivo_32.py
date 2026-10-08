#Funções da janela móvel!
#Gerando gráficos dinâmicos com Python!


import pandas as pd
from matplotlib import pyplot as plt

x  = pd.read_csv('stock_px_2.csv', parse_dates=True, index_col=0)

y  = x[['AAPL','MSFT','XOM']]

z  = y.resample('B').ffill()

z.AAPL['2001':'2012'].rolling(250).mean().plot(style='k--', label='Simple MA')
plt.legend()
plt.show() 