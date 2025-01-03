import random    
import pygame
 
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)
VIOLETA = (98, 0, 255)
colPers = (ROJO, VERDE, AZUL, AMARILLO)

pos = []
vel = []
for i in range(4):
    pos.append([0, 70 + 100*i])
    vel.append(random.randint(1, 10))

puntos = [0,0,0,0]
reiniciar  = False

pygame.init()
dimensiones = [700,470]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Carrera")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

    # ---------------------------------------------------LÓGICA---------------------------------------------------
    for i in range(4):
        pos[i][0] += vel[i]
        if pos[i][0] >= 670:
            reiniciar = True
            puntos[i] += 1
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(BLANCO)

    for i in range(4):
        pygame.draw.rect(pantalla, colPers[i], [pos[i][0], pos[i][1], 30, 30])

    fuente = pygame.font.Font(None, 25)
    for i in range(4):
        txt = fuente.render(str(puntos[i]), True, NEGRO)
        pantalla.blit(txt, [650, 70 + 100*i])
        
    pygame.display.flip()
    reloj.tick(30)

    if reiniciar:
        reiniciar  = False
        pos = []
        vel = []
        for i in range(4):
            pos.append([0, 70 + 100*i])
            vel.append(random.randint(1, 10))
            
pygame.quit()
