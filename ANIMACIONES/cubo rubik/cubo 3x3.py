import pygame
import random
from numpy import sin, cos, radians

class Punto:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Cubo:
    def __init__ (self, pos, t, c):
        self.t = t
        self.c = c
        self.v = [Punto(pos.x, pos.y, pos.z), Punto(pos.x+t, pos.y, pos.z), Punto(pos.x+t, pos.y+t, pos.z), Punto(pos.x, pos.y+t, pos.z),
                Punto(pos.x, pos.y, pos.z+t), Punto(pos.x+t, pos.y, pos.z+t), Punto(pos.x+t, pos.y+t, pos.z+t), Punto(pos.x, pos.y+t, pos.z+t)]


        
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

cols = [(0, 0, 0), (0, 255, 0), (255, 0, 0),
        (0, 0, 255), (255, 255, 0), (0, 255, 255),
        (255, 0, 255), (255, 255, 255), (126, 200, 42)]
esc = 2
cubos = []
t = 100

p0 = int(-(t*3)/2)
p = Punto(p0, p0, p0)

for i in range(3):
    for j in range(3):
        for l in range(3):

            cubos.append(Cubo(Punto(p.x + i*t, p.y + j*t, p.z + l*t), t, cols[i+j+l]))



c = Punto(800, 800, 800)
ang = radians(0.5)

aristas = [[1, 2], [2, 3], [3, 4], [4, 1],
               [1, 5], [2, 6], [3, 7], [4, 8],
               [5, 6], [6, 7], [7, 8], [8, 5]]


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
    for C in cubos:

        for i in range(8): # giro x
            p = C.v[i]
            C.v[i] = Punto(p.x,
                            p.y*cos(-ang)-p.z*sin(-ang),
                            p.y*sin(-ang)+p.z*cos(-ang))

        for i in range(8): # giro y
            p = C.v[i]
            C.v[i] = Punto(p.x*cos(ang)-p.z*sin(ang),
                            p.y,
                            p.x*sin(ang)+p.z*cos(ang))

        for i in range(8): # giro z
            p = C.v[i]
            C.v[i] = Punto(p.x*cos(-ang)-p.y*sin(-ang),
                            p.x*sin(-ang)+p.y*cos(-ang),
                            p.z)
    
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill((150, 150, 150))

    for C in cubos:
        for a in aristas:
            p1 = [esc*p0 + c.x + esc*C.v[a[0]-1].x, esc*p0 + c.y + esc*C.v[a[0]-1].y]
            p2 = [esc*p0 + c.x + esc*C.v[a[1]-1].x, esc*p0 + c.y + esc*C.v[a[1]-1].y]
            pygame.draw.line(pantalla, C.c, p1, p2, 5)

        for i in range(8):
            pygame.draw.ellipse(pantalla, C.c, [esc*p0 + c.x + esc*C.v[i].x-2, esc*p0 + c.y + esc*C.v[i].y-2, 6, 6])
    
    pygame.display.flip()
    reloj.tick(30)

pygame.quit()
