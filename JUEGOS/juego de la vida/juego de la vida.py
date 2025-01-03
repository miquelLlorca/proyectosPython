f = 10
c = 10
tablero = []
for i in range(f):
    tablero.append([False]*c)

tablero[4][4] = True
tablero[3][3] = True
tablero[3][5] = True
tablero[4][5] = True
tablero[5][4] = True

print('Estado inicial')
for i in range(f):
    for j in range(c):
        if tablero[i][j]:
            print('*', end='')
        else:
            print('-',end='')
    print()

pulsos = 6

for t in range(pulsos):
    nuevo = []
    for i in range(f):
        nuevo.append([False]*c)
        
    for y in range(f):
        for x in range(c):
            n = 0
            if y>0 and x>0 and tablero[y-1][x-1]:
                n+=1
            if x>0 and tablero[y][x-1]:
                n+=1
            if y<f-1 and x>0 and tablero[y+1][x-1]:
                n+=1
            if y>0 and tablero[y-1][x]:
                n+=1
            if y<f-1 and tablero[y+1][x]:
                n+=1
            if y>0 and x<c-1 and tablero[y-1][x+1]:
                n+=1
            if x<c-1 and tablero[y][x+1]:
                n+=1
            if y<f-1 and x<c-1 and tablero[y+1][x+1]:
                n+=1

            if tablero[y][x] and (n==2 or n==3):
                nuevo[y][x] = True
            elif not tablero[y][x] and n==3:
                nuevo[y][x] = True
            else:
                nuevo[y][x] = False
    tablero = nuevo
    print()
    for i in range(f):
        for j in range(c):
            if tablero[i][j]:
                print('*', end='')
            else:
                print('-',end='')
        print()
            
