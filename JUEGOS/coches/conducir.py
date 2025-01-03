import pygame
from pygame.constants import KEYDOWN
from Coche import Coche, rotaRuedas


NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)


coche = Coche(pos=[200, 500], dt = 1/60)
inputs = [0, 0] # aceleracion y direccion


pygame.init()
dimensiones = [1800, 1000]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Coches")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_w or evento.key == pygame.K_UP: # acelera
                inputs[0] += 1
            if evento.key == pygame.K_s or evento.key == pygame.K_DOWN: # frena
                inputs[0] -= 1

            if evento.key == pygame.K_a or evento.key == pygame.K_LEFT: # izquierda
                inputs[1] -= 1
            if evento.key == pygame.K_d or evento.key == pygame.K_RIGHT: # derecha
                inputs[1] += 1

            if evento.key == pygame.K_r: # reset
                coche = Coche(pos=[200, 500], dt = 1/60)
                inputs = [0, 0] # aceleracion y direccion



        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_w or evento.key == pygame.K_UP:
                inputs[0] = 0
            if evento.key == pygame.K_s or evento.key == pygame.K_DOWN:
                inputs[0] = 0
            if evento.key == pygame.K_a or evento.key == pygame.K_LEFT:
                inputs[1] = 0
            if evento.key == pygame.K_d or evento.key == pygame.K_RIGHT:
                inputs[1] = 0

    # ---------------------------------------------------LÓGICA---------------------------------------------------
    if(inputs[0] != 0):
        coche.Accelerate(inputs[0]*(100 if inputs[0]>0 else 500))
        inputs[0] += 1 if 0<inputs[0]<10 else -1 if 0>inputs[0]>-10 else 0


    if(inputs[1] != 0):
        coche.Steer(inputs[1]*2)
        inputs[0] += 1 if 0<inputs[0]<10 else -1 if 0>inputs[0]>-10 else 0

    
    coche.Update(debug = True)
    print("INPUTS =", inputs)
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill((150, 150, 150))

    aux = 0
    for i in range(4):
        if(i == 1 or i == 2):
            aux = coche.steer
        else:
            aux = 0

        extremos = [[x[j]+coche.pos[j]+coche.ruedas[i][j] for j in range(2)] for x in rotaRuedas(coche.ruedas[i], coche.orientation+aux)]
        pygame.draw.polygon(pantalla, NEGRO, extremos, 20)
        pygame.draw.line(pantalla, NEGRO, [coche.ruedas[i][j]+coche.pos[j] for j in range(2)], 
                                          [coche.ruedas[(i+1)%4][j]+coche.pos[j] for j in range(2)], 2)

    

    pygame.display.flip()
    reloj.tick(60)


pygame.quit()
