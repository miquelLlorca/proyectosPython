import pygame
import random
import numpy as np
from adaboost import *


NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

def LeerCFs():
    cf = []
    af = []
    file = open("t10.txt", "r")

    T = int(file.readline().split()[0])

    for i in range(10):
        cf.append([])
        af.append([])
        for j in range(T):
            cd = [int(x) for x in file.readline().split()]
            a = float(file.readline().split()[0])
            cf[i].append(cd)
            af[i].append(a)
    return cf, af



res = 25
dimensiones = [28*res + 200, 28*res]

imagen = np.zeros((28, 28))
solved = -1
pintar = False
CF, alphas = LeerCFs() 
anchoPincel = 1*res
eje = 28*res + 100
altoGraf = int(dimensiones[1]/10)+1

pygame.init()
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Adabooooost")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

        if evento.type == pygame.MOUSEBUTTONDOWN:
            pintar = True
            
        if evento.type == pygame.MOUSEBUTTONUP:
            pintar = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                imagen = np.zeros((28, 28))
                solved = -1

            if evento.key == pygame.K_s:
                solved, max, results = clasificar_imagen(CF, alphas, imagen.reshape(28*28))
                histograma = [x/max for x in results]

    # ---------------------------------------------------LÓGICA---------------------------------------------------
    
    if(pintar):
        pos = pygame.mouse.get_pos()
        posInt = [x//25 for x in pos]

        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                x = (posInt[0] + i + 0.5)*res
                y = (posInt[1] + j + 0.5)*res

                distancia = ( (pos[0]-x)**2 + (pos[1]-y)**2)**0.5

                color =  int(255*(1 - (distancia/2)/anchoPincel)) + imagen[posInt[1]+j][posInt[0]+i] 

                imagen[posInt[1]+j][posInt[0]+i] = 0 if color < 0 else ( color if color <= 255 else 255)





    if(solved != -1):
        print(solved, results)
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(BLANCO)

    for i in range(28):
        for j in range(28):
            pygame.draw.rect(pantalla, [imagen[j][i] for x in range(3)], [i*res, j*res, res, res])


    pygame.draw.line(pantalla, NEGRO, [eje, 0], [eje, 28*res], 1)


    if(solved != -1):
        for i in range(len(CF[solved])):
            x = CF[solved][i][0]%28
            y = CF[solved][i][0]//28
            pygame.draw.ellipse(pantalla, VERDE, [x*res+5, y*res+5, res-10, res-10], 5)
    
        for i in range(len(histograma)):
            h = histograma[i]
            if(h >= 0):
                pygame.draw.rect(pantalla, NEGRO, [eje, i*altoGraf, 100*h, altoGraf])
            elif(h < 0):
                pygame.draw.rect(pantalla, NEGRO, [eje-100*h, i*altoGraf, 100*h, altoGraf])

        print(histograma)
        #fuente = pygame.font.Font(None, 75)
        #txt = fuente.render(str(solved), True, (150, 150, 150))
        #pantalla.blit(txt, [0, dimensiones[1]-80])

    # pinta nums simper, cambia color
    pygame.display.flip()
    reloj.tick(10)

pygame.quit()
