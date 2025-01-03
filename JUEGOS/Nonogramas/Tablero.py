import pygame

def drawCursor(x, y, v, pantalla):
    if(v == 1):
        c = (0, 0, 0)
    else:
        c = (255, 255, 255)
    
    ps = [[0, 0],
          [0, 20],
          [5, 15],
          [7, 20],
          [8, 19],
          [7, 14],
          [10, 14]]
    
    for p in ps:
        p[0] += x
        p[1] += y

    outline = 0
    if(v == -1): outline = 1

    pygame.draw.polygon(pantalla, c, ps, outline)



class Tablero:

    def __init__(self, t):
        self.t = t
        self.xs = []
        self.ys = []

        self.tablero = []

        for i in range(t):
            self.tablero.append([])
            for j in range(t):
                self.tablero[i].append(0)

    def draw(self, res, p):
        for i in range(self.t):
            for j in range(self.t):
                if(self.tablero[i][j] == 1):
                    pygame.draw.rect(p, (50, 50, 50), [i*res, j*res, res, res])

                elif(self.tablero[i][j] == 0):
                    pygame.draw.rect(p, (200, 200, 200), [i*res, j*res, res, res])

                elif(self.tablero[i][j] == -1):
                    pygame.draw.rect(p, (200, 200, 200), [i*res, j*res, res, res])
                    pygame.draw.line(p, (50, 50, 50), [i*res, j*res], [(i+1)*res, (j+1)*res], 3)
                    pygame.draw.line(p, (50, 50, 50), [(i+1)*res, j*res], [i*res, (j+1)*res], 3)

        for i in range(self.t):
            pygame.draw.line(p, (255, 255, 255), [i*res, 0], [i*res, self.t*res])
            pygame.draw.line(p, (255, 255, 255), [0, i*res], [self.t*res, i*res])


    def calcularXY(self):
        self.xs = []
        self.ys = []

        for i in range(self.t):
            self.xs.append([0])
            for v in self.tablero[i]:
                if(self.xs[i][len(self.xs[i])-1]>0 and v == 0):
                    self.xs[i].append(0)
                if(v == 1):
                    self.xs[i][len(self.xs[i])-1] += 1


        for i in range(self.t):
            self.ys.append([0])
            for v in self.tablero[:][i:i+1][0]:
                if(self.ys[i][len(self.ys[i])-1]>0 and v == 0):
                    self.ys[i].append(0)
                if(v == 1):
                    self.ys[i][len(self.ys[i])-1] += 1


    def guardar(self):
        
        self.calcularXY()

        nextName = open("Niveles/nextName.txt", 'r') # se busca el nuevo nombre
        levelName = int(nextName.readline())
        nextName.close()


        level = open("Niveles/"+str(levelName)+".txt", 'w') # se guarda el nivel
        level.write(str(self.t)+"\n")
        for i in range(self.t):
            linea = ""
            for v in self.xs[i]:
                linea += str(v)
                linea += " "
            linea += "\n"
            level.write(linea)
        
        for i in range(self.t):
            linea = ""
            for v in self.ys[i]:
                linea += str(v)
                linea += " "
            linea += "\n"
            level.write(linea)
        level.close()


        levelName = str(int(levelName) + 1) # se actualiza el nombre y se guarda
        nextName = open("Niveles/nextName.txt", 'w')
        nextName.write(levelName)
        nextName.close()


    def equals(self, xs, ys):
        self.calcularXY()
        return self.xs == xs and self.ys == ys

    def set(self, x, y, v):
        self.tablero[x][y] = v




