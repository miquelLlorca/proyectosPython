n = int(input('n = '))
lista = []
for i in range(2,n+1):
    for j in range(i):
        lista.append(j+1)
lista.append(1)
for k in range(len(lista)):
    if k == len(lista)-1:
            break
    if lista[k+1] == 1:
        print('{}.'.format(lista[k]))
    else:
        print(lista[k],end=', ')
    

