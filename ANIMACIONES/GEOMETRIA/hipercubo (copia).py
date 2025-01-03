import pygame
import random
from numpy import sin, cos, radians

class Punto:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

        
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)


puntos = [Punto(-100, -100, -100, -100), Punto(-100, 100, -100, -100),
                Punto(100, 100, -100, -100), Punto(100, -100, -100, -100),
                Punto(-100, -100, 100, -100), Punto(-100, 100, 100, -100),
                Punto(100, 100, 100, -100), Punto(100, -100, 100, -100),
                Punto(-100, -100, -100, 100), Punto(-100, 100, -100, 100),
                Punto(100, 100, -100, 100), Punto(100, -100, -100, 100),
                Punto(-100, -100, 100, 100), Punto(-100, 100, 100, 100),
                Punto(100, 100, 100, 100), Punto(100, -100, 100, 100)]

c = Punto(300, 300, 300, 300)
ang = radians(1)

aristas = [[1, 2], [2, 3], [3, 4], [4, 1], # -----
               [1, 5], [2, 6], [3, 7], [4, 8], # cubo 1
               [5, 6], [6, 7], [7, 8], [8, 5], # -----
               [1+8, 2+8], [2+8, 3+8], [3+8, 4+8], [4+8, 1+8], #-----
               [1+8, 5+8], [2+8, 6+8], [3+8, 7+8], [4+8, 8+8], # cubo 2
               [5+8, 6+8], [6+8, 7+8], [7+8, 8+8], [8+8, 5+8], #-----
               [1, 9], [2, 10], [3, 11], [4, 12], # -------
               [5, 13], [6, 14], [7, 15], [8, 16]] # union


pygame.init()
dimensiones = [600,600]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("cubo")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

    # ---------------------------------------------------LÓGICA---------------------------------------------------

    
    for i in range(len(puntos)): # giro x
        p = puntos[i]
        puntos[i] = Punto(p.x,
                          p.y*cos(ang)-p.w*sin(ang),
                          p.z,
                          p.y*sin(ang)+p.w*cos(ang))

    for i in range(len(puntos)): # giro y
        p = puntos[i]
        puntos[i] = Punto(p.x*cos(ang)-p.z*sin(ang),
                          p.y,
                          p.x*sin(ang)+p.z*cos(ang),
                          p.w)
    
    for i in range(len(puntos)): # giro z
        p = puntos[i]
        puntos[i] = Punto(p.x*cos(ang)-p.y*sin(ang),
                          p.x*sin(ang)+p.y*cos(ang),
                          p.z,
                          p.w)
        
    for i in range(len(puntos)): # giro w
        p = puntos[i]
        puntos[i] = Punto(p.x*cos(ang)-p.w*sin(ang),
                          p.y,
                          p.z,
                          p.x*sin(ang)+p.w*cos(ang))
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(BLANCO)

    for a in aristas:
        p1 = [c.x + puntos[a[0]-1].x, c.y + puntos[a[0]-1].y]
        p2 = [c.x + puntos[a[1]-1].x, c.y + puntos[a[1]-1].y]
        pygame.draw.line(pantalla, NEGRO, p1, p2, 2)

    for i in range(16):
        pygame.draw.ellipse(pantalla, NEGRO, [c.x + puntos[i].x-2, c.y + puntos[i].y-2, 6, 6])
    
    pygame.display.flip()
    reloj.tick(30)

pygame.quit()
