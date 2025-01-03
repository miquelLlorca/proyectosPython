import pygame
import random
import numpy as np
import math
pi = math.pi

def PointsInCircum(r,n=100):
    return [(-math.cos(2*pi/n*x)*r,-math.sin(2*pi/n*x)*r) for x in range(0,n+1)]

NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)


lns = []

n = int(input("Resolucion: "))
op = int(input("Modo (1-curva, 2-animacion): "))

if(op==1):
    m = int(input("Curva: "))
else:
    m = 1

puntos = PointsInCircum(450, n)
dly = 0
color = (0, 0, 0)
i=0
ctr = 500

pygame.init()
dimensiones = [1000,1000]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Cardioid")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

    # ---------------------------------------------------LÓGICA---------------------------------------------------
    if(op==2 and dly == 0):
        m += 0.005
        print(m)
        if(abs(m - int(m))<0.005):
            dly += 1
            #color = (255, 0, 0)
    elif(0<dly<10):
        dly += 1
    elif(dly==10):
        dly = 0
        color = (0, 0, 0)
    
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill((150, 150, 150))

    for i in range(len(puntos)):
        pygame.draw.ellipse(pantalla, NEGRO, [puntos[i][0]+ctr, puntos[i][1]+ctr, 5, 5])
        if(len(puntos) != len(lns)):
            lns.append([[puntos[i][0]+ctr, puntos[i][1]+ctr],
                         [puntos[int((i*m)%len(puntos))][0]+ctr, puntos[int((i*m)%len(puntos))][1]+ctr]])
        pygame.draw.line(pantalla, color, [puntos[i][0]+ctr, puntos[i][1]+ctr],
                         [puntos[int((i*m)%len(puntos))][0]+ctr, puntos[int((i*m)%len(puntos))][1]+ctr])
        
    pygame.display.flip()
    reloj.tick(40)

pygame.quit()






    
