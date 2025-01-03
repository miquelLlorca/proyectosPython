import pygame
 
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)
color = NEGRO
x = 20

pygame.init()
dimensiones = [900,600]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption('Pintar')
hecho = False
reloj = pygame.time.Clock()
pantalla.fill(BLANCO)
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
                
            if evento.key == pygame.K_1:
                color = NEGRO
            if evento.key == pygame.K_2:
                color = ROJO
            if evento.key == pygame.K_3:
                color = AZUL
            if evento.key == pygame.K_4:
                color = VERDE
            if evento.key == pygame.K_5:
                color = VIOLETA
            if evento.key == pygame.K_0:
                color = BLANCO
                
            if evento.key == pygame.K_KP_PLUS:
                x +=10
            if evento.key == pygame.K_KP_MINUS:
                if x > 10:
                    x -=10
                    
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
    pygame.draw.ellipse(pantalla, color, [pos[0], pos[1], x, x])
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
