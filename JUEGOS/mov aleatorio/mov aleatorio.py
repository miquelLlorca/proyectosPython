import pygame
from random import randrange

# p = c/t *100 

def calc(x):
    suma = 0
    for n in x:
        suma += n
    p = []
    for i in range(len(x)):
        p.append(round(x[i]*100/suma, 2))
    print('R {}, L {}, D {}, U {}'.format(p[0],p[1],p[2],p[3]))

def creacol():
    col = []
    for i in range(3):
        col.append(randrange(255))
    return col
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)

vel = [0,0]
pos = [0, 0]
perder = False
cont = 0
vels = [[1,0], [-1,0], [0,1], [0,-1]] # right, left, down, up
veces = [0, 0, 0, 0]
COLOR = creacol()

pygame.init()
dimensiones = [705,705] #47 cuadrados de 15 px
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption('Snake')
hecho = False
reloj = pygame.time.Clock()
pantalla.fill(BLANCO)

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r: #reset
                vel = [0,0]
                pos = [0, 0]
                perder = False

    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ
    
    if cont == 2:
        x = randrange(4)
        vel = vels[x]
        veces[x] += 1
        cont = 0
        calc(veces)
        COLOR = creacol()
    else:
        cont += 1
                
    for i in range(2):
        if 0 <= pos[i] + vel[i]*3 <= dimensiones[i] - 15:
            pos[i] += vel[i]*10

    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ
    #pantalla.fill(BLANCO) 
    pygame.draw.rect(pantalla, COLOR, [pos[0], pos[1], 15, 15])
    
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()

print(veces)
