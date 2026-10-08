#Código para fazer parse de data!

from dateutil.parser import parse

x = parse('2021-07-03, 09:00 AM')

print(x)


#Outro exemplo

y = parse('Jan 16, 2018 11:00 AM')

print(y)

#Mais um exemplo

z = parse('05/12/2018, 10:00 AM', dayfirst=True)
    
print(z)
