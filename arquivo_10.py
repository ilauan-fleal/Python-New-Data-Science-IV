
#Convertendo string em data com o uso de DateTime
import datetime
valor = '2018-03-01'

x = datetime.datetime.strptime(valor,'%Y-%m-%d')

datas_aleatorias = ['07/05/2021', '07/06/2022']

k = [datetime.datetime.strptime(x, '%m/%d/%Y') for x in datas_aleatorias]

print(k)

