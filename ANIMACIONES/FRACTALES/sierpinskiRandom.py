import pygame
import random
import numpy as np

NEGRO = (0,0,0)


def GetHalfPoint(a, b):
    diff = [(b[i]-a[i])/2 for i in range(2)]
    return [a[i]+diff[i] for i in range(2)]


puntos = []
lastPoint = [-1,-1]
done = False



pygame.init()
dimensiones = [1000, 1000]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Sierpinski random")
hecho = False
reloj = pygame.time.Clock()

pantalla.fill((150, 150, 150))
pygame.display.flip()
while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                puntos = []
                lastPoint = [-1,-1]
                done = False
                pantalla.fill((150, 150, 150))
                pygame.display.flip()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if(len(puntos) < 3):
                puntos.append(pos)
            elif(not done):
                lastPoint = pos
                pygame.draw.ellipse(pantalla, NEGRO, [lastPoint[0], lastPoint[1], 1, 1])
                done = True

    # ---------------------------------------------------LÓGICA---------------------------------------------------
    if(done):
        r = np.random.randint(0,3)
        lastPoint = GetHalfPoint(lastPoint, puntos[r])
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    if(lastPoint != [-1,-1]):
        pygame.draw.ellipse(pantalla, NEGRO, [lastPoint[0], lastPoint[1], 1, 1])

    if(not done):
        for p in puntos:
            pygame.draw.ellipse(pantalla, NEGRO, [p[0], p[1], 5, 5])

    
        
        
    pygame.display.flip()
    reloj.tick(1000)

pygame.quit()
