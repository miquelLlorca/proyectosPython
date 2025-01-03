#prueba juego
import pygame

# Colores:
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
PI = 3.1415926535

pygame.init()
dimensiones = (700,500)
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption('PRUEBA')


#Itera hasta que el usuario pincha sobre el botón de cierre.
hecho = False
 
# Se usa para gestionar cuan rápido se actualiza la pantalla
reloj = pygame.time.Clock()
 
# -------- Bucle Principal del Programa -----------
while not hecho:
    # TODOS LOS EVENTOS DE PROCESAMIENTO DEBERÍAN IR DEBAJO DE ESTE COMENTARIO
    
    for evento in pygame.event.get(): # El usuario hizo algo
        if evento.type == pygame.QUIT: # Si el usuario pincha sobre cerrar
            hecho = True # Esto que indica que hemos acabado y sale de este bucle
    # TODOS LOS EVENTOS DE PROCESAMIENTO DEBERÍAN IR ENCIMA DE ESTE COMENTARIO
 
 
    # TODA LA LÓGICA DEL JUEGO DEBERÍA IR DEBAJO DE ESTE COMENTARIO
 
    # TODA LA LÓGICA DEL JUEGO DEBERÍA IR ENCIMA DE ESTE COMENTARIO
 
 
    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR DEBAJO DE ESTE COMENTARIO
    pantalla.fill(BLANCO)
    for i in range(5):
        pygame.draw.line(pantalla, AZUL, [0 + 10*i, 0], [700, 500 - 10*i], 5)
    pygame.draw.rect(pantalla, (0,0,0), [50,200, 200, 100], 1)
    pygame.draw.ellipse(pantalla, (0,0,0), [50,200, 200, 100], 1)
    pygame.draw.arc(pantalla, VERDE, [300, 100, 200, 100], PI/2, PI, 2)
    pygame.draw.polygon(pantalla, ROJO, [[92, 55], [205, 309], [699, 499], [346, 100], [129, 200]], 2)
    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR ENCIMA DE ESTE COMENTARIO
    pygame.display.flip()

    # Limita a 20 fotogramas por segundo (frames per second)
    reloj.tick(20)

pygame.quit()
