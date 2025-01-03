import pygame
import random
import numpy as np

class triangulo:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def drawT(self):
        pygame.draw.polygon(pantalla, VERDE, [self.A, self.B, self.C], 1)

    def creadef(self):
        d = [(self.A[0] + self.C[0])/2, (self.A[1] + self.C[1])/2]
        e = [(self.A[0] + self.B[0])/2, (self.A[1] + self.B[1])/2]
        f = [(self.B[0] + self.C[0])/2, (self.B[1] + self.C[1])/2]
        return [d, e, f]
    
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

a = [50, 950]
b = [950, 950]
c = [a[0]+900*np.cos(np.radians(60)),
         a[1]-900*np.sin(np.radians(60))]

ts = []
t = triangulo(a, b, c)
ts.append(t)


pygame.init()
dimensiones = [1000, 1000]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Mi Primer juego en Informática")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_KP_PLUS:
                nts = []
                for i in range(len(ts)):
                    nps = ts[i].creadef()
                    nts.append(triangulo(ts[i].A, nps[0], nps[1]))
                    nts.append(triangulo(ts[i].B, nps[2], nps[1]))
                    nts.append(triangulo(ts[i].C, nps[0], nps[2]))

                ts = nts + []

    # ---------------------------------------------------LÓGICA---------------------------------------------------
  
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill((50, 50, 50))

    for t in ts:
        t.drawT()
        
        
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
