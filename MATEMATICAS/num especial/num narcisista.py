
for i in range(10, 9999999):
    suma = 0
    x = str(i)
    for j in x:
        suma += int(j)**len(x)

    if suma == i:
        print(i, 'True')
