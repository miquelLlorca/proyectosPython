import pygame
import random
from numpy import sin, cos, radians
from Cubo import *




        
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

cubo = Cube(Point(200, 200, 200), 600, 3) # posicion, tamaño, n

#turns = [["R", 90], ["U", 90], ["!R", 90], ["!U", 90]]
rotar = [0, 0]



pygame.init()
dimensiones = [1000,1000]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("cubo")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a:
                rotar[1] += 1
            elif evento.key == pygame.K_d:
                rotar[1] += -1
            elif evento.key == pygame.K_w:
                rotar[0] += 1
            elif evento.key == pygame.K_s:
                rotar[0] += -1

        elif evento.type == pygame.KEYUP:
            rotar = [0, 0]

    # ---------------------------------------------------LÓGICA---------------------------------------------------
    
    #cubo.turn(turns)
    #cubo.rotate(rotar[0], rotar[1], 0)
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill((150, 150, 150))

    cubo.DrawSkeleton(pantalla, rotar)
    
    pygame.display.flip()
    reloj.tick(30)

pygame.quit()
