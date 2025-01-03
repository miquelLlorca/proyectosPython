import pygame
from random import randrange

def altura(n):
    m = randrange(50, 350)
    while abs(n-m) > 200:
        m = randrange(50, 350)
    return m
        
def dibujaTubo(x, pos):
    pygame.draw.rect(pantalla, TUBOS, [pos, 0, 35, x])
    pygame.draw.rect(pantalla, TUBOS, [pos, x + 70, 35, 500 - x - 70])
    pygame.draw.rect(pantalla, NEGRO, [pos, -2, 35, x], 2)
    pygame.draw.rect(pantalla, NEGRO, [pos, x + 70, 35, 500 - x - 70], 2)
    
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)
CIELO = (86, 148, 210)
TUBOS = (22, 195, 22)
SUELO = (64, 29, 29)

pos = [50, 200]
vel = [0, 0]
altTubos = []
posTubos = []
n = 200
for i in range(6):
    altTubos.append(altura(n))
    posTubos.append(500+150*i)

velTubos = 2.5
perder = False

pygame.init()
dimensiones = [400,500]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Mi Primer juego en Informática")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                vel[1] = -8
            if evento.key == pygame.K_r:
                pos = [50, 200]
                vel = [0, 0]
                altTubos = []
                posTubos = []
                n = 200
                for i in range(6):
                    altTubos.append(altura(n))
                    posTubos.append(500+150*i)

                velTubos = 2
                perder = False


    # ---------------------------------------------------LÓGICA---------------------------------------------------
    for i in range(6):
        posTubos[i] -= velTubos
        
    if posTubos[4] < 400:
        for i in range(2):
            posTubos.append(posTubos[5] + 150)
            posTubos.pop(0)
            altTubos.append(altura(altTubos[5]))
            altTubos.pop(0)
        
    if  pos[1] < dimensiones[1] - 50:
        vel[1] +=0.4
    else:
        perder = True
    
    if 0 <= pos[1] + vel[1] <= dimensiones[1] - 20:
        pos[1] += vel[1] 
    # ---------------------------------------------------DIBUJO---------------------------------------------------
    pantalla.fill(CIELO)
    if not perder:
        pygame.draw.rect(pantalla, VERDE, [0,470, 400, 10 ])
        pygame.draw.rect(pantalla, SUELO, [0,480, 400, 20 ])
        pygame.draw.rect(pantalla, NEGRO, [0,470, 400, 1 ])
        pygame.draw.rect(pantalla, AMARILLO, [pos[0], pos[1], 20, 20])

        # dibujar tubos
        for i in range(6):
            dibujaTubo(altTubos[i], posTubos[i])
        
        pygame.draw.rect(pantalla, VERDE, [0,470, 400, 10 ])
        pygame.draw.rect(pantalla, SUELO, [0,480, 400, 20 ])
        pygame.draw.rect(pantalla, NEGRO, [0,470, 400, 1 ])
    else:
        fuente = pygame.font.Font(None, 50)
        txt = fuente.render('GAME OVER', True, (0,0,0))
        txt2 = fuente.render('Press R to restart', True, (0,0,0))
        pantalla.blit(txt, [100,200])
        pantalla.blit(txt2, [65, 235])
        

    
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
