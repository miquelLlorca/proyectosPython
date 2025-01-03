import pygame
import random
import numpy as np

def cuadrZ(z):
    m = z[0]**2 + z[1]**2
    
    if(z[0]==0 and z[1]>0):
        ang = 90
    elif(z[0]==0 and z[1]<0):
        ang = -90
    elif(z[0]==0 and z[1]==0):
        ang = 0
    else:
        ang = np.arctan(z[1]/z[0])*2
        
    return [m * np.cos(ang), m * np.sin(ang)]

def sumZ(z0, z1):
    return [z0[0] + z1[0], z0[1] + z1[1]]

def compZ(z0, z1):
    a = (z0[0]**2 + z0[1]**2)**0.5
    b = (z1[0]**2 + z1[1]**2)**0.5

    return a==b


def creaCol(c):
    z = [0, 0]
    s = []
    for i in range(100):
        zn =  sumZ(cuadrZ(z), c)

        s.append(compZ(zn, z))

        ln = len(s)
        if(i>25 and s[ln-5]==s[ln-4]==s[ln-3]==s[ln-2]==s[ln-1]):
            return (255, 255, 255)
        elif(i>25 and not(s[ln-5]==s[ln-4]==s[ln-3]==s[ln-2]==s[ln-1])):
            return (0,0,0)

        z = zn+[]
                



NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

#ts = [100, 50, 25, 20, 10, 5, 2, 1]
dimensiones = [800,800]
ct = [int(dimensiones[0]/2)+200, int(dimensiones[1]/2)]
tam = 10#ts[0]
cols = []

for i in np.arange(0, dimensiones[0], tam):
    cols.append([])
    for j in np.arange(0, dimensiones[1], tam):
        x = (i - ct[0])/300
        y = (j - ct[1])/300
        #print(x, y)
        cols[-1].append(creaCol([x, y]))


pygame.init()
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Mandelbrot")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

    # ---------------------------------------------------LÓGICA---------------------------------------------------
  
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(BLANCO)
    for i in range(len(cols)):
        for j in range(len(cols[0])):
            pygame.draw.rect(pantalla, cols[i][j], [i*tam, j*tam, tam, tam])
            
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
