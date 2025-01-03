import pygame
import random
 
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)
COLORES = [(229, 235, 52), (52, 198, 235), VIOLETA, AZUL, VERDE, ROJO]

dimensiones = [1500,700]

towers = [[0 for j in range(6)]for i in range(5)]
towers[0] = [1, 2, 3, 4, 5, 6]

suelo = 500
top = suelo - 6*(10 + 30)

seleccion = [[-1, -1], 0]
click = False


pygame.init()
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Torres de Hanoi")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

        if evento.type == pygame.MOUSEBUTTONDOWN:
            click = True

    # ---------------------------------------------------LÓGICA---------------------------------------------------
    if(click):
        pos = pygame.mouse.get_pos()
        t = int(pos[0]/300)
        print(t)
        
        if(seleccion[1] == 0):
            for i in range(6):
                if(towers[t][i] != 0):
                    seleccion = [[t, i], towers[t][i]]
                    break

        else:
            for i in range(5, -1, -1):
                if(towers[t][i] == 0):
                    towers[t][i] = seleccion[1]
                    towers[seleccion[0][0]][seleccion[0][1]] = 0

                    seleccion = [[-1, -1], 0]
                    break

        click = False

    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(BLANCO)

    
    pygame.draw.line(pantalla, NEGRO, [0, suelo], [dimensiones[0], suelo], 5)

    for i in range(5):
        pygame.draw.line(pantalla, NEGRO, [150+i*300, 0], [150+i*300, suelo], 5)

    for i in range(5):
        eje = 150+i*300

        for j in range(6):
            n = towers[i][j]
            
            if(n != 0):
                pygame.draw.rect(pantalla, COLORES[n-1], [eje-30*n, top+j*(40), 30*n*2, 30])


        

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
