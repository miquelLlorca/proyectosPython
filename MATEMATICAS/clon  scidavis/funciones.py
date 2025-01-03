from random import randrange

def ajuste(x, y):
    sumxy= 0
    sumxx = 0
    sumx = 0
    sumy = 0
    n = len(x)
    for i in range(n):
        sumxy += x[i]*y[i]
        sumxx += x[i]**2
        sumx += x[i]
        sumy += y[i]
    m = (sumxy - (sumx * sumy)/n)/(sumxx - (sumx**2)/n)
    b = sumy/n - sumx*m/n
    return m,b

def leerArchivo():
    nombre = input('Nombre del arhivo: ')
    sep = input('Separador: ')
    linign = int(input('Lineas a ignorar: '))
    ejex = int(input('Columna de x: '))
    ejey = int(input('Columna de y: '))
    entrada = open(nombre, 'r')

    for i in range(linign + 1):
        linea = entrada.readline()
    linea2 = linea[0:len(linea)-1]
    x = []
    y = []
    while linea != '':
        nums = linea2.split(sep)
        x.append(float(nums[0]))
        y.append(float(nums[1]))
        linea = entrada.readline()
        if linea != '':
            if linea[len(linea)-1] == '\n':
                linea2 = linea[0:len(linea)-1]
            else:
                linea2 = linea
    entrada.close()
    return x, y

def generar():
    n = int(input('Nº de puntos a generar: '))
    RX = input('Rango de valores de X: ').split()
    RY = input('Rango de valores de Y: ').split()
    
    x = []
    y = []
    for i in range(n):
        x.append(randrange(float(RX[0]), float(RX[1])))
        y.append(randrange(float(RY[0]), float(RY[1])))
    return x, y

def maymen(lista):
    for i in range(len(lista)):
        if i == 0:
            may = lista[i]
            men = lista[i]
        elif lista[i] < men:
            men = lista[i]
        elif lista[i] > may:
            may = lista[i]
    return may, men
