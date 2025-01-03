import pygame
import random

def linea(a, b):
    pygame.draw.line(pantalla, (0,0,0), a, b, 1)

    
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

dim = [700, 700]
res = 20
puntos  = []

for i in range(int(dim[0]/res)+1):
    puntos.append([])
    for j in range(int(dim[1]/res)+1):
        puntos[i].append(random.randint(0,1))
    
pygame.init()
pantalla = pygame.display.set_mode(dim) 
pygame.display.set_caption("Marching squares")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

    # ---------------------------------------------------LÓGICA---------------------------------------------------
    
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill((100, 100, 100))

    for i in range(int(dim[0]/res+1)):
        for j in range(int(dim[1]/res+1)):
            col = NEGRO if(puntos[i][j]) else BLANCO
            pygame.draw.ellipse(pantalla, col, [i*res-3, j*res-3, 6, 6])


    for i in range(int(dim[0]/res)):
        for j in range(int(dim[1]/res)):
            estado = puntos[i][j] + puntos[i+1][j]*2 + puntos[i+1][j+1]*4 + puntos[i][j+1]*8
            x = i*res 
            y = j*res
            
            a = [x, y + res/2]
            b = [x + res/2, y]
            c = [x + res, y + res/2]
            d = [x  + res/2, y + res]
            
            if(estado == 1):
                linea(a, b)
            elif(estado == 2):
                linea(b, c)
            elif(estado == 3):
                linea(a, c)
            elif(estado == 4):
                linea(c, d)
            elif(estado == 5):
                linea(a, b)
                linea(c, d)                
            elif(estado == 6):
                linea(b, d)
            elif(estado == 7):
                linea(a, d)
            elif(estado == 8):
                linea(a, d)
            elif(estado == 9):
                linea(b, d)
            elif(estado == 10):
                linea(b, c)
                linea(a, d)
            elif(estado == 11):
                linea(c, d)
            elif(estado == 12):
                linea(a, c)
            elif(estado == 13):
                linea(b, c)
            elif(estado == 14):
                linea(a, b)
            
    pygame.display.flip()
    reloj.tick(10)

pygame.quit()
