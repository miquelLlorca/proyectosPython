import pygame
import numpy as np
from time import sleep

NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

##########################################################################################################################################

def GetGradient(a, b, n):
    gradient = []
    diff = [(b[i]-a[i])/n for i in range(3)]
    for i in range(1,n+1):
        gradient.append([int(a[j]+diff[j]*i) for j in range(3)])
    return gradient

def GetBigGradient(cols, n):
    nc = len(cols)-1
    gradient = []
    for i in range(nc):
        gradient += GetGradient(cols[i], cols[i+1], int(n/nc)+1)
    return gradient


class Piece:
    def __init__(self, id, color):
        self.id = id
        self.color = color   


class Tablero:
    def __init__(self, x, y, n, cols):
        self.pantalla = None

        self.x = x
        self.y = y
        self.n = n
        self.t = int(x/n)

        self.pieces = []
        gradient = GetBigGradient(cols, n)
        for i in range(n):
            self.pieces.append(Piece(i, gradient[i]))


    def AddScreen(self, pantalla):
        self.pantalla = pantalla


    def Randomize(self,pasos):
        for i in range(pasos):
            a = np.random.randint(0,n)
            b = np.random.randint(0,n)

            aux = self.pieces[a]
            self.pieces[a] = self.pieces[b]
            self.pieces[b] = aux
            self.Draw()
        return

    def Sort(self, type):
        if(type == "insert"):
            self.insertSort()
        if(type == "select"):
            self.selSort()


    def insertSort(self):
        swaps = 1
        while(swaps != 0):
            swaps = 0
            for i in range(self.n-1):
                if(self.pieces[i].id > self.pieces[i+1].id):
                    aux = self.pieces[i]
                    self.pieces[i] = self.pieces[i+1]
                    self.pieces[i+1] = aux
                    swaps += 1
                    self.Draw()
        return

    
    def selSort(self):
        pos = 0
        while(pos<self.n):
            menor = pos
            for i in range(pos, len(self.pieces)):
                if(self.pieces[i].id<self.pieces[menor].id):
                    menor = i

            aux = self.pieces[pos]
            self.pieces[pos] = self.pieces[menor]
            self.pieces[menor] = aux
            self.Draw()
            pos += 1

        return 


    def Draw(self):
        
        for i in range(self.n):
            pygame.draw.rect(self.pantalla, self.pieces[i].color, [i*self.t, 0, self.t, self.y])
        print(i*self.t)
        pygame.display.flip()
        reloj.tick(FR)
        return


##########################################################################################################################################

FR = 100
n = 500
dimensiones = [1500,500]
cols = [
    (255,   0,   0),
    (255, 255,   0),
    (  0, 255, 255),
    (  0,   0, 255),
    (255,   0, 255)
]
tablero = Tablero(dimensiones[0], dimensiones[1], n, cols)
print(len(tablero.pieces))
sorter = "select"

pygame.init()
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Rainbow sort")
hecho = False
reloj = pygame.time.Clock()


tablero.AddScreen(pantalla)

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                tablero.Randomize(500)
                sleep(0.5)
                tablero.Sort(sorter)
    # ---------------------------------------------------LÓGICA---------------------------------------------------

    # ---------------------------------------------------DIBUJO---------------------------------------------------

    tablero.Draw()


pygame.quit()
