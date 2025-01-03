import pygame
import random
import numpy as np

NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)


class Circulo:
    def __init__(self, centro, radio):
        self.c = centro
        self.r = radio
        self.radios = []
        self.angulo = 0

    def Incrementa(self):
        x = self.c[0] + self.r * np.cos(np.radians(self.angulo))
        y = self.c[1] + self.r * np.sin(np.radians(self.angulo))
        self.radios.append([x, y])
        self.angulo += 161.803


    def Draw(self, pantalla):
        for p in self.radios:
            pygame.draw.line(pantalla, NEGRO, self.c, p, 1)
        pygame.draw.ellipse(pantalla, NEGRO, [self.c[0]-5, self.c[1]-5, 10, 10])
        pygame.draw.ellipse(pantalla, NEGRO, [self.c[0]-self.r, self.c[1]-self.r, self.r*2, self.r*2], 3)




###############################################################################################################################


dimensiones = [1000,1000]
circulo = Circulo([500, 500], 500)



pygame.init()
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Numero Aureo")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

    # ---------------------------------------------------LÓGICA---------------------------------------------------

    circulo.Incrementa()

    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(BLANCO)

    circulo.Draw(pantalla)

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
