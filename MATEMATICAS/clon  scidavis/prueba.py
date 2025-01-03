
def maymen(lista):
    for i in range(len(lista)):
        if i == 0:
            may = lista[i]
            print(may)
        elif lista[i] > may:
            may = lista[i]
            print(may)

    for i in range(len(lista)):
        if i == 0:
            men = lista[i]
            print(men)
        elif lista[i] < men:
            men = lista[i]
            print(men)
        print('i {}, n {}'.format(i, lista[i]))
    return may, men


lista = [4, 2, 9, 5, 7, 1, 0, 12, 30, -34, -2, -9]

maymen(lista)
