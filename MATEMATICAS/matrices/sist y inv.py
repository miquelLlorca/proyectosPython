def printMat(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end='  ')
        print()
        
def identidad(n):
    identidad = []
    for i in range(n):
        identidad.append([])
        for j in range(n):
            if i == j:
                identidad[i].append(1)
            else:
                identidad[i].append(0)
    return identidad

def diagonalizar(M, Inv):
    if Inv:
        ID = identidad(len(M))
    for j in range(len(M[0])-1):
        for i in range(len(M)):
            if i != j:
                n = M[i][j]
                ref = j
                
                if n != 0:
                    a = M[ref][j]
                    b = n
                    if a > 0 and b > 0 or a < 0 and b < 0:
                        a *= -1
                    for k in range(len(M[0])):
                        M[i][k] = a*M[i][k] + b*M[ref][k]
                        if Inv:
                            ID[i][k] = a*ID[i][k] + b*ID[ref][k]
                        else:
                            ID = None
    for i in range(len(M)):
        for k in range(len(M[0])):
            if M[i][i] != 0:
                M[i][k] = M[i][k]/M[i][i]
                if Inv:
                    ID[i][k] = ID[i][k]/M[i][i]
                
    print(M)
    return M, ID

#solo funciona con m de rango igual a dim, en realidad no funciona (xd),  REVISAR LINEAS 30 - 35

M = [[1, 2], [3, 4]]
inv = True
M, ID = diagonalizar(M, inv)
if inv:
    printMat(ID)
else:
    for i in range(len(M)):
        print('x{} = {}'.format(i, M[i][len(M)-1]))
    
