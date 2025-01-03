import pygame
 
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)
  
pygame.init()
dimensiones = [900,600]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Control con teclado")
hecho = False
reloj = pygame.time.Clock()

fondo = pygame.image.load('laberinto.png').convert()
pers = pygame.image.load('flappydef.png').convert()
pers.set_colorkey(BLANCO)
vel = [0, 0]
pos = [0, 60]

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                vel[0] = -5
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                vel[0] = 5
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                vel[1] = -5
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                vel[1] = 5
                
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                vel[0] = 0
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                vel[0] = 0
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                vel[1] = 0
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                vel[1] = 0
            
     
    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ
    for i in range(2):
        if 0 <= pos[i] + vel[i] <= dimensiones[i] - 20:
            pos[i] += vel[i]
    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ
    #pantalla.fill(BLANCO)
    pantalla.blit(fondo, [0,0])
    #pygame.draw.rect(pantalla, NEGRO, [pos[0], pos[1], 20, 20])
    pantalla.blit(pers, [pos[0], pos[1]])
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()