import pygame
import random
from numpy import sin, cos, radians

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

puntos = [Punto(-100, -100), Punto(-100, 100), Punto(100, 100), Punto(100, -100)]
c = Punto(300, 300)

pygame.init()
dimensiones = [600,600]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("cuadrado")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

    # ---------------------------------------------------LÓGICA---------------------------------------------------
    a = radians(1)
    for i in range(len(puntos)):
        p = puntos[i]
        puntos[i] = Punto(p.x*cos(a)-p.y*sin(a), p.x*sin(a)+p.y*cos(a))
    #({p.x*cos(i)-p.y*sen(i),p.x*sen(i)+p.y*cos(i)});

    
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(BLANCO)

    for i in range(-1, 3):
        pygame.draw.line(pantalla, NEGRO, [c.x + puntos[i].x, c.y + puntos[i].y],
                         [c.x + puntos[i+1].x, c.y + puntos[i+1].y], 2)

    for i in range(4):
        pygame.draw.ellipse(pantalla, NEGRO, [c.x + puntos[i].x-2, c.y + puntos[i].y-2, 6, 6])
    
    pygame.display.flip()
    reloj.tick(30)

pygame.quit()
