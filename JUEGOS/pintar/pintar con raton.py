import pygame

NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)
color = NEGRO
x = 20
down = False
pygame.init()
dimensiones = [700, 500]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption('Pintar')
hecho = False
reloj = pygame.time.Clock()
pos = pygame.mouse.get_pos()
# Ocultamos el cursor del ratón.
pygame.mouse.set_visible(0)
pantalla.fill(BLANCO)
while not hecho:
    for evento in pygame.event.get():  
        if evento.type == pygame.QUIT: 
            hecho = True  
        elif evento.type == pygame.KEYDOWN:
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

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            down = True
        elif evento.type == pygame.MOUSEBUTTONUP:
            down = False
            
    # TODA LA LÓGICA DEL JUEGO DEBERÍA IR DEBAJO DE ESTE COMENTARIO
    if down:
         pos = pygame.mouse.get_pos()
    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR DEBAJO DE ESTE COMENTARIO
    pygame.draw.ellipse(pantalla, color, [pos[0], pos[1], x, x])
    pygame.display.flip()
    reloj.tick(600)

    
pygame.quit()
