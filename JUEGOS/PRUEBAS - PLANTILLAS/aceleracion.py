import pygame
from random import randrange

def creaCol():
    col = [0,0,0]
    for i in range(3):
        col[i] = randrange(0,256)
    return col
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)
vel = [0, 0]
pos = [0, 60]

pygame.init()
dimensiones = [900,800]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Mi Primer juego en Informática")
hecho = False
reloj = pygame.time.Clock()
pantalla.fill(BLANCO)
ac = False
op = [False, False, False, False]

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                op[0] = True
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                op[1] = True
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                op[2] = True
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                op[3] = True
            
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                op[0] = False
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                op[1] = False
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                op[2] = False
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                op[3] = False
    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ
    
    if op[0]:
        vel[0] -= 1
    if op[1]:
        vel[0]+= 1
    if op[2]:
        vel[1] -= 1
    if op[3]:
        vel[1] += 1
            
    for i in range(2):
        if 0 <= pos[i] + vel[i] <= dimensiones[i] - 20:
            pos[i] += vel[i]
    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ
    col = creaCol()
    #pantalla.fill(BLANCO)
    col = creaCol()
    pygame.draw.rect(pantalla, NEGRO, [pos[0], pos[1], 20, 20])
    pygame.display.flip()
    reloj.tick(10)

pygame.quit()
