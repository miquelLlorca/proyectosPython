import pygame
import random

NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)
  
pygame.init()
dimensiones = [700,500]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Mi Primer juego en Informática")
hecho = False
reloj = pygame.time.Clock()

pos = [0, 0]
vel = [random.randrange(1,6), random.randrange(1,6)]
colores = [VERDE, ROJO, AZUL, VIOLETA]
color = (random.randrange(0,256), random.randrange(0,256), random.randrange(0,256))

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
     
    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ
  
    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ
    pantalla.fill(NEGRO)
    pygame.draw.ellipse(pantalla, color, [pos[0], pos[1] , 90, 50])

    for i in range(2):
        pos[i] += vel[i]

    if pos[0] > 610 or pos[0] < 0:
        vel[0] *= -1
        color = (random.randrange(0,256), random.randrange(0,256), random.randrange(0,256))
    if pos[1] > 450 or pos[1] < 0:
        vel[1] *= -1
        color = (random.randrange(0,256), random.randrange(0,256), random.randrange(0,256))


    pygame.display.flip()
    reloj.tick(60)
     
pygame.quit()

