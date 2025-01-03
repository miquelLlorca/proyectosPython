import pygame
import random
import numpy as np
import math
pi = math.pi


class Linea():
    def __init__(self, c, r, ang): 
        self.a = [c[0] + r * np.sin(np.radians(ang)), c[1] + r * np.cos(np.radians(ang))]
        self.b = [c[0] + r * np.sin(np.radians(ang+180)), c[1] + r * np.cos(np.radians(ang+180))]
        self.r = r
        self.c = c
        self.ang = ang
        self.p = [c[0] + np.cos(ang), c[1] + np.sin(ang)]

    def moverP(self, dP):
        direc = 1
        if(self.p[0] + direc*dP*np.cos(self.ang) > self.a[0]):
            direc = -1
        
        self.p[0] += direc*dP*np.cos(self.ang)
        self.p[1] += direc*dP*np.sin(self.ang)

NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)


c = [350, 350]
lns = []
n = 16
for i in range(int(n/2)):
    lns.append(Linea(c, 300, i*(360/n)))
    

pygame.init()
dimensiones = [700,700]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("jaja xd lol")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

    # ---------------------------------------------------LÓGICA---------------------------------------------------

    for l in lns:
        l.moverP(1)
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill((150, 150, 150))

    pygame.draw.ellipse(pantalla, NEGRO, [50, 50, 600, 600], 3)
    pygame.draw.ellipse(pantalla, NEGRO, [c[0]-4, c[0]-4, 8, 8])

    for l in lns:
        pygame.draw.line(pantalla, NEGRO, l.a, l.b, 1)
        pygame.draw.ellipse(pantalla, ROJO, [l.p[0]-6, l.p[1]-6, 12, 12])
    
    pygame.display.flip()
    reloj.tick(30)

pygame.quit()





    
