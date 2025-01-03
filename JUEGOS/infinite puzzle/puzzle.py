import pygame
import random

def printTabla():
    print("1. Rojo")
    print("2. Verde")
    print("3. Azul")
    print("4. Cian")
    print("5. Rosa")
    print("6. Amarillo")
    print("7. Naranja")
    print("8. Morado")

 
def newTablero():
    tablero = []
    for i in range(7):
        tablero.append([])
        for j in range(6):
            tablero[i].append(0)

    tablero[random.randint(0, 6)][random.randint(0, 5)] = 9
    tablero[random.randint(0, 6)][random.randint(0, 5)] = 9

    return tablero

NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

cols = [(150, 150, 150),
        (255,   0,   0),
        (  0, 255,   0),
        (  0,   0, 255),
        (  3, 223, 252),
        (255,   0, 247),
        (229, 255, 0),
        (255, 162,   0),
        (106,   0, 255),
        NEGRO]


tablero = newTablero()
dimensiones = [700,600]
res = 100
printTabla()
n = 1
select = False



pygame.init()
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Puzzle")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            select = True

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                tablero = newTablero()
            
            if evento.key == pygame.K_0:
                n = 0
            elif evento.key == pygame.K_1:
                n = 1
            elif evento.key == pygame.K_2:
                n = 2
            elif evento.key == pygame.K_3:
                n = 3
            elif evento.key == pygame.K_4:
                n = 4
            elif evento.key == pygame.K_5:
                n = 5
            elif evento.key == pygame.K_6:
                n = 6
            elif evento.key == pygame.K_7:
                n = 7
            elif evento.key == pygame.K_8:
                n = 8

    # ---------------------------------------------------LÓGICA---------------------------------------------------
    x, y = pygame.mouse.get_pos()
    if(select):
        xi = int(x/100)
        yi = int(y/100)
        tablero[xi][yi] = n
        select = False
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(BLANCO)

    for i in range(7):
        for j in range(6):
            pygame.draw.rect(pantalla, cols[tablero[i][j]], [i*res, j*res, res, res])

    for i in range(7):
        for j in range(6):
            if(i<6 and tablero[i][j] != tablero[i+1][j]):
                pygame.draw.line(pantalla, NEGRO, [i*res+res, j* res], [i*res+res, j* res+res], 2)

            if(j<5 and tablero[i][j] != tablero[i][j+1]):
                pygame.draw.line(pantalla, NEGRO, [i*res, j*res+res], [i*res+res, j* res+res], 2)


    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
