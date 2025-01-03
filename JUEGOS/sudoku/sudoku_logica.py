from random import randint

def crearSud():
    sudoku = []
    for i in range(9):
        sudoku.append([])
        for j in range(9):
            sudoku[i].append(0)
    return sudoku

def printSud(s):
    for fila in range(9):
        for cuad in range(3):
            for pos in range(3):
                a, b = ajustar(fila)
                print(s[cuad + b][pos + a], end=' ')
                if pos == 2:
                    print('    ', end='')
        print()
        if (fila +1)% 3 == 0:
            print()
    return

def ajustar(n):
    if n == 2 or n == 5 or n == 8:
        a = 6
    elif n == 1 or n == 4 or n == 7:
        a = 3
    elif n == 0 or n == 3 or n == 6:
        a = 0

    if n < 3:
        b = 0
    elif 3 <= n < 6:
        b = 3
    else:
        b = 6
    return a, b

def buscar(s, num, cuad, pos, lista, pos2):
    if num in s[cuad]:
        #print('a')
        return True
    
    if num in lista[pos2]:
        #print('b')
        return True

    if pos2 != 0:
        for i in range(pos2):
            if num == lista[i][pos]:
                #print('c')
                return True
    return False

def llenarSud(s):
    filas = []
    for fila in range(9):
        filas.append([])
        a, b = ajustar(fila) 
        for cuad in range(3):
            for pos in range(3):
                n = randint(1,9)
                print(cuad +b, pos + a)
                esta = buscar(s, n, cuad, pos, filas, fila)
                while esta == True:
                    n = randint(1,9)
                    esta = buscar(s, n, cuad + b, pos + a, filas, fila)
                filas[fila].append(n)
                s[cuad + b][pos + a] = n
                #print(n)
        
        printSud(s)

sudoku = crearSud()
llenarSud(sudoku)
printSud(sudoku)
