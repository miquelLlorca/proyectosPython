
import pygame
import numpy as np
 
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

dimensiones = [1800,1000]
onda1 = []
onda2 = []
ondaT = []
res = 1
for i in range(int(dimensiones[0]/res)):
    onda1.append([i*res, dimensiones[1]/4])
    onda2.append([i*res, dimensiones[1]/2])
    ondaT.append([i*res, 3*dimensiones[1]/4])

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
        
    # y = amp * sin( omega*t  -  lambda*x) 
    


    for i in range(len(onda1)):
        onda1[i][1] =   dimensiones[1]/4 + 20*np.sin( 0.05*t - 0.02*i)
        onda2[i][1] =   dimensiones[1]/2 + 75*np.sin( 0.01*t - 0.01*i)
        ondaT[i][1] = 3*dimensiones[1]/4 + 20*np.sin( 0.05*t - 0.02*i) + 75*np.sin( 0.01*t - 0.01*i)



    '''
    # para el calculo x siempre es 0

    onda1.pop(len(onda1)-1)
    onda1.insert(0, [-1, dimensiones[1]/4 + 20*np.sin(   0.05*t )])

    onda2.pop(len(onda2)-1)
    onda2.insert(0, [-1, dimensiones[1]/2 + 75*np.sin( 0.01*t )])

    ondaT.pop(len(ondaT)-1)
    ondaT.insert(0, [-1, 3*dimensiones[1]/4 + 75*np.sin( 0.01*t ) + 20*np.sin(   0.05*t )])

    for i in range(len(onda1)):
        onda1[i][0] += 1
        onda2[i][0] += 1
        ondaT[i][0] += 1

    '''
    t += 1
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill((150, 150, 150))
    
    for i in range(len(onda1)- 1):
        pygame.draw.line(pantalla, NEGRO, onda1[i], onda1[i+1], 5)
        pygame.draw.line(pantalla, NEGRO, onda2[i], onda2[i+1], 5)
        pygame.draw.line(pantalla, NEGRO, ondaT[i], ondaT[i+1], 5)

    pygame.draw.line(pantalla, NEGRO, [0,   dimensiones[1]/4], [dimensiones[0],   dimensiones[1]/4], 1)
    pygame.draw.line(pantalla, NEGRO, [0,   dimensiones[1]/2], [dimensiones[0],   dimensiones[1]/2], 1)
    pygame.draw.line(pantalla, NEGRO, [0, 3*dimensiones[1]/4], [dimensiones[0], 3*dimensiones[1]/4], 1)

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
