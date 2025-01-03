
import pygame
from random import randrange
import numpy as np

N = 120

class Hormiga():
    
    def __init__(self, x, y, v, c, eC, eH, cN):         
        super().__init__()
 
        self.x = x
        self.y = y
        self.v = v
        self.c = c
        self.cN = 0
        if(c[0] == 255 and c[1] == 0):
            self.cN == 0 # rojo
        elif(c[1] == 255 and c[0] == 0):
            self.cN == 1 # verde
        elif(c[0] == 255 and c[1] == 255):
            self.cN == 2 # amarillo
        elif(c[2] == 255):
            self.cN == 3 # azul
            
        self.eC = eC
        self.eH = eH

    def dib(self):
        x = self.x
        y = self.y
        pygame.draw.ellipse(pantalla, (0,0,0), [x-4, y-4, 8, 8], 2) 
        pygame.draw.ellipse(pantalla, self.c, [x+1-4, y+1-4, 6, 6]) 

    def updatePos(self):
        self.x += self.v[0]
        self.y += self.v[1]
        
        if(self.x>=496 or self.x <= 4):
            self.v[0] *= -1
            
        if(self.y>=496 or self.y <= 4):
            self.v[1] *= -1
     

    def updateCol(self):
        while(len(self.eC) > N/20):
            self.eC.pop(0)
            self.eH.pop(0)
            
        cs = [0, 0, 0, 0]
        for i in range(len(self.eC)):
            if(self.cN == 0):
                cs[0] += 1
            elif(self.cN == 1):
                cs[1] += 1
            elif(self.cN == 2):
                cs[2] += 1
            elif(self.cN == 3):
                cs[3] += 1

        tot = cs[0] + cs[1] + cs[2] + cs[3]

        r = 0
        m = 10000000
        for i in range(4):
            if(cs[i]<m):
                r = i
                m = cs[i]
                
        if(r == 0):
            self.c = (255, 0, 0)
        elif(r == 1):
            self.c = (0, 255, 0)
        elif(r == 2):
            self.c = (255, 255, 0)
        elif(r == 3):
            self.c = (0, 0, 255)
            
        self.cN = r
            
                
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
GRIS = (150, 150, 150)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)


hormigas = []
cs = [ROJO, VERDE, AZUL, AMARILLO]
for i in range(N): # crear bloques
    ang = randrange(0, 360)
    vel = [np.sin(ang), np.cos(ang)]
    h = Hormiga(randrange(10, 490), randrange(10, 490), vel, cs[i%4], [], [], 0)
    hormigas.append(h)


pygame.init()
dimensiones = [500,500]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Comportamiento emergente")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        if evento.type == pygame.KEYDOWN:
            if(evento.key == pygame.K_f): # matar rojos ajaj xd lol
                x = 0
                cs = [AMARILLO, VERDE, AZUL]
                for i in range(int(len(hormigas)/4), len(hormigas)):
                    if(i%4 == 0):
                        h = hormigas[i]
                        hormigas[i] = Hormiga(h.x, h.y, h.v, cs[x%3], h.eC, h.eH, 0)
                        x += 1
                    
    # ---------------------------------------------------LÓGICA---------------------------------------------------
    cs = [0, 0, 0, 0] # contador
    for i in range(len(hormigas)): # movimiento y contador de trbajos
        hormigas[i].updatePos()

        if(hormigas[i].c[2] == 255):
            cs[0] += 1
        elif(hormigas[i].c[1] == 255 and hormigas[i].c[0] == 0):
            cs[1] += 1 
        elif(hormigas[i].c[0] == 255 and hormigas[i].c[1] == 0):
            cs[2] += 1
        elif(hormigas[i].c[1] == 255 and hormigas[i].c[0] == 255):
            cs[3] += 1

    print("R, G, B, Y -> {}, {}, {}, {}".format(cs[2], cs[1], cs[0], cs[3]))


    for i in range(len(hormigas)):
        for j in range(len(hormigas)):
            if(i != j):
                if(((hormigas[i].x - hormigas[j].x)**2 + (hormigas[i].y - hormigas[j].y)**2)**0.5 < 10):   
                    if(len(hormigas[i].eH) == 0 or len(hormigas[i].eH) > 0 and j != hormigas[i].eH[len(hormigas[i].eH)-1]):
                        hormigas[i].eH.append(j)
                        hormigas[i].eC.append(hormigas[j].cN)

    for i in range(len(hormigas)):
        if(len(hormigas[i].eC) > 10):
            hormigas[i].updateCol()
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(GRIS)
    
    
    for i in range(len(hormigas)): # dibuja hormigas y cuenta trabajos
        hormigas[i].dib()
        

    
        
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
