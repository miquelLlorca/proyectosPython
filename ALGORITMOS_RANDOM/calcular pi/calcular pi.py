import pygame
import random
import numpy as np

d = 25

class Linea():
    def __init__(self, p0, ang):
        self.p0 = p0
        self.pf = [p0[0]+np.cos(ang)*d, p0[1]+np.sin(ang)*d]

def randPos(dimensiones):
    return [random.randint(0, dimensiones[0]), random.randint(0, dimensiones[1])]

def randAng():
    return random.randint(0, 360)


NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

a = 50
lineas = 0
DIVS = []
dimensiones = [900,700]
for i in range(int(dimensiones[1]/a + 1)):
    DIVS.append(i*a)

cortes = 0

pygame.init()

pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("calcular pi")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

    # ---------------------------------------------------LÓGICA---------------------------------------------------

    lin = Linea(randPos(dimensiones), randAng())
    lineas += 1

    for n in DIVS:
        c1 = lin.p0[1] < n and lin.pf[1] > n
        c2 = lin.p0[1] > n and lin.pf[1] < n 
        
        if(c1 or c2):
            cortes += 1

    if(lineas%100==0):
        p = 2*d*lineas/(a*cortes)
        
        print("Iteraciones:", lineas, ", PI =", p)
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(BLANCO)
    for n in DIVS:
        pygame.draw.line(pantalla, NEGRO, [0, n], [dimensiones[0], n], 3)

    pygame.draw.line(pantalla, NEGRO, lin.p0, lin.pf, 1)
        
    pygame.display.flip()
    reloj.tick(500)

pygame.quit()
