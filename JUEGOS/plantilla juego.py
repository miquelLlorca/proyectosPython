import pygame
import random
 
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)


class LOL:
    def __init__(self):
        self.a = 0

# ========================================================================================

dimensiones = [1800,1000]

# MAIN =================================================================================================================

if(__name__ == "__main__"):
    pygame.init()
    pantalla = pygame.display.set_mode(dimensiones) 
    pygame.display.set_caption("PYGAMEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
    hecho = False
    reloj = pygame.time.Clock()


    pers = pygame.image.load('flappydef.png').convert()
    pers.set_colorkey(BLANCO)


    while not hecho:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                hecho = True

        # LÓGICA---------------------------------------------LÓGICA---------------------------------------------LÓGICA
        pos = pygame.mouse.get_pos()
        # DIBUJO---------------------------------------------DIBUJO---------------------------------------------DIBUJO

        pantalla.fill(BLANCO)

        fuente = pygame.font.Font(None, 75)
        txt = fuente.render('GAME OVER', True, (0,0,0))
        pantalla.blit(txt, [200,300])

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()
