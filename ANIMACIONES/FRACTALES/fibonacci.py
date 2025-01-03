import pygame
import numpy as np
from pygame import Rect

NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

PHI = 1.618034



class Cuadrante:
    def __init__(self, rect, rectCurva, orientacion):
        self.rect = rect
        self.rectCurva = rectCurva
        self.orientacion = orientacion

    
    def Draw(self, pantalla, origen, escala):
        r = Rect(origen[0]+self.rect.x*escala, origen[1]+self.rect.y*escala, self.rect.w*escala, self.rect.h*escala)
        pygame.draw.rect(pantalla, NEGRO, r, 1)
        a = 0
        b = 90
        if(self.orientacion == 1):
            a = 90
            b = 180
        elif(self.orientacion == 2):
            a = 0
            b = 90
        elif(self.orientacion == 3):
            a = -90
            b = 0
        elif(self.orientacion == 4):
            a = 180
            b = 270

        r = Rect(origen[0]+self.rectCurva.x*escala, origen[1]+self.rectCurva.y*escala, self.rectCurva.w*escala, self.rectCurva.h*escala)
        pygame.draw.arc(pantalla, NEGRO, r, np.radians(a), np.radians(b), 3)

        



class Fibonacci:
    def __init__(self, lado):
        self.tramos = [Cuadrante(Rect(0, 0, lado, lado), Rect(0, 0, lado*2, lado*2), 1)]
        self.n = 0
        self.origen = [0, 0]
        self.escala = 1


    def Escalar(self, dir):
        self.escala *= 10**dir
        self.origen[0] *= 10**dir
        self.origen[1] *= 10**dir


    def Mover(self, dx, dy):
        self.origen[0] += dx
        self.origen[1] += dy


    def Expandir(self):
        lastOri = self.tramos[self.n].orientacion
        prevTam = self.tramos[self.n].rect.w
        tam = prevTam * abs(1-PHI)

        if(lastOri == 1):
            r1 = Rect(self.tramos[self.n].rect.x+prevTam, self.tramos[self.n].rect.y, tam, tam)
            r2 = Rect(self.tramos[self.n].rect.x+abs(prevTam-tam), self.tramos[self.n].rect.y, tam*2, tam*2)
            self.tramos.append(Cuadrante(r1, r2, 2))
            
        elif(lastOri == 2):
            r1 = Rect(self.tramos[self.n].rect.x+abs(prevTam-tam), self.tramos[self.n].rect.y+prevTam, tam, tam)
            r2 = Rect(r1.x-tam, r1.y-tam, tam*2, tam*2)
            self.tramos.append(Cuadrante(r1, r2, 3))

        elif(lastOri == 3):
            r1 = Rect(self.tramos[self.n].rect.x-tam, self.tramos[self.n].rect.y+abs(prevTam-tam), tam, tam)
            r2 = Rect(r1.x, r1.y-tam, tam*2, tam*2)
            self.tramos.append(Cuadrante(r1, r2, 4))

        elif(lastOri == 4):
            r1 = Rect(self.tramos[self.n].rect.x, self.tramos[self.n].rect.y-tam, tam, tam)
            r2 = Rect(r1.x, r1.y, tam*2, tam*2)
            self.tramos.append(Cuadrante(r1, r2, 1))

        self.n += 1

    def Draw(self, pantalla):
        for t in self.tramos:
            t.Draw(pantalla, self.origen, self.escala)


# angulo empieza desde der y tira hacia arriba, antihorario


lado = 1000
dimensiones = [int(lado*PHI), lado]
mover = False
fib = Fibonacci(lado)

pygame.init()
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Fibonacci")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                fib.Expandir()
            if evento.key == pygame.K_PLUS:
                fib.Escalar(1)
            if evento.key == pygame.K_MINUS:
                fib.Escalar(-1)

        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            mover = True

        if evento.type == pygame.MOUSEBUTTONUP:
            oldPos = pos
            pos = pygame.mouse.get_pos()
            fib.Mover(pos[0]-oldPos[0], pos[1]-oldPos[1])
            mover = False
    # ---------------------------------------------------LÃGICA--------------------------------------------------

    if(mover):
        oldPos = pos
        pos = pygame.mouse.get_pos()
        fib.Mover(pos[0]-oldPos[0], pos[1]-oldPos[1])
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill((150, 150, 150))
    fib.Draw(pantalla)

    #pygame.draw.arc(pantalla, NEGRO, pygame.Rect(0, 0, 2000, 2000), np.radians(90), np.radians(180), 3)

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
