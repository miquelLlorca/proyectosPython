import pygame
import random
from Radial import *


NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
FONDO = (200, 200, 200)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)


def RestaPuntos(pos, r, l):
    return [pos[i] - r[i]*l for i in [0, 1]]

def SumaPuntos(pos, r, l):
    return [pos[i] + r[i]*l for i in [0, 1]]



class Hojas:
    def __init__(self, dim, n, af):
        self.dim = dim + []
        self.hs = []
        for i in range(n):
            self.hs.append([random.randint(0, dim[0]), random.randint(0, dim[1])])

        self.n = n
        self.act_func = af

    def Actualiza(self, centro, vel, rango):

        for i in range(self.n):
            h = self.hs[i]
            radio = centro.GetRadioPos(h)
            dist = centro.GetDistancia(h)

            v = vel/dist if dist < rango else 0
            self.hs[i] = self.act_func(h, radio, v)


        for i in range(self.n):
            if(not(0 < self.hs[i][0] < self.dim[0]) or not(0 < self.hs[i][1] < self.dim[1])):
                self.hs.pop(i)
                self.hs.insert(i, [random.randint(0, self.dim[0]), random.randint(0, self.dim[1])])
            

        return

    def Draw(self, pantalla):
        for h in self.hs:
            pygame.draw.ellipse(pantalla, NEGRO, [h[0]-5, h[1]-5, 10, 10])


dimensiones = [1800, 1000]
centro = Radial([500, 500])
hojas = Hojas(dimensiones, 3000, SumaPuntos)

pygame.init()
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Soplador")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

    # ---------------------------------------------------LÓGICA---------------------------------------------------
    pos = pygame.mouse.get_pos()
    centro.c = pos
    hojas.Actualiza(centro, vel=5000, rango=500)

    #radioN = centro.GetRadioNeg(pos)
    #radioP = centro.GetRadioPos(pos)
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(FONDO)

    #pygame.draw.line(pantalla, NEGRO, pos, RestaPuntos(pos, radioN, 50), 5)
    #pygame.draw.line(pantalla, ROJO,  pos, RestaPuntos(pos, radioP, 50), 5)

    pygame.draw.ellipse(pantalla, NEGRO, [centro.c[0]-50, centro.c[1]-50, 100, 100])
    hojas.Draw(pantalla)

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
