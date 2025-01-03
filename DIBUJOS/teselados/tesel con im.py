import pygame
    
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)
  
pygame.init()
dimensiones = [800,700]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption('Teselado')
hecho = False
reloj = pygame.time.Clock()
fondo = pygame.image.load('teselado2.png').convert()

x = dimensiones[0]//51 + 1
y = dimensiones[1]//51 + 1
while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

    # ---------------------------------------------------LÓGICA---------------------------------------------------
  
    # ---------------------------------------------------DIBUJO---------------------------------------------------

   
    for i in range(x):
        for j in range(y):
            pantalla.blit(fondo,[51*i, 51*j])
            
    pygame.display.flip()
    reloj.tick(1)

pygame.quit()
