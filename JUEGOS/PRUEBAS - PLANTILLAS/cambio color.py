import pygame
 
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

color = [(0,0,0)]

for i in range(255):
    c = (0+i,0,0)
    color.append(c)



for i in range(255):
    c = (255,0+i,0)
    color.append(c)



for i in range(255):
    c = (255,255,0+i)
    color.append(c)




    
pygame.init()
dimensiones = [700,500]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Mi Primer juego en Informática")
hecho = False
reloj = pygame.time.Clock()

i = 0

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
     
    # -----------------------------------LÓGICA-----------------------------------
  
    # -----------------------------------DIBUJO-----------------------------------

    pantalla.fill(color[i])
    i += 1
    
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
