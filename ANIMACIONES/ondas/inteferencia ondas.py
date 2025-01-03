import pygame
import numpy as np
 
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

dimensiones = [1600,1000]
eje = dimensiones[1]/2
onda = []
res = 1
for i in range(int(dimensiones[0]/res)):
    onda.append([i*res, dimensiones[1]/2])

bs = [0.05, 0.01, 0.001]

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
    
    a = 0.1
    
    amp = 150
    for i in range(len(onda)):
        onda[i][1] = 0
        for b in bs:
            onda[i][1] += amp*np.sin(a*t + b*onda[i][0])
        onda[i][1] += eje



    t += 1
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(NEGRO)

    for i in range(len(onda)- 1):
        pygame.draw.line(pantalla, BLANCO, onda[i], onda[i+1], 3)
        
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
