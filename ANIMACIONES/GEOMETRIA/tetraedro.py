import pygame
import random
from numpy import sin, cos, radians

class Punto:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

r = 200

dx = r*sin(radians(30))
dy = r*cos(radians(30))

puntos = [Punto(0, 0, r), 
        Punto(-dy, 0, -dx), Punto(dx, -dy, - dx), Punto(dx, dy, -dx)]


c = Punto(300, 300, 300)
ang = radians(1)

aristas = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]
              


pygame.init()
dimensiones = [600,600]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Tetraedro")
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
                          p.y*cos(ang)-p.z*sin(ang),
                          p.y*sin(ang)+p.z*cos(ang))
    
    for i in range(len(puntos)): # giro y
        p = puntos[i]
        puntos[i] = Punto(p.x*cos(ang)-p.z*sin(ang),
                          p.y,
                          p.x*sin(ang)+p.z*cos(ang))
    
    for i in range(len(puntos)): # giro z
        p = puntos[i]
        puntos[i] = Punto(p.x*cos(ang)-p.y*sin(ang),
                          p.x*sin(ang)+p.y*cos(ang),
                          p.z)
    
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(BLANCO)

    for a in aristas:
        p1 = [c.x + puntos[a[0]-1].x, c.y + puntos[a[0]-1].y]
        p2 = [c.x + puntos[a[1]-1].x, c.y + puntos[a[1]-1].y]
        pygame.draw.line(pantalla, NEGRO, p1, p2, 2)

    for i in range(4):
        pygame.draw.ellipse(pantalla, NEGRO, [c.x + puntos[i].x-2, c.y + puntos[i].y-2, 6, 6])
    
    pygame.display.flip()
    reloj.tick(30)

pygame.quit()
