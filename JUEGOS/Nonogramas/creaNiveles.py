import pygame
import random
import Tablero as tab


NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)

sn = 's'

while(sn == 's' or sn == 'S'):
    n = int(input("Tamaño (n x n): "))
    res = 50
    dimensiones = [n*res, n*res]

    tablero = tab.Tablero(n)

    cambio = False
    valor = 1
    
    pygame.init()
    pantalla = pygame.display.set_mode(dimensiones) 
    pygame.display.set_caption("crear nivel")
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
                    if(valor):
                        valor = 0
                    else:
                        valor = 1

        # ---------------------------------------------------LÓGICA---------------------------------------------------
        x, y = pygame.mouse.get_pos()

        if(cambio):
            xi = int(x/res)
            yi = int(y/res)

            tablero.set(xi, yi, valor)
            

        # ---------------------------------------------------DIBUJO---------------------------------------------------

        pantalla.fill((200, 200, 200))

        tablero.draw(res, pantalla)

        tab.drawCursor(x, y, valor, pantalla)

        pygame.display.flip()
        reloj.tick(30)

    pygame.quit()

    print("Guardando tablero...")
    tablero.guardar()
    print("Tablero guardado.")
    sn = input("Continuar? ")
