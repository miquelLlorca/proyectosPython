import pygame
import random

def drawMat(M, dimensiones):
    pantalla.fill(NEGRO)
    for i in range(len(M)):
        x0 = 20 +i*(dimensiones[0]-40)/len(M)+1
        xf = (dimensiones[0]-40)/len(M)-2
        y0 = dimensiones[1] - 20
        yf = -(M[i]/len(M) *(dimensiones[1]-40))
        pygame.draw.rect(pantalla, BLANCO, [x0, y0, xf, yf])
        
def selSort(M):
    pos = 0
    sec = []
    sec.append(M)
    while(pos<len(M)):
        menor = pos
        for i in range(pos, len(M)):
            if(M[i]<M[menor]):
                menor = i

        aux = M[pos]
        M[pos] = M[menor]
        M[menor] = aux

        pos += 1

        sec.append(M+[])
    return sec


def insertSort(M):
    swaps = 1
    sex = []
    while(swaps != 0):
        swaps = 0
        for i in range(len(M)-1):
            if(M[i] > M[i+1]):
                aux = M[i]
                M[i] = M[i+1]
                M[i+1] = aux
                swaps += 1
                sec.append(M+[])
    return sec


def mySortxd(M):
    sec = []
    swaps = 1
    while(swaps != 0):
        swaps = 0
        for i in range(len(M)):
            if(M[i] != i+1):
                aux = M[i]
                M[i] = M[aux-1]
                M[aux-1] = aux
                swaps += 1
                sec.append(M+[])
    return sec


def creaMat(t):
    M = []

    for i in range(t):
        M.append(None)
        
    for i in range(1, t+1):
        done = False
        while(not done):
            x = random.randint(0,t-1)
            if(M[x] == None):
                done = True
                M[x] = i
    return M
            
    
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

sec = []
M = creaMat(75)
n = 1
FR = 10
pygame.init()
dimensiones = [700,500]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Mi Primer juego en Informática")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

    # ---------------------------------------------------LÓGICA---------------------------------------------------
    if(sec == []):
        if(n == 1):
            sec = selSort(M)
            n += 1
            FR = 10
        elif(n == 2):
            M = creaMat(75)
            sec = insertSort(M)
            FR = 90
            n += 1
        elif(n == 3):
            M = creaMat(100)
            sec = mySortxd(M)
            FR = 15
            n += 1
            
    # ---------------------------------------------------DIBUJO---------------------------------------------------
    if(sec != []):
        drawMat(sec[0], dimensiones)
        sec.pop(0)
        if(sec==[]):
            FR = 1
    pygame.display.flip()
    reloj.tick(FR)

pygame.quit()
