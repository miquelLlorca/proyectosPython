import pygame
import sys


NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)


t = int(sys.argv[1])
res = int(1000/t)
tablero = []

pygame.init()
dimensiones = [res*t, res*t]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("PATHFIND")
hecho = False
reloj = pygame.time.Clock()


while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

    # ---------------------------------------------------LÓGICA---------------------------------------------------
    inp = open('tablero.txt', 'r')
    lineas = inp.readlines()
    inp.close()

    if(lineas != []):
        tablero = []
        for linea in lineas:
            tablero.append([])
            for c in linea:
                tablero[len(tablero)-1].append(c)
 

    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill((150, 150, 250))
    
    if(tablero != []):
        for i in range(t):
            for j in range(t):
                col = 0
                if(tablero[i][j] == 'I'):
                    col = (0, 255, 0)
                elif(tablero[i][j] == 'F'):
                    col = (255, 0, 0)
                elif(tablero[i][j] == 'X'):
                    col = (50, 50, 50)
                elif(tablero[i][j] == '_'):
                    col = (200, 200, 200)
                elif(tablero[i][j] == 'o'):
                    col = (150, 150, 250)

                pygame.draw.rect(pantalla, col, [i*res, j*res, res, res])

    pygame.display.flip()
    reloj.tick(4)

pygame.quit()
