import pygame
 
NEGRO = (0, 0 ,0)
GRIS = (155, 155, 155)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

dimensiones = [700,700]
t = 10
f = int(dimensiones[0]/t)
c = int(dimensiones[0]/t)
tablero = []
for i in range(f):
    tablero.append([False]*c)

# glider
'''
tablero[4][4] = True
tablero[3][3] = True
tablero[3][5] = True  
tablero[4][5] = True
tablero[5][4] = True
'''
# cosa random

cnt = int(f/2)
tablero[cnt][cnt] = True
tablero[cnt-1][cnt] = True
tablero[cnt][cnt-1] = True
tablero[cnt][cnt+1] = True
tablero[cnt+1][cnt-1] = True

# cosa random simetrica
'''
cnt = int(f/2)
tablero[cnt][cnt] = True
tablero[cnt-1][cnt] = True
tablero[cnt+1][cnt] = True
tablero[cnt][cnt+1] = True
tablero[cnt-1][cnt+2] = True
tablero[cnt+1][cnt+2] = True
'''

pygame.init()
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Conway's game of life")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

    # ---------------------------------------------------LÓGICA---------------------------------------------------
    nuevo = []
    for i in range(f):
        nuevo.append([False]*c)
        
    for y in range(f):
        for x in range(c):
            n = 0
            if y>0 and x>0 and tablero[y-1][x-1]:
                n+=1
            if x>0 and tablero[y][x-1]:
                n+=1
            if y<f-1 and x>0 and tablero[y+1][x-1]:
                n+=1
            if y>0 and tablero[y-1][x]:
                n+=1
            if y<f-1 and tablero[y+1][x]:
                n+=1
            if y>0 and x<c-1 and tablero[y-1][x+1]:
                n+=1
            if x<c-1 and tablero[y][x+1]:
                n+=1
            if y<f-1 and x<c-1 and tablero[y+1][x+1]:
                n+=1

            if tablero[y][x] and (n==2 or n==3):
                nuevo[y][x] = True
            elif not tablero[y][x] and n==3:
                nuevo[y][x] = True
            else:
                nuevo[y][x] = False
    tablero = nuevo
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(NEGRO)
    for i in range(f+1):
        pygame.draw.line(pantalla, GRIS, [0, i*t], [dimensiones[0], i*t], 1)
        pygame.draw.line(pantalla, GRIS, [i*t, 0], [i*t, dimensiones[1]], 1)
        
    for i in range(f):
        for j in range(c):
            if(tablero[i][j]):
                pygame.draw.rect(pantalla, VERDE, [i*t+1, j*t+1, t-2, t-2])
    
    pygame.display.flip()
    reloj.tick(10)

pygame.quit()
