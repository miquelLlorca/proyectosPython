import pygame
import random
import numpy as np

NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)


def GeneraPuntos(x, y, n):
    p1 = []
    p2 = []

    for i in range(n):
        punto = [random.randrange(x), random.randrange(y)]
        p1.append(punto.copy())
        p2.append(punto.copy())

    return p1, p2


def TransformaPunto(p, escala, origen, rotacion, dimensiones):
    dX = dimensiones[0]/2
    dY = dimensiones[1]/2

    # se mueve el punto para rotar respecto al centro de la nube de puntos
    x = p[0]-dX 
    y = p[1]-dY

    # se aplica la rotacion
    X = x*np.cos(np.radians(rotacion)) - y*np.sin(np.radians(rotacion))
    Y = x*np.sin(np.radians(rotacion)) + y*np.cos(np.radians(rotacion))

    # se mueve el punto a donde toca
    X += origen[0] + dX
    Y += origen[1] + dY
    
    # se escala 
    X *= escala
    Y *= escala

    return X, Y
# ===============================================================================================

origen = [0,0]
escala = 1
rotacion = 0
moverOrigen = False
shift = False

dimensiones = [1000, 1000]
pOrig, pMod = GeneraPuntos(dimensiones[0], dimensiones[1], 8000)


pygame.init()

pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Puntos")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

        if evento.type == pygame.MOUSEBUTTONDOWN:
            moverOrigen = True
            pos1 = pygame.mouse.get_pos()
        if evento.type == pygame.MOUSEBUTTONUP:
            moverOrigen = False

        elif evento.type == pygame.KEYDOWN:
            if not shift and evento.key == pygame.K_r:
                rotacion += 1
            if evento.key == pygame.K_KP_PLUS:
                escala -= escala*0.1
            if evento.key == pygame.K_KP_MINUS:
                escala += escala*0.1

            if evento.key == pygame.K_LSHIFT:
                shift = not shift
            if shift and evento.key == pygame.K_r:
                rotacion -= 1

        elif evento.type == pygame.KEYUP:
            time = 1

    # ---------------------------------------------------LÓGICA---------------------------------------------------
    
    if(moverOrigen):
        pos2 = pygame.mouse.get_pos()

        origen[0] += (pos2[0] - pos1[0])*escala**-1
        origen[1] += (pos2[1] - pos1[1])*escala**-1

        pos1 = pos2


    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill((150, 150, 150))
    
    for p in pOrig:
        pygame.draw.rect(pantalla, NEGRO, [p[0], p[1], 5, 5])

    for p in pOrig:
        x, y = TransformaPunto(p, escala, origen, rotacion, dimensiones)
        pygame.draw.rect(pantalla, NEGRO, [x, y, 5, 5])



    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
