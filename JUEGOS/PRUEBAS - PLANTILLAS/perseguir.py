import pygame
 
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
vel1 = [0, 0]
pos1 = [0, 0]
vel2 = [0, 0]
pos2 = [0, 480]
perder = False

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
                vel1[0] = -4
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                vel1[0] = 4
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                vel1[1] = -4
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                vel1[1] = 4
            if evento.key == pygame.K_r: #reset
                vel1 = [0, 0]
                pos1 = [0, 0]
                vel2 = [0, 0]
                pos2 = [0, 480]
                perder = False

        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                vel1[0] = 0
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                vel1[0] = 0
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                vel1[1] = 0
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                vel1[1] = 0
     
    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ
    if not perder:
        for i in range(2):
            if pos1[i] != pos2[i]:
                    if pos1[i] < pos2[i]:
                        vel2[i] = -2
                    else:
                        vel2[i] = 2
            else:
                vel2[i] = 0
        for i in range(2):
            if 0 <= pos1[i] + vel1[i] <= dimensiones[i] - 20:
                pos1[i] += vel1[i] 
            if 0 <= pos2[i] + vel2[i] <= dimensiones[i] - 20:
                pos2[i] += vel2[i]
        p1 = []
        p2 = []
        
        for i in range(2):
            p1.append([])
            p2.append([])
            for j in range(20):
                p1[i].append(pos1[i] + j)
                p2[i].append(pos2[i] + j)
                
        for x in p1[0]:
            if x in p2[0]:
                for y in p1[1]:
                    if y in p2[1]:
                        perder = True
                        break
        
    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ
    if not perder:
        pantalla.fill(BLANCO)
        pygame.draw.rect(pantalla, NEGRO, [pos1[0], pos1[1], 20, 20])
        pygame.draw.rect(pantalla, ROJO, [pos2[0], pos2[1], 20, 20])
        
    else:
        pantalla.fill(ROJO)
        fuente = pygame.font.Font(None, 75)
        txt = fuente.render('GAME OVER', True, (0,0,0))
        txt2 = fuente.render('Press R to restart', True, (0,0,0))
        pantalla.blit(txt, [200,300])
        pantalla.blit(txt2, [150, 360])
    pygame.display.flip()
    reloj.tick(60)
pygame.quit()
