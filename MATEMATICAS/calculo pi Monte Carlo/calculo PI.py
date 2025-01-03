import pygame
import random
from os import system 

NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)


total = 0
aciertos = 0
puntos = []


pygame.init()
dimensiones = [1000, 1000]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Calculo PI")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

    # ---------------------------------------------------LÓGICA---------------------------------------------------
    i = 0
    while(i<100):
        p = [random.randrange(0, 1000), random.randrange(0, 1000)]
        
        if(len(puntos) == 5000):
            puntos.pop(0)
        puntos.append(p)
        total += 1
        d = ( (p[0]-500)**2 + (p[1]-500)**2 )**0.5
        aciertos += 1 if d<500 else 0
        i += 1

    system("clear")
    print("iter:", total)
    print(4*aciertos/total)
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill((150, 150, 150))

    pygame.draw.ellipse(pantalla, NEGRO, [0, 0, 1000, 1000], 2)

    for p in puntos:
        pygame.draw.ellipse(pantalla, NEGRO, [p[0]-3, p[1]-3, 6, 6])
        pygame.draw.ellipse(pantalla, ROJO, [p[0]-2, p[1]-2, 4, 4])



    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
