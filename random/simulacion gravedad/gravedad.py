import pygame
import random
from clases import Masa, Vector, Plano, Punto


NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

origen = [0,0]
escala = 1
time = 1
stopTime = True
moverOrigen = False
plano = Plano([Masa(5, Punto(500, 500), Vector(), 5)])

m1 = Masa(1, Punto(200, 200), Vector(d = 100, ang = 90), 1)
m2 = Masa(2, Punto(300, 300), Vector(d = 100, ang = 45), 2)
m3 = Masa(2, Punto(800, 800), Vector(d = 100, ang = 180), 2)

pygame.init()
dimensiones = [1000, 1000]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Gravedad")
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
            if evento.key == pygame.K_KP_PLUS:
                escala -= escala*0.1
            if evento.key == pygame.K_KP_MINUS:
                escala += escala*0.1
            if evento.key == pygame.K_SPACE:
                stopTime = not stopTime
            if evento.key == pygame.K_RETURN: # esto no va xd
                time = -1

        elif evento.type == pygame.KEYUP:
            time = 1

    # ---------------------------------------------------LÓGICA---------------------------------------------------
    
    if(moverOrigen):
        pos2 = pygame.mouse.get_pos()

        origen[0] += (pos2[0] - pos1[0])*escala**-1
        origen[1] += (pos2[1] - pos1[1])*escala**-1

        pos1 = pos2
        print(origen)

    if(not stopTime):
        #plano.Update(1/60)
        m1.Move(plano, time * 1/30)
        m2.Move(plano, time * 1/30)
        #m3.Move(plano, 1/30)

    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(NEGRO)
    
    for m in plano.Ms:
        pygame.draw.ellipse(pantalla, BLANCO, [(origen[0]+m.pos.x - 10)*escala, (origen[1]+m.pos.y - 10)*escala, 20, 20], 3)

    pygame.draw.ellipse(pantalla, BLANCO, [(origen[0]+m1.pos.x - 10)*escala, (origen[1]+m1.pos.y - 10)*escala, 20, 20], 3)
    pygame.draw.line(   pantalla,  VERDE, [(origen[0]+m1.pos.x)*escala,      (origen[1]+m1.pos.y)*escala], 
                                          [(origen[0]+m1.pos.x + m1.g.x*10)*escala, (origen[1]+m1.pos.y + m1.g.y*10)*escala], 5)

    pygame.draw.ellipse(pantalla, BLANCO, [(origen[0]+m2.pos.x - 10)*escala, (origen[1]+m2.pos.y - 10)*escala, 20, 20], 3)
    pygame.draw.line(   pantalla,  VERDE, [(origen[0]+m2.pos.x)*escala,      (origen[1]+m2.pos.y)*escala], 
                                          [(origen[0]+m2.pos.x + m2.g.x*10)*escala, (origen[1]+m2.pos.y + m2.g.y*10)*escala], 5)

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
