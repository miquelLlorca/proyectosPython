import pygame
import sympy as sm
import numpy as np

class Pieza:
    def __init__(self, x, y, tipo, tam):
        self.x = int(x/10)
        self.y = int(y/10)
        self.type = tipo
        self.l = int(tam/10)
        self.v = 0
    
    def update(self, yMax):
        dy = self.v*(1/60) + 10*0.5*9.81*(1/60)**2
        if(self.y + self.l + dy < yMax):
            self.y += dy
            self.v += 10*9.81*(1/60)
        else:
            self.y = yMax-self.l
            self.v = 0

    def draw(self):
        if(self.type == 'c'):
            pygame.draw.rect(pantalla, NEGRO, [self.x*10, self.y*10, self.l*10, self.l*10], 2)


NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

pick = False
selected = False
p = Pieza(100, 100, 'c', 50)



pygame.init()
dimensiones = [800,800]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Gravedad")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pick = True
        if evento.type == pygame.MOUSEBUTTONUP:
            selected = False
    # ---------------------------------------------------LÓGICA---------------------------------------------------
    x, y = pygame.mouse.get_pos()
    
    if(pick):
        dx = x - p.x*10
        dy = y - p.y*10
        if(dx>=0 and dx<p.l*10 and dy>=0 and dy<p.l*10):
            selected = True
            pick = False
            p.v = 0 
        
    if(selected):
        p.x = int((x-dx)/10)
        p.y = int((y-dy)/10)

    p.update(int(dimensiones[1]/10))
   
    # ---------------------------------------------------DIBUJO---------------------------------------------------
    
    pantalla.fill(BLANCO)

    p.draw()

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
