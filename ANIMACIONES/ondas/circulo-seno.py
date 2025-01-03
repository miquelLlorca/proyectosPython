import pygame
import numpy as np


class Linea:
    def __init__(self, a, d, ang):
        self.a = a
        self.b = [a[0] + d * np.cos(np.radians(ang)), a[1] - d * np.sin(np.radians(ang))]
        self.d = d
        self.ang =  ang



NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)


dimensiones = [1000,600]
onda1 = []
onda2 = []
r = Linea((100, 100), 75, 45)


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

    r = Linea((100, 100), 75, r.ang+1)
    onda1.insert(0, r.b[1])
    onda2.insert(0, 200-r.b[0] + 200)

    if(len(onda1) > dimensiones[0]-198):
        onda1.pop(len(onda1)-1)
        onda2.pop(len(onda2)-1)
        
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill((150, 150, 150))

    # cirrculo y ondas
    
    pygame.draw.ellipse(pantalla, NEGRO, [25, 25, 150, 150], 5) # circulo
    pygame.draw.ellipse(pantalla, NEGRO, [99, 99, 4, 4]) # centro c
    pygame.draw.line(pantalla, VERDE, r.a, r.b, 3) #radio
    pygame.draw.line(pantalla, ROJO, r.b, [200, r.b[1]], 3) #dx
    pygame.draw.line(pantalla, AZUL, r.b, [r.b[0], 200], 3) #dy
    pygame.draw.arc(pantalla, AZUL, [200 - (200-r.b[0]), 200 - (200-r.b[0]), (200-r.b[0])*2, (200-r.b[0])*2+2], np.radians(180), np.radians(270), 3) # arco dy

    pygame.draw.line(pantalla, NEGRO, [100, 100], [dimensiones[0], 100], 1) # eje 1
    pygame.draw.line(pantalla, NEGRO, [200, 300], [dimensiones[0], 300], 1) # eje 2
    pygame.draw.line(pantalla, NEGRO, [100, 100], [100, 200], 1) # eje v2
    pygame.draw.arc(pantalla, NEGRO, [100, 100, 200, 201], np.radians(180), np.radians(270), 1) # arco eje 2
    
    pygame.draw.line(pantalla, NEGRO, [200, 0], [200, 800], 3) #sep v
    
    pygame.draw.line(pantalla, NEGRO, [0, 200], [dimensiones[0], 200], 3) # sep h1
    pygame.draw.line(pantalla, NEGRO, [0, 400], [dimensiones[0], 400], 3) # sep h2


    for i in range(len(onda1)-1):
        pygame.draw.line(pantalla, ROJO, [200+i, onda1[i]], [201+i, onda1[i+1]], 3) # onda 1
        pygame.draw.line(pantalla, AZUL, [200+i, onda2[i]], [201+i, onda2[i+1]], 3) # onda 2


    # ondas al cuadrado  

    for i in range(len(onda1)-1):
        o12 = 425 + 150*(((onda1[i] - 100) / 75)**2)
        o22 = 575 - 150*(((onda2[i] - 300) / 75)**2)  
        pygame.draw.line(pantalla, ROJO, [200+i, 425], [200+i, o12], 1) # onda1^2
        pygame.draw.line(pantalla, AZUL, [200+i, o22], [200+i, 575], 1) # onda2^2

    pygame.draw.line(pantalla, NEGRO, [200, 425], [dimensiones[0], 425], 2) # ss1
    pygame.draw.line(pantalla, NEGRO, [200, 575], [dimensiones[0], 575], 2) # ss2

    
    pygame.display.flip()
    reloj.tick(120)

pygame.quit()












