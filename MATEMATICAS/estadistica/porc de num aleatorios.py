from random import randrange

def media(x):
    suma = 0
    long = len(x)
    for i in range(0,len(x)):
        term = x[i]
        suma += term
    return round(suma/long,5)
    
def desv(x):
    n = len(x)
    m = media(x)
    suma = 0
    for i in range(0,len(x)):
        suma += (x[i] - m)**2
    return round((suma / (n - 1))**0.5, 5)

n = 1000000
lista = []
nums = []
for i in range(n):
    lista.append(randrange(0,10))

for i in range(10):
    cont = 0
    for j in range(n):
        if lista[j] == i:
            cont += 1
    nums.append(cont)
    p100 = 100*cont/n
    print('El numero {} aparece {} veces, {}%.'.format(i, cont, p100))

print('La media es de {} .'.format(media(nums)))
print('La desviacion es de {} .'.format(desv(nums)))
