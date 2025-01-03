import pygame

def forma(x, y, t):
    pygame.draw.line(pantalla, NEGRO, [x, y],[x + 86*t, y+50*t])
    pygame.draw.line(pantalla, NEGRO, [x + 86*t, y+50*t],[x + 86*2*t, y])
    pygame.draw.line(pantalla, NEGRO, [x+86*2*t, y],[x + 86*3*t, y+50*t])
    pygame.draw.line(pantalla, NEGRO, [x+86*3*t, y+50*t],[x + 86*3*t, y+150*t])
    pygame.draw.line(pantalla, NEGRO, [x+86*3*t, y+150*t],[x + 86*2*t, y+200*t])
    pygame.draw.line(pantalla, NEGRO, [x+86*2*t, y+200*t],[x + 86*2*t, y+300*t])
    pygame.draw.line(pantalla, NEGRO, [x, y+300*t],[x + 86*t, y+350*t])
    pygame.draw.line(pantalla, NEGRO, [x + 86*t, y+350*t],[x + 86*2*t, y+300*t])
    pygame.draw.line(pantalla, NEGRO, [x, y+300*t],[x, y+200*t])
    pygame.draw.line(pantalla, NEGRO, [x, y+200*t],[x-86*t, y+150*t])
    pygame.draw.line(pantalla, NEGRO, [x-86*t, y+150*t], [x-86*t, y+50*t])
    pygame.draw.line(pantalla, NEGRO, [x-86*t, y+50*t], [x, y])
    pygame.draw.line(pantalla, NEGRO, [x-86*t, y+50*t], [x+86*t, y+150*t])
    pygame.draw.line(pantalla, NEGRO, [x+86*3*t, y+50*t], [x+86*t, y+150*t])
    pygame.draw.line(pantalla, NEGRO, [x+86*t, y+350*t], [x+86*t, y+150*t])
    
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)
  
pygame.init()
dimensiones = [700,500]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption('Teselado')
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

    # ---------------------------------------------------LÓGICA---------------------------------------------------
  
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(BLANCO)
    forma(90,0, 0.3)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
