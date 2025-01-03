import pygame

NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

valores = []
v = 0
for i in range(50):
    valores.append([])
    for j in range(50):
        valores[i].append(v + (1/50)*j)
    v += 1/50
        
print(valores)

pygame.init()
dimensiones = [500,500]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Mi Primer juego en Informática")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
     
    # -----------------------------------LÓGICA-----------------------------------
    
    # -----------------------------------DIBUJO-----------------------------------

    pantalla.fill(BLANCO)

    for i in range(50):
        for j in range(50):
            if(valores[i][j]<0.125):
                color = [255, 0, 0]
            elif(valores[i][j]<0.375):
                color = [255, 100, 100]
            elif(valores[i][j]<0.625):
                color = [255, 255, 255]
            elif(valores[i][j]<0.875):
                color = [100, 100, 255]
            else:
                color = [0, 0, 255]
                
            pygame.draw.rect(pantalla, color, [i*10, j*10, 10, 10])
        
    
    pygame.display.flip()
    reloj.tick(5)

pygame.quit()
