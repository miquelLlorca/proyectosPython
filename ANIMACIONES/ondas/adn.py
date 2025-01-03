
import pygame
import numpy as np
import random

NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)

dimensiones = [1000,500]
onda1 = []
onda2 = []
res = 1
for i in range(int(dimensiones[0]/res)):
    onda1.append([i*res, dimensiones[1]/2])
    onda2.append([i*res, dimensiones[1]/2])
t = 0

actg = []
res = 50
for i in range(int(dimensiones[0]/res + 2)):
    actg.append([i*res, random.choice(['a', 'c', 't', 'g'])]) # gc,  at


pygame.init()

pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("ADN")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

    # ---------------------------------------------------LÓGICA---------------------------------------------------
    eje = dimensiones[1]/2
    a = 0.1
    b = 0.01
    amp = 150
    for i in range(len(onda1)):
        onda1[i][1] = eje + amp*np.sin(a*t + b*onda1[i][0])
        onda2[i][1] = eje + amp*np.sin(a*t + b*onda2[i][0] + np.pi/1.5)

    for i in range(len(actg)):
        actg[i][0] -= 2
        if(actg[i][0] < 0):
            actg.pop(i)
            actg.append([actg[len(actg)-1][0]+res, random.choice(['a', 'c', 't', 'g'])])
        
    t += 0.3
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill((150, 150, 150))
    
    j = 0
    for i in range(len(onda1)- 1):
        
        if(onda1[i][0] == actg[j][0]):
            eje = (onda1[i][1] + onda2[i][1])/2
            if(actg[j][1] == 'a'):
                pygame.draw.line(pantalla, AZUL, onda1[i], [actg[j][0], eje], 5)
                pygame.draw.line(pantalla, VERDE, onda2[i], [actg[j][0], eje], 5)
            elif(actg[j][1] == 't'):
                pygame.draw.line(pantalla, VERDE, onda1[i], [actg[j][0], eje], 5)
                pygame.draw.line(pantalla, AZUL, onda2[i], [actg[j][0], eje], 5)
            elif(actg[j][1] == 'c'):
                pygame.draw.line(pantalla, AMARILLO, onda1[i], [actg[j][0], eje], 5)
                pygame.draw.line(pantalla, ROJO, onda2[i], [actg[j][0], eje], 5)
            elif(actg[j][1] == 'g'):
                pygame.draw.line(pantalla, ROJO, onda1[i], [actg[j][0], eje], 5)
                pygame.draw.line(pantalla, AMARILLO, onda2[i], [actg[j][0], eje], 5)

            j += 1
        pygame.draw.line(pantalla, NEGRO, onda1[i], onda1[i+1], 5)
        pygame.draw.line(pantalla, NEGRO, onda2[i], onda2[i+1], 5)

    pygame.display.flip()
    reloj.tick(30)

pygame.quit()
