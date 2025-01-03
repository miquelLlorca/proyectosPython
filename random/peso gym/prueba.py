import pygame

def flecha(x, y, h, a):
    pygame.draw.line(pantalla, NEGRO, [x, y+(h/2)], [x+a, y+(h/2)], 2)
    pygame.draw.line(pantalla, NEGRO, [x+a, y+(h/2)], [x+(4*a/5), y], 2)
    pygame.draw.line(pantalla, NEGRO, [x+a, y+(h/2)], [x+(4*a/5), y+h], 2)
    
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

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

    # ---------------------------------------------------LÓGICA---------------------------------------------------
  
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(BLANCO)
    flecha(100, 100, 50, 100)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
