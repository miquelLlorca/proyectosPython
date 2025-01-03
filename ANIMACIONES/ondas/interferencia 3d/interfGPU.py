import pygame
import numpy as np
from multiprocessing.sharedctypes import Value, Array
import os
import signal
from time import sleep


AMPMAX = 3
dimensiones = [1000,1000]
res = 2

class Onda:
    def __init__(self, x, y, w, k):
        self.x0 = x
        self.y0 = y
        self.w = w
        self.k = k

    def distancia(self, xi, yi):
        return ((self.x0 - xi)**2 + (self.y0 - yi)**2)**0.5


    def calcularZ(self, xi, yi, t):
        return np.sin(self.w*t - self.k*self.distancia(xi, yi))


def calculaColor(z):
    return (int(255*abs(z)/AMPMAX), int(255*abs(z)/AMPMAX), int(255*abs(z)/AMPMAX))

def calculaPos(i):
    return i%int(dimensiones[0]/res), int(i/int(dimensiones[0]/res))

NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)



length = int(dimensiones[0]/res * dimensiones[1]/res)
plano = Array('d', range(length))

for i in range(length):
    plano[i] = 0.0

t = 0

ondas = [
    Onda(200, 200, 0.1, 0.03),
    Onda(200, 800, 0.1, 0.03),
    Onda(800, 800, 0.1, 0.03),
    Onda(800, 200, 0.1, 0.03)
]
'''
ondas = [
    Onda(500, 200, 0.1, 0.05),
    Onda(800, 800, 0.1, 0.05),
    Onda(200, 800, 0.1, 0.05)
]'''
AMPMAX = len(ondas)


pygame.init()

pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Ondas")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

    # ---------------------------------------------------LÓGICA---------------------------------------------------
    
    rx = int(length/4)

    if(os.fork()):
        if(os.fork()):
            if(os.fork()): # padre
                for i in range(0, rx):
                    x, y = calculaPos(i)
                    plano[i] = ondas[0].calcularZ(x*res, y*res, t)
                
                for o in range(1, len(ondas)):
                    for i in range(0, rx):
                        x, y = calculaPos(i)
                        plano[i] += ondas[o].calcularZ(x*res, y*res, t)

            else: # hijo 3
                for i in range(rx*3, rx*4):
                    x, y = calculaPos(i)
                    plano[i] = ondas[0].calcularZ(x*res, y*res, t)
                
                for o in range(1, len(ondas)):
                    for i in range(rx*3, rx*4):
                        x, y = calculaPos(i)
                        plano[i] += ondas[o].calcularZ(x*res, y*res, t)

                os.kill(os.getpid(), signal.SIGKILL)


        else: # hijo 2
            for i in range(rx*2, rx*3):
                    x, y = calculaPos(i)
                    plano[i] = ondas[0].calcularZ(x*res, y*res, t)
            
            for o in range(1, len(ondas)):
                for i in range(rx*2, rx*3):
                    x, y = calculaPos(i)
                    plano[i] += ondas[o].calcularZ(x*res, y*res, t)

            os.kill(os.getpid(), signal.SIGKILL)


    else: # hijo 1
        for i in range(rx, rx*2):
            x, y = calculaPos(i)
            plano[i] = ondas[0].calcularZ(x*res, y*res, t)
        
        for o in range(1, len(ondas)):
            for i in range(rx, rx*2):
                x, y = calculaPos(i)
                plano[i] += ondas[o].calcularZ(x*res, y*res, t)

        os.kill(os.getpid(), signal.SIGKILL)

    os.wait()
    os.wait()
    os.wait()
    
    t += 1
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(BLANCO)

    for i in range(length):
        x, y = calculaPos(i)
        pygame.draw.rect(pantalla, calculaColor(plano[i]), [x*res, y*res, res, res])
    
    pygame.display.flip()
    reloj.tick(30)

pygame.quit()
