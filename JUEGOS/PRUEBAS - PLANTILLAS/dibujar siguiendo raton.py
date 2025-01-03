import pygame

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
 
def dibuja_hombrepalitos(pantalla, x, y):
    # Cabeza
    pygame.draw.ellipse(pantalla, NEGRO, [1 + x, y, 10, 10], 0)
    # Piernas
    pygame.draw.line(pantalla, NEGRO, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(pantalla, NEGRO, [5 + x, 17 + y], [x, 27 + y], 2)
    # Cuerpo
    pygame.draw.line(pantalla, ROJO, [5 + x, 17 + y], [5 + x, 7 + y], 2)
    # Brazos
    pygame.draw.line(pantalla, ROJO, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(pantalla, ROJO, [5 + x, 7 + y], [1 + x, 17 + y], 2)
     

pygame.init()
dimensiones = [700, 500]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Mi Juego")
hecho = False
reloj = pygame.time.Clock()
 
# Ocultamos el cursor del ratón.
pygame.mouse.set_visible(0)

while not hecho:
    for evento in pygame.event.get():  
        if evento.type == pygame.QUIT: 
            hecho = True  
 
    # TODA LA LÓGICA DEL JUEGO DEBERÍA IR DEBAJO DE ESTE COMENTARIO
 
    # Llamamos a la función que dibuja al hombre de palitos
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]

    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR DEBAJO DE ESTE COMENTARIO
    pantalla.fill(BLANCO)
    dibuja_hombrepalitos(pantalla, x, y)
    
    pygame.display.flip()
    reloj.tick(30)
    
pygame.quit()
