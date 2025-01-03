import pygame
import random
import numpy as np

NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)
  
# ==============================================================================================================================

class Tablero:
    def __init__(self, dimensiones, ia1=False, ia2=False):
        self.bola = [x/2 for x in dimensiones]
        self.dimensiones = dimensiones + []
        self.p1 = dimensiones[1]/2
        self.p2 = dimensiones[1]/2
        self.ia1 = ia1
        self.ia2 = ia2
        self.tam = 50 # *2 = tamaño de raqueta
        self.puntos = [0, 0]

        ang = random.randint(20, 340)
        while(not (20 <= ang%90 <= 70)):
            ang = random.randint(20, 340)
        self.vB = [np.cos(np.radians(ang)), np.sin(np.radians(ang))]


    def Restart(self):
        self.bola = [x/2 for x in self.dimensiones]
        self.p1 = self.dimensiones[1]/2
        self.p2 = self.dimensiones[1]/2

        ang = random.randint(20, 340)
        while(not (20 <= ang%90 <= 70)):
            ang = random.randint(20, 340)
        self.vB = [np.cos(np.radians(ang)), np.sin(np.radians(ang))]


    def Update(self, move1, move2):
        v = 10
        # mueve 1
        if(self.ia1):
            if(not (self.vB[0] > 0)):
                self.p1 += v if self.bola[1]>self.p1 else -v 
        else:
            self.p1 += move1*v if 20+self.tam <= self.p1+move1*v <= self.dimensiones[1]-20-self.tam else 0

        # mueve 2
        if(self.ia2):
            if(not (self.vB[0] < 0)):
                self.p2 += v if self.bola[1]>self.p2 else -v
        else:
            self.p2 += move2*v if 20+self.tam <= self.p2+move2*v <= self.dimensiones[1]-20-self.tam else 0


        # mueve la bola
        v = 10
        # se comprueba que no salga por el eje y
        if(30 <= self.bola[1]+v*self.vB[1] <= self.dimensiones[1]-30): 
            self.bola[1] += v*self.vB[1]
        else:
            self.bola[1] -= v*self.vB[1]
            self.vB[1] *= -1

        # se comprueban las raquetas y los puntos
        if(40 <= self.bola[0] <= 60):
            if(self.p1-self.tam <= self.bola[1] <= self.p1+self.tam): # golpea 1
                self.vB[0] *= -1
        elif(self.dimensiones[0]-40 <= self.bola[0] <= self.dimensiones[0]-60): # golpea 2
            if(self.p2-self.tam <= self.bola[1] <= self.p2+self.tam):
                self.vB[0] *= -1
        elif(self.bola[0] < 50): # punto para 1
            self.puntos[0] += 1
            self.Restart()
        elif(self.bola[0] > self.dimensiones[0]-50): # punto para 2
            self.puntos[1] += 1
            self.Restart()

        self.bola[0] += v*self.vB[0] 
        

        

        return 

    
    def Draw(self, pantalla):

        pygame.draw.rect(pantalla, NEGRO, [20, 20, self.dimensiones[0]-40, self.dimensiones[1]-40])
        pygame.draw.ellipse(pantalla, BLANCO, [self.bola[0]-10, self.bola[1]-10, 20, 20])

        pygame.draw.line(pantalla, BLANCO, [50, self.p1 + self.tam], [50, self.p1 - self.tam], 10)
        pygame.draw.line(pantalla, BLANCO, [self.dimensiones[0]-50, self.p2 + self.tam], [self.dimensiones[0]-50, self.p2 - self.tam], 10)


        return


# ==============================================================================================================================



dimensiones = [1800,1000]
tabl = Tablero(dimensiones, True, True)


pygame.init()
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("pong")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

    # ---------------------------------------------------LÓGICA---------------------------------------------------
    tabl.Update(1, 1)

    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(BLANCO)

    tabl.Draw(pantalla)

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
