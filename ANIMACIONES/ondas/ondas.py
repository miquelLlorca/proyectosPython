import pygame
import numpy as np
 
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

dimensiones = [1000,500]
onda = []
res = 1
for i in range(int(dimensiones[0]/res)):
    onda.append([i*res, dimensiones[1]/2])

t = 0


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
    eje = dimensiones[1]/2
    a = 0.1
    b = 0.05
        
    for i in range(len(onda)):
        x = (onda[i][0] - dimensiones[0]/2)
        if(x>-400 and x<400):
            amp = -0.000622*x**2 + 100 #
        else:
            amp = 0
        onda[i][1] = eje + amp*np.sin(a*t + b*onda[i][0])

    t += 1
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(BLANCO)

    for i in range(len(onda)- 1):
        pygame.draw.line(pantalla, NEGRO, onda[i], onda[i+1], 3)
        
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
