
import pytz
import pandas as pd

x = pytz.common_timezones[-3:]

print(x)

t = pytz.timezone('UTC')

#Gerando intervalo de datas com definição de fusos horários

s = pd.date_range('3/9/2020 8:30', periods=12, freq='D', tz='UTC')

print(s)



