suma = 0
for i in range(3000, 3500):
    x = str(i)
    for j in x:
        suma += int(j)**int(j)

    if suma == i:
        print(i, 'True')

    suma = 0
