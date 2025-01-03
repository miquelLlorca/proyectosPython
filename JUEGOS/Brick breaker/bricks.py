import pygame
from classes import *


NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

dimensiones = [1000,1000]
g = Game(dimensiones, 20)


pygame.init()
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Brick breaker")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a or evento.key == pygame.K_LEFT:
                g.racket.move = -1
            if evento.key == pygame.K_d or evento.key == pygame.K_RIGHT:
                g.racket.move = 1
            
            if(not g.started):
                g.Throw()
                
        
        if evento.type == pygame.KEYUP:
            g.racket.move = 0

    # ---------------------------------------------------LÓGICA---------------------------------------------------
    
    g.Update()

    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(NEGRO)

    for b in g.bricks:
        pygame.draw.rect(pantalla, b.color, [b.pos.x, b.pos.y, g.tam, g.tam])

    for b in g.balls:
        pygame.draw.ellipse(pantalla, BLANCO, [b.pos.x, b.pos.y, g.tam, g.tam])

    pygame.draw.line(pantalla, BLANCO, [g.racket.pos.x-g.racket.tam, g.racket.pos.y], [g.racket.pos.x+g.racket.tam, g.racket.pos.y], 5)

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
