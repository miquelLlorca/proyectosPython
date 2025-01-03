import pygame
import random
from numpy import sin, cos, radians

edges = [[1, 2], [2, 3], [3, 4], [4, 1],
                      [1, 5], [2, 6], [3, 7], [4, 8],
                      [5, 6], [6, 7], [7, 8], [8, 5]]


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Cubie:
    def __init__ (self, pos, t):
        self.t = t
        self.v = [Point(pos.x,   pos.y,   pos.z),   Point(pos.x+t, pos.y,   pos.z), 
                  Point(pos.x+t, pos.y+t, pos.z),   Point(pos.x,   pos.y+t, pos.z),
                  Point(pos.x,   pos.y,   pos.z+t), Point(pos.x+t, pos.y,   pos.z+t), 
                  Point(pos.x+t, pos.y+t, pos.z+t), Point(pos.x,   pos.y+t, pos.z+t)]

    def rotate(self, rx, ry, rz, c): # rota un cubo respecto a c
        for i in range(8): # mueve el cubo hacia el centro de rotacion
            p = self.v[i]
            self.v[i] = Point(p.x-c.x, p.y-c.y, p.z-c.z)

        if(rx != 0):
            for i in range(8): # giro x
                p = self.v[i]
                self.v[i] = Point(p.x,
                                p.y*cos(rx) - p.z*sin(rx),
                                p.y*sin(rx) + p.z*cos(rx))

        if(ry != 0):
            for i in range(8): # giro y
                p = self.v[i]
                self.v[i] = Point(p.x*cos(ry) - p.z*sin(ry),
                                p.y,
                                p.x*sin(ry) + p.z*cos(ry))

        if(rz != 0):
            for i in range(8): # giro z
                p = self.v[i]
                self.v[i] = Point(p.x*cos(rz) - p.y*sin(rz),
                                p.x*sin(rz) + p.y*cos(rz),
                                p.z)
                             
        for i in range(8): # devuelve el cubo a su pos original
            p = self.v[i]
            self.v[i] = Point(p.x+c.x, p.y+c.y, p.z+c.z)



class Cube:
    def __init__(self, pos, tam, n):
        self.n = n
        self.pos = pos
        self.cubies = []
        self.tam = tam
        self.tC = tam/n
        self.c = Point(self.pos.x + self.tam/2, self.pos.y + self.tam/2, self.pos.z + self.tam/2)

        self.U = []
        self.D = []
        self.R = []
        self.L = []
        self.F = []
        self.B = []

        for i in range(n):
            self.cubies.append([])
            for j in range(n):
                self.cubies[i].append([])
                for l in range(n):
                    self.cubies[i][j].append(Cubie(Point(pos.x + self.tC*i, pos.y + self.tC*j, pos.z + self.tC*l), self.tC))

                    if(i == 0):
                        self.U.append([i, j, l]) # ------ EJE X
                    elif(i == n-1):
                        self.D.append([i, j, l])

                    if(j == 0):
                        self.R.append([i, j, l]) # ------ EJE Y
                    elif(j == n-1):
                        self.L.append([i, j, l])

                    if(l == 0):
                        self.F.append([i, j, l]) # ------ EJE Z
                    elif(l == n-1):
                        self.B.append([i, j, l])
        

    def rotate(self, rx, ry, rz):
        for i in range(self.n):
            for j in range(self.n):
                for l in range(self.n):
                    self.cubies[i][j][l].rotate(radians(rx), radians(ry), radians(rz), self.c)

    def turn_R(self, turns):
        if(turns[0][1] > 0):
            sentido = 1
            if(turns[0][0] == "!R"):
                sentido = -1

            for i in range(self.n):
                for j in range(self.n):
                    for l in range(self.n):
                        if([i, j, l] in self.R):
                            self.cubies[i][j][l].rotate(0, sentido*radians(1), 0, self.c)

        turns[0][1] -= 1


        if(turns[0][1] == -15):
            turns.pop(0)

    def turn_U(self, turns):
        if(turns[0][1] > 0):
            sentido = 1
            if(turns[0][0] == "!U"):
                sentido = -1

            for i in range(self.n):
                for j in range(self.n):
                    for l in range(self.n):
                        if([i, j, l] in self.U):
                            self.cubies[i][j][l].rotate(0, sentido*radians(1), 0, self.c)

        turns[0][1] -= 1


        if(turns[0][1] == -15):
            turns.pop(0)


    def turn(self, turns):
        if("R" in turns[0][0]):
            self.turn_R(turns)
        elif(turns[0][0] == "U" or turns[0][0] == "!R"):
            self.turn_U(turns)


    def drawCube(self):
        cubo.rotate(0, -45, 0)
        cubo.rotate(-45, 0, 0)

        for i in range(self.n):
            for j in range(self.n):
                for l in range(self.n):
                    for e in edges:
                        p1 = [self.cubies[i][j][l].v[e[0]-1].x, self.cubies[i][j][l].v[e[0]-1].y]
                        p2 = [self.cubies[i][j][l].v[e[1]-1].x, self.cubies[i][j][l].v[e[1]-1].y]
                        pygame.draw.line(pantalla, NEGRO, p1, p2, 2)
        
        cubo.rotate(+45, 0, 0)
        cubo.rotate(0, +45, 0)

        
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

cubo = Cube(Point(200, 200, 200), 600, 3) # posicion, tamaño, n

turns = [["R", 90], ["U", 90], ["!R", 90], ["!U", 90]]




pygame.init()
dimensiones = [1000,1000]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("cubo")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

    # ---------------------------------------------------LÓGICA---------------------------------------------------
    
    cubo.turn(turns)
    #cubo.rotate(0.01, 1, 0)
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill((150, 150, 150))

    cubo.drawCube()
    
    pygame.display.flip()
    reloj.tick(30)

pygame.quit()
