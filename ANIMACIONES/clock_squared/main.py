import pygame
import random
from clock import *
from clock_manager import ClockManager


NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)




# ========================================================================================


# MAIN =================================================================================================================

if(__name__ == "__main__"):


    time = '0123456789'
    t_pos = 0


    dimensiones = [900,900]

    
    manager = ClockManager([9,9], 50)
    manager.SetBigClock(ClockSquared([0,3]))

    pygame.init()
    pantalla = pygame.display.set_mode(dimensiones) 
    pygame.display.set_caption("Clock")
    hecho = False
    reloj = pygame.time.Clock()



    while not hecho:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                hecho = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    t_pos += 1
                    t_pos = t_pos%len(time)
                    t_aux = [int(x) for x in time[t_pos:t_pos+4]]
                    manager.SetTime(t_aux)


        # LÓGICA---------------------------------------------LÓGICA---------------------------------------------LÓGICA
        pos = pygame.mouse.get_pos()
        manager.Update()
        # DIBUJO---------------------------------------------DIBUJO---------------------------------------------DIBUJO

        pantalla.fill(BLANCO)

        manager.Draw(pantalla)

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()

