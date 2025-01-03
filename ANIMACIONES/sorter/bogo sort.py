import pygame
import random

NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)



def drawMat(M, dimensiones):
    pantalla.fill(NEGRO)
    



def creaMat(n, max):
    M = []
    v = 0
    dv = int(max/n)
    for i in range(n):
        M.append(v)
        v += dv

    for i in range(n):
        a = random.randint(0, n-1)
        b = random.randint(0, n-1)

        aux = M[a]
        M[a] = M[b]
        M[b] = aux
        

    return M
            
    

dimensiones = [1500, 1000]
n = 2
M = creaMat(n, dimensiones[1] - 100)
FR = 8
color = BLANCO
wait = 3
data = [0]


pygame.init()
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Bogo Sort")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

    # ---------------------------------------------------LÓGICA---------------------------------------------------
    
    data[len(data)-1] += 1
    sorted = True
    for i in range(n-1):
        if(M[i]>M[i+1]):
            sorted = False
            break
    
    if(sorted):
        FR = 1
        color = VERDE
        wait -= 1
        if(wait == 0):
            n *= 2
            M = creaMat(n, dimensiones[1] - 100)
            wait = 3
            FR = 8 if n <= 8 else 10000
            color = BLANCO
            data.append(0)
            print(data)
    else:
        FR = 8
        color = BLANCO
        for i in range(int(n/2)):
            a = random.randint(0, n-1)
            b = random.randint(0, n-1)

            aux = M[a]
            M[a] = M[b]
            M[b] = aux



    # ---------------------------------------------------DIBUJO---------------------------------------------------
    pantalla.fill((100, 100, 100))

    dx = (dimensiones[0]-50 - 5*(n-1))/len(M)
    for i in range(n):
        x0 = 25 + i*(dx+5)
        y0 = dimensiones[1] - 50 - M[i]
        dy = M[i]

        pygame.draw.rect(pantalla, color, [x0, y0, dx, dy])

    pygame.display.flip()
    reloj.tick(FR)

pygame.quit()
