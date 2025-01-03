import click
import pygame
import random
 
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

FONDO = (150, 150, 150)
FONDO_TABL = (0, 0, 155)
AMARILLO = (255, 255, 0)

'''
 o  o  o  o  o  o  o
 o  o  o  o  o  o  o
 o  o  o  o  o  o  o
 o  o  o  o  o  o  o
 o  o  o  o  o  o  o
 o  o  o  o  o  o  o

 7 x 6
 espacio + circulo + espacio
'''
c = 130
esp = 15
dimensiones = [7*(esp*2 + c), 6*(esp*2 + c)]

tablero = [[0 for j in range(6)] for i in range(7)]
player = 1
drop = False


pygame.init()
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Connect 4")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            drop = True
    # ---------------------------------------------------LÓGICA---------------------------------------------------
    
    if(drop):
        x = int(pos[0]/(esp*2+c))

        for i in range(6):
            if(tablero[x][i] != 0):
                if(i != 0):
                    tablero[x][i-1] = player
                    player *= -1

                break
            elif(i == 5):
                tablero[x][5] = player
                player *= -1
                break

        drop = False

    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(FONDO_TABL)

    #fuente = pygame.font.Font(None, 75)
    #txt = fuente.render('GAME OVER', True, (0,0,0))
    #pantalla.blit(txt, [200,300])

    x = esp
    y = esp
    for i in range(7):
        for j in range(6):
            
            if(tablero[i][j] == 0):
                pygame.draw.ellipse(pantalla, FONDO, [x, y, c, c])
            elif(tablero[i][j] == 1):
                pygame.draw.ellipse(pantalla, ROJO, [x, y, c, c])
            elif(tablero[i][j] == -1):
                pygame.draw.ellipse(pantalla, AMARILLO, [x, y, c, c])

            pygame.draw.ellipse(pantalla, NEGRO, [x, y, c, c], 3)
            y += esp*2 + c
        
        y = esp
        x += esp*2 + c



    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
