import pygame
import numpy as np
from time import sleep


NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)


AMPMAX = 3
dimensiones = [1000,1000]
res = 10

SENO = np.array([np.sin(np.deg2rad(x)) for x in range(0, 360)])

class Onda:
    def __init__(self, x, y, w, k):
        self.x0 = x
        self.y0 = y
        self.w = w
        self.k = k

    def distancia(self, xi, yi):
        return ((self.x0 - xi)**2 + (self.y0 - yi)**2)**0.5


    def calcularZ(self, xi, yi, t):
        dist = self.distancia(xi, yi)

        if(dist < t*self.w/self.k):
            arg = int(np.rad2deg(self.w*t - self.k*dist))
            return SENO[arg%360]
        else:
            return 0
        return np.sin(self.w*t - self.k*self.distancia(xi, yi))





def calculaColor(z):
    return (int(255*abs(z)/AMPMAX), int(255*abs(z)/AMPMAX), int(255*abs(z)/AMPMAX))

def calculaPos(i):
    return i%int(dimensiones[0]/res), int(i/int(dimensiones[0]/res))



#for i in range(360):
#    print(SENO[i])





length = int(dimensiones[0]/res * dimensiones[1]/res)
W = int(dimensiones[0]/res)
H = int(dimensiones[1]/res)


plano = np.zeros((W, H))

t = 0


ondas = [
    Onda(500, 280, 0.1, 0.05),
    Onda(800, 800, 0.1, 0.05),
    Onda(200, 800, 0.1, 0.05)
]
'''
ondas = [
    Onda(500, 200, 0.1, 0.05),
    Onda(800, 800, 0.1, 0.05)
]

ondas = [
    Onda(0, 0, 0.1, 0.05),
    Onda(0, 1000, 0.1, 0.05)
]

'''
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
    

    for i in range(W):
        for j in range(H):
            plano[i][j] = ondas[0].calcularZ(i*res, j*res, t)
    
    for o in range(1, len(ondas)):
        for i in range(W):
            for j in range(H):  
                plano[i][j] += ondas[o].calcularZ(i*res, j*res, t)


    t += 1
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(BLANCO)

    for i in range(W):
        for j in range(H):
            pygame.draw.rect(pantalla, calculaColor(plano[i][j]), [i*res, j*res, res, res])
    
    pygame.image.save(pantalla, "framesOndas/frame"+str(t)+".png")
    pygame.display.flip()
    reloj.tick(30)

pygame.quit()
