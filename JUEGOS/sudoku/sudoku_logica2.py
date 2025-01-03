from random import randint

def crearSud():
    sudoku = []
    for i in range(9):
        sudoku.append([])
        for j in range(9):
            sudoku[i].append(0)
    return sudoku

def printSud(s):
    for i in range(9):
        for j in range(9):
            print(s[i][j], end=' ')
            if (j+1)%3 == 0:
                print('    ', end='')
        print()
        if (i+1)%3 == 0:
                print()

def ajustar(fila, pos):
    if fila < 3:
        cuadY = [0, 1, 2]
    elif 3 <= fila < 6:
        cuadY = [3, 4, 5]
    else:
        cuadY = [6, 7, 8]
    if pos < 3:
        cuadX = [0, 1, 2]
    elif 3 <= pos < 6:
        cuadX = [3, 4, 5]
    else:
        cuadX = [6, 7, 8]
        
    return cuadX, cuadY
    
def buscar(s, n, fila, pos):
    if n in s[fila]:
        print('a', n ,'--' ,s[fila])
        return True
    
    for i in range(fila):
        if n == s[i][pos]:
            print('b', s[i][pos], i, pos)
            return True
        
    cuadX, cuadY = ajustar(fila, pos)
    
    for x in cuadX:
        for y in cuadY:
            if n == s[y][x]:
                print('c', n, x, y)
                return True
    return False
            
def llenarSud(s):
    for i in range(9):
        for j in range(9):
            n = randint(1,9)
            #print(cuad +b, pos + a)
            esta = buscar(s, n, i, j)
            while esta == True:
                n = randint(1,9)
                esta = buscar(s, n, i, j)
            s[i][j] = n
            printSud(s)
    
    
sudoku = crearSud()
llenarSud(sudoku)
printSud(sudoku)
