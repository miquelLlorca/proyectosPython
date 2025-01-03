import pygame
import random
 
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)



x, y = [int(x) for x in input("Dimensiones: ").split()]
nDim = [x, y]
tam = int(input("Tamaño: "))
dimensiones = [x*tam, y*tam]
mapa = [ [0 for i in range(y)] for i in range(x)]
pintar = False
mi, mj = [-1, -1]

pygame.init()
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Crear mapa")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

        if evento.type == pygame.MOUSEBUTTONDOWN:
            pintar = True
        if evento.type == pygame.MOUSEBUTTONUP:
            pintar = False

    # ---------------------------------------------------LÓGICA---------------------------------------------------
    
    if(pintar):
        oldMi, oldMj = [mi, mj]
        mi, mj = [ i//tam for i in pygame.mouse.get_pos()]
        print(mi, mj)

        if(not (mi == oldMi and mj == oldMj)):
            if(mapa[mi][mj] == 0):
                mapa[mi][mj] = 1
            elif(mapa[mi][mj] == 1):
                mapa[mi][mj] = 0

    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(BLANCO)

    for i in range(x):
        pygame.draw.line(pantalla, NEGRO, [i*tam, 0], [i*tam, dimensiones[1]], 2)

    for j in range(y):
        pygame.draw.line(pantalla, NEGRO, [0, j*tam], [dimensiones[0], j*tam], 2)


    for i in range(x):
        for j in range(y):
            if(mapa[i][j] == 1):
                pygame.draw.rect(pantalla, NEGRO, [i*tam, j*tam, tam, tam])



    pygame.display.flip()
    reloj.tick(60)

pygame.quit()

if(input("Save? ") == "y"):
    name = input("Write name: ")
    file = open(name, "w")

    for i in range(y):
        for j in range(x):
            file.write( "# " if mapa[j][i]==1 else ". ")
        file.write("\n")

    file.close()