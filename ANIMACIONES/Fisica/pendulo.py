import pygame
import sympy as sm
import numpy as np

def calculo(d, a):
    # ang = amax * sen(g/d*t)
    i=0
    ang = [1, 2, 3]
    t = 0
    #abs(ang[len(ang)-1] - ang[len(ang)-2])> 0.001
    while(t<100):
        arg = (9.8/d * t)**0.5 
        angulo = a* np.sin(arg)
        print(angulo, '  -  ', arg)
        ang.append(np.radians(angulo))
        t += 1/60
        a -= 0.001

    for i in range(3):
        ang.pop(2-i)

    return ang

NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

origen = [250, 250]
d = 150
ang = 45
x = 0
y = 0
m = 0.1
g = 9.8
listAng = calculo(d, ang)
pos = 0

print(np.sin(90))
pygame.init()
dimensiones = [500,500]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Pendulo")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

    # ---------------------------------------------------LÓGICA---------------------------------------------------
    

    x = np.sin(listAng[pos]) * d
    y = abs(np.cos(listAng[pos])) * d
    if(pos+1 == len(listAng)):
        pos=0
    else:
        pos+=1
    
    # ---------------------------------------------------DIBUJO---------------------------------------------------
    
    pantalla.fill(BLANCO)

    pygame.draw.line(pantalla, NEGRO, [origen[0], origen[1]], [origen[0]+x, origen[1]+y], 2)
    pygame.draw.ellipse(pantalla, NEGRO, [origen[0]+x-20, origen[1]+y-20, 40, 40], 1)
    
    pygame.display.flip()
    reloj.tick(120)

pygame.quit()
