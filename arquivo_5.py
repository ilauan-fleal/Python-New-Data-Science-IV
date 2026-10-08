#Reordenando valores, a partir de uma função!

import pandas as pd

def reordenar(dataframe, n=5, column='tip_pct'):
    return dataframe.sort_values(by=column)[-n:]



x = pd.read_csv('tips.csv')

x['tip_pct'] = x['tip']/x['total_bill']



z = reordenar(x,n=6)


print(z)


h = x.groupby('smoker').apply(reordenar, n=1, column='total_bill')

print(h)
