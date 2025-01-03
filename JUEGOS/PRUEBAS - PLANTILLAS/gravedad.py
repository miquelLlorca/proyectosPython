import pygame
 
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
vel = [0, 0]
pos = [0, 0]
g =[0, 9.8]

pygame.init()
dimensiones = [700,500]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Mi Primer juego en Informática")
hecho = False
reloj = pygame.time.Clock()

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
                vel[1] = -10
                
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                vel[0] = 0
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                vel[0] = 0
            '''if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                vel[1] = 0
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                vel[1] = 0'''
     
    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ

    if  pos[1] < dimensiones[1] - 20:
        vel[1] +=0.5
        
    for i in range(2):
        if 0 <= pos[i] + vel[i] <= dimensiones[i] - 20:
            pos[i] += vel[i] 
            
    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ

    pantalla.fill(BLANCO)
    pygame.draw.rect(pantalla, NEGRO, [pos[0], pos[1], 20, 20])
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
