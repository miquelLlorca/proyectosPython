import pygame
import random
import numpy as np

NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)
  


dimensiones = [1800,1000]
centro = [x/2 for x in dimensiones]
ang = random.randint(30, 330)
while(not (30 <= ang%90 <= 60)):
    ang = random.randint(30, 330)
#vB = [np.cos(ang), np.sin(ang)]
angs = []
angs.append(ang)

pygame.init()
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("pong")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

    # ---------------------------------------------------LÓGICA---------------------------------------------------
    ang = random.randint(20, 340)
    while(not (20 <= ang%90 <= 70)):
        ang = random.randint(20, 340)

    angs.append(ang)

    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(NEGRO)

    for ang in angs:
        pygame.draw.line(pantalla, BLANCO, centro, [centro[0]+np.cos(np.radians(ang))*1000, centro[1]+np.sin(np.radians(ang))*1000], 1)

    pygame.display.flip()
    reloj.tick(6000)

pygame.quit()
