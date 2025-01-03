import pygame
import random
from numpy import sin, cos, radians

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def ToArray(self):
        return [self.x, self.y]

class Cuadrado:
    def __init__(self, pos, tam, n):
        self.pos = pos
        self.tam = tam
        self.n = n
        self.puntos = []

        for i in range(n):
            for j in range(n):
                self.puntos.append(Punto(pos.x+i*tam/(n-1), pos.y+j*tam/(n-1)))

    




NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

cuad = Cuadrado(Punto(100, 100), 800, 2)

pygame.init()
dimensiones = [1000,1000]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("cuadrado")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_PLUS:
                cuad = Cuadrado(Punto(100, 100), 800, cuad.n + 1)


    # ---------------------------------------------------LÓGICA---------------------------------------------------
    
    
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill((150, 150, 150))

    for p1 in cuad.puntos:
        #pygame.draw.ellipse(pantalla, NEGRO, [p1.x-5, p1.y-5, 10, 10])
        for p2 in cuad.puntos:
            pygame.draw.line(pantalla, NEGRO, p1.ToArray(), p2.ToArray(), 2)

    pygame.display.flip()
    reloj.tick(30)

pygame.quit()
