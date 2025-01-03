import pygame
import random
import Tablero as tab

sn = 's'
while(sn == 's' or sn == 'S'):

    nextName = open("Niveles/nextLevel.txt", 'r') # se busca el nuevo nombre
    levelName = int(nextName.readline())
    nextName.close()

    level = open("Niveles/"+str(levelName)+".txt", 'r')
    t = int(level.readline())
    tablero = tab.Tablero(t)
    xs = []
    for i in range(t):
        xs.append([int(x) for x in level.readline().split()])

    ys = []
    for i in range(t):
        ys.append([int(x) for x in level.readline().split()])

    level.close()

    levelName = str(int(levelName) + 1) # se actualiza el nombre y se guarda
    nextName = open("Niveles/nextName.txt", 'w')
    nextName.write(levelName)
    nextName.close()
        
    change = False

    res = 50
    dimensiones = [t*res, t*res]
    cambio = False
    valor = 1



    pygame.init()
    pantalla = pygame.display.set_mode(dimensiones) 
    pygame.display.set_caption("Nonogramas")
    hecho = False
    reloj = pygame.time.Clock()
    pygame.mouse.set_visible(0)

    while not hecho:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                hecho = True

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                cambio = True
            elif evento.type == pygame.MOUSEBUTTONUP:
                cambio = False

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_c:
                    if(valor == 1):
                        valor = -1
                    else:
                        valor = 1

                elif evento.key == pygame.K_x:
                    valor = 0

        # ---------------------------------------------------LÓGICA---------------------------------------------------
        x, y = pygame.mouse.get_pos()

        if(cambio):
            xi = int(x/res)
            yi = int(y/res)

            tablero.set(xi, yi, valor)
        
        if(tablero.equals(xs, ys)):
            hecho = True
        # ---------------------------------------------------DIBUJO---------------------------------------------------

        pantalla.fill((0, 0, 0))

        tablero.draw(res, pantalla)
        tab.drawCursor(x, y, valor, pantalla)

        pygame.display.flip()
        reloj.tick(30)


    pygame.quit()

    sn = input("Continuar? ")


        
