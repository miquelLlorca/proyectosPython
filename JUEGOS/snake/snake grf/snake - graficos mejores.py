import pygame
from random import randrange

def creaCom():
    x = [randrange(1,46)*15, randrange(1,46)*15]
    while x in cola:
        x = [randrange(1,46)*15, randrange(1,46)*15]
    return x

def bordes():
    pygame.draw.rect(pantalla, (255,255,255), [0, 0, 14, 704])
    pygame.draw.rect(pantalla, (255,255,255), [0, 0, 704, 14])
    pygame.draw.rect(pantalla, (255,255,255), [705, 705, -13, -705])
    pygame.draw.rect(pantalla, (255,255,255), [705, 705, -705, -13])


#fondo = pygame.image.load('laberinto.png').convert()
#pantalla.blit(pers, [pos[0], pos[1]])

BLANCO = (255, 255, 255)
NEGRO = (0, 0 ,0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

vel = [0,0]
puntos = 0
cola = []
for i in range(10):
    cola.append([-1*(i-1)*15, 15])
perder = False
posCom = creaCom()
fps = 10

pygame.init()
dimensiones = [705,705] #47 cuadrados de 15 px
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption('Snake')
hecho = False
reloj = pygame.time.Clock()

cabeza1 = pygame.image.load('cabeza1.png').convert()
cabeza2 = pygame.image.load('cabeza2.png').convert()
cabeza3 = pygame.image.load('cabeza3.png').convert()
cabeza4 = pygame.image.load('cabeza4.png').convert()

giro1 = pygame.image.load('giro1.png').convert()
giro2 = pygame.image.load('giro2.png').convert()
giro3 = pygame.image.load('giro3.png').convert()
giro4 = pygame.image.load('giro4.png').convert()

cola1 = pygame.image.load('cola1.png').convert()
cola2 = pygame.image.load('cola2.png').convert()
cola3 = pygame.image.load('cola3.png').convert()
cola4 = pygame.image.load('cola4.png').convert()

rectox = pygame.image.load('rectox.png').convert()
rectoy = pygame.image.load('rectoy.png').convert()

comida = pygame.image.load('comida.png').convert()

cabeza1.set_colorkey(NEGRO)
cabeza2.set_colorkey(NEGRO)
cabeza3.set_colorkey(NEGRO)
cabeza4.set_colorkey(NEGRO)

giro1.set_colorkey(NEGRO)
giro2.set_colorkey(NEGRO)
giro3.set_colorkey(NEGRO)
giro4.set_colorkey(NEGRO)

cola1.set_colorkey(NEGRO)
cola2.set_colorkey(NEGRO)
cola3.set_colorkey(NEGRO)
cola4.set_colorkey(NEGRO)

rectox.set_colorkey(NEGRO)
rectoy.set_colorkey(NEGRO)

comida.set_colorkey(NEGRO)

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                if vel[0] == 0:
                    vel = [-1,0]
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                if vel[0] == 0:
                    vel = [1,0]
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                if vel[1] == 0:
                    vel = [0,-1]
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                if vel[1] == 0:
                    vel = [0,1]
            if evento.key == pygame.K_r: #reset
                vel = [0,0]
                puntos = 0
                cola = []
                for i in range(3):
                    cola.append([-1*(i-1)*15, 15])
                perder = False
                posCom = creaCom()

    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ
    if not perder:
        
        if vel[0] != 0 or vel[1] != 0:
            if cola[len(cola)-1] == [None]:
                cola[len(cola)-1] = [cola[len(cola)-2][0], cola[len(cola)-2][1]]
            for i in range(len(cola)-1,-1, -1):
                if i < len(cola)-1:
                    cola[i+1] = [cola[i][0], cola[i][1]]
                
            for i in range(2):
                if 15 <= cola[0][i] + vel[i] <= dimensiones[i] - 30:
                    for j in range(1,len(cola)):
                        if cola[j][0] == cola[0][0] + vel[0]*15 and cola[j][1] == cola[0][1] + vel[1]*15:
                            perder = True
                            break
                            
                    if not perder:
                        cola[0][i] += vel[i]*15
                else:
                    perder = True
                    break
        #comida
        if posCom == cola[0]:
            posCom = creaCom()
            puntos += 1
            cola.append([None])
            if puntos % 10 == 0:
                fps += 2
            print(puntos)
            
    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ
    
    if not perder: 
        pantalla.fill(NEGRO)
        bordes()
        if puntos < 10:
            fuente = pygame.font.Font(None, 500)
            txt = fuente.render(str(puntos), True, (50, 50, 50))
            pantalla.blit(txt, [300,200])
        elif puntos <100:
            fuente = pygame.font.Font(None, 500)
            txt = fuente.render(str(puntos), True, (50, 50, 50))
            pantalla.blit(txt, [175,200])
            
        
        pantalla.blit(comida, [posCom[0], posCom[1]])
        for i in range(len(cola)-1):
            if cola[i] != [None]:
                if 15 <= cola[i][0]:
                    if i==0:
                        if vel[0]==1:
                            pantalla.blit(cabeza2, [cola[0][0], cola[0][1]])
                        elif vel[0]==-1:
                            pantalla.blit(cabeza4, [cola[0][0], cola[0][1]])
                        elif vel[1]==1:
                            pantalla.blit(cabeza3, [cola[0][0], cola[0][1]])
                        elif vel[1]==-1:
                            pantalla.blit(cabeza1, [cola[0][0], cola[0][1]])
                        else:
                            pantalla.blit(cabeza2, [cola[0][0], cola[0][1]])
                    elif i==len(cola)-2 and cola[len(cola)-1]==[None]:
                        if cola[i][0]<cola[i-1][0]:
                            pantalla.blit(cola2, [cola[i][0], cola[i][1]])
                        elif cola[i][0]>cola[i-1][0]:
                            pantalla.blit(cola4, [cola[i][0], cola[i][1]])
                        elif cola[i][1]>cola[i-1][1]:
                            pantalla.blit(cola1, [cola[i][0], cola[i][1]])
                        elif cola[i][1]<cola[i-1][1]:
                            pantalla.blit(cola3, [cola[i][0], cola[i][1]])
                    elif i==len(cola)-2 and cola[len(cola)-1]!=[None]:
                        if cola[i][0]<cola[i-1][0]:
                            pantalla.blit(cola2, [cola[i][0], cola[i][1]])
                        elif cola[i][0]>cola[i-1][0]:
                            pantalla.blit(cola4, [cola[i][0], cola[i][1]])
                        elif cola[i][1]>cola[i-1][1]:
                            pantalla.blit(cola1, [cola[i][0], cola[i][1]])
                        elif cola[i][1]<cola[i-1][1]:
                            pantalla.blit(cola3, [cola[i][0], cola[i][1]])
                    else:
                        if cola[i-1][0]==cola[i][0]==cola[i+1][0]:
                            pantalla.blit(rectox, [cola[i][0], cola[i][1]])
                        elif cola[i-1][1]==cola[i][1]==cola[i+1][1]:
                            pantalla.blit(rectoy, [cola[i][0], cola[i][1]])
                        elif (cola[i-1][1]>cola[i][1] and cola[i][0]<cola[i+1][0]) or (cola[i+1][1]>cola[i][1] and cola[i][0]<cola[i-1][0]):
                            pantalla.blit(giro1, [cola[i][0], cola[i][1]])
                        elif (cola[i-1][1]<cola[i][1] and cola[i][0]<cola[i+1][0]) or (cola[i+1][1]<cola[i][1] and cola[i][0]<cola[i-1][0]):
                            pantalla.blit(giro4, [cola[i][0], cola[i][1]])
                        elif (cola[i-1][1]<cola[i][1] and cola[i][0]>cola[i+1][0]) or (cola[i+1][1]<cola[i][1] and cola[i][0]>cola[i-1][0]):
                            pantalla.blit(giro3, [cola[i][0], cola[i][1]])
                        elif (cola[i-1][1]>cola[i][1] and cola[i][0]>cola[i+1][0]) or (cola[i+1][1]>cola[i][1] and cola[i][0]>cola[i-1][0]):
                            pantalla.blit(giro2, [cola[i][0], cola[i][1]])
                            
    else:
        pantalla.fill(ROJO)
        fuente = pygame.font.Font(None, 75)
        txt = fuente.render('GAME OVER', True, (0,0,0))
        txt2 = fuente.render('Press R to restart', True, (0,0,0))
        pantalla.blit(txt, [200,300])
        pantalla.blit(txt2, [150, 360])
        
    pygame.display.flip()
    reloj.tick(fps)

pygame.quit()
