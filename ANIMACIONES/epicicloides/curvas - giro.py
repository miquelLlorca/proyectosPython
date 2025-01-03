import pygame
import random
import math
import numpy as np

class Linea():
    def __init__(self, c, r, ang): 
        self.a = [c[0] + r * np.sin(np.radians(ang)), c[1] + r * np.cos(np.radians(ang))]
        self.b = [c[0] + r * np.sin(np.radians(ang+180)), c[1] + r * np.cos(np.radians(ang+180))]
        self.r = r
        self.c = c
        self.ang = ang

    def rotarCtr(self, dA):
        self.ang += dA
        self.a = [self.c[0] + self.r * np.sin(np.radians(self.ang)), self.c[1]
                  + self.r * np.cos(np.radians(self.ang))]
        self.b = [self.c[0] + self.r * np.sin(np.radians(self.ang+180)), self.c[1]
                  + self.r * np.cos(np.radians(self.ang+180))]

    
    
pi = math.pi

def PointsInCircum(r,n=100):
    return [(-math.cos(2*pi/n*x)*r +500,-math.sin(2*pi/n*x)*r +500) for x in range(0,n+1)]

def instrucciones():
    print("c -> cambio curva")
    print("r -> cambio resolucion")
    
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

instrucciones()

r = 400 # radio
n = 100 # resolucion
puntos = PointsInCircum(r, n)
m = 3/2# curva
lns = []
a = m*360

for i in range(len(puntos)):
    a -=  m*360/n
    l = Linea(puntos[i], r/m, a)
    lns.append(l)

cambio = 0
signo = 0

pygame.init()
dimensiones = [1000,1000]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Epicicloide")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_KP_PLUS:
                signo = 1
            if evento.key == pygame.K_KP_MINUS:
                signo = -1
            if evento.key == pygame.K_r:
                cambio = 'r'
            if evento.key == pygame.K_c:
                cambio = 'c'
                
    # ---------------------------------------------------LÓGICA---------------------------------------------------

    if(signo != 0):
        if(cambio == 'r'): # cambio  resolucion
            if(n==1 and signo == -1):
                dn = 0
            elif(n==1 and signo == 1):
                dn = 2
            elif(1< n <=5):
                dn = 2
            elif(5< n <=50):
                dn = 5
            elif(50< n <=500):
                dn = 50
            else:
                dn = 100
            
            n += dn * signo # resolucion
            puntos = PointsInCircum(r, n)
            lns = []
            a = m*360

            for i in range(len(puntos)):
                a -=  m*360/n
                l = Linea(puntos[i], r/m, a)
                lns.append(l)
            signo = 0
            
        if(cambio == 'c'): # curva
            m += signo * 1/2# curva
            lns = []
            a = m*360

            for i in range(len(puntos)):
                a -=  m*360/n
                l = Linea(puntos[i], r/m, a)
                lns.append(l)
            signo = 0
        
    
    for i in range(len(puntos)):
        lns[i].rotarCtr(2)

    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill((150, 150, 150))

    for i in range(len(puntos)):
        pygame.draw.ellipse(pantalla, NEGRO, [puntos[i][0], puntos[i][1], 5, 5])
        pygame.draw.line(pantalla, NEGRO, lns[i].a, lns[i].b, 2)



    
    pygame.display.flip()
    reloj.tick(30)

pygame.quit()
