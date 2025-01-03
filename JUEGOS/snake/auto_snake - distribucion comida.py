import pygame
from random import randrange

def creaCom():
    x = [randrange(1,46), randrange(1,46)]
    return x

def bordes():
    pygame.draw.rect(pantalla, (255,255,255), [0, 0, 14, 704])
    pygame.draw.rect(pantalla, (255,255,255), [0, 0, 704, 14])
    pygame.draw.rect(pantalla, (255,255,255), [705, 705, -13, -705])
    pygame.draw.rect(pantalla, (255,255,255), [705, 705, -705, -13])

def mover(cola, vel):
    for i in range(2):
        if 15 <= cola[0][i] + vel[i] <= dimensiones[i] - 30:
            for j in range(1,len(cola)):
                if cola[j][0] == cola[0][0] + vel[0]*15 and cola[j][1] == cola[0][1] + vel[1]*15:
                    return False
        else:
            return False
    return True
56, 255, 79
    
NEGRO = (0, 0 ,0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
colCom = [[251, 255, 133], [56, 255, 79], [131, 247, 247], [129, 125, 255], [255, 79, 79], [205, 76, 252]]
listaCom = []
for i in range(47):
    listaCom.append([])
    for j in range(47):
        listaCom[i].append(0)
        
vel = [0,0]
puntos = 0
cola = []
for i in range(2):
    cola.append([-1*(i-1)*15, 15])
perder = False
posCom = creaCom()
listaCom[posCom[0]][posCom[1]] += 1
posCom[0] *= 15
posCom[1] *= 15
            
pygame.init()
dimensiones = [705,705] #47 cuadrados de 15 px
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption('Snake')
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        elif evento.type == pygame.KEYDOWN:
            '''if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
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
                    vel = [0,1]'''
            if evento.key == pygame.K_r: #reset
                vel = [0,0]
                puntos = 0
                cola = []
                for i in range(2):
                    cola.append([-1*(i-1)*15, 15])
                perder = False
                posCom = creaCom()
                listaCom[posCom[0]][posCom[1]] += 1
                posCom[0] *= 15
                posCom[1] *= 15
    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ
    if not perder:
        if vel[0] == 0:
            if cola[0][0] - posCom[0] > 0:
                vel = [-1,0]
            elif cola[0][0] - posCom[0] < 0:
                vel = [1,0]
        
        elif vel[1] == 0:
            if cola[0][1] - posCom[1] > 0:
                vel = [0,-1]
            elif cola[0][1] - posCom[1] < 0:
                vel = [0,1]
                
        mov = False
        cont = 0
        while mov == False:
            if mover(cola, vel):
                if vel[0] != 0 or vel[1] != 0:
                    if cola[len(cola)-1] == [None]:
                        cola[len(cola)-1] = [cola[len(cola)-2][0], cola[len(cola)-2][1]]
                    for i in range(len(cola)-1,-1, -1):
                        if i < len(cola)-1:
                            cola[i+1] = [cola[i][0], cola[i][1]]
                        
                    for i in range(2):
                        cola[0][i] += vel[i]*15
                    mov = True
            else:
                if vel[0] != 0:
                    if mover(cola, [0, 1]):
                        vel = [0,1]
                    else:
                        vel = [0,-1]
                else:
                    if mover(cola, [1, 0]):
                        vel = [1, 0]
                    else:
                        vel = [-1, 0]
            cont += 1
            if cont > 3:
                vel = [0,0]
                puntos = 0
                cola = []
                for i in range(2):
                    cola.append([-1*(i-1)*15, 15])
                perder = False
                posCom = creaCom()
                listaCom[posCom[0]][posCom[1]] += 1
                posCom[0] *= 15
                posCom[1] *= 15
                break
                    
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
            
        for i in range(47):
            for j in range(47):
                if 6 > listaCom[i][j] > 0:
                    pygame.draw.rect(pantalla, colCom[listaCom[i][j]-1], [i*15+1, j*15+1, 13, 13])
                elif 6 < listaCom[i][j]:
                    pygame.draw.rect(pantalla, colCom[5], [i*15+1, j*15+1, 13, 13])
                    
        pygame.draw.rect(pantalla, ROJO, [posCom[0]+1, posCom[1]+1, 13, 13])
        
        if posCom == cola[0]:
            posCom = creaCom()
            puntos += 1
            
            listaCom[posCom[0]][posCom[1]] += 1
            cola.append([None])
            print(puntos)
            posCom[0] *= 15
            posCom[1] *= 15
            
        for x in cola:
            if x != [None]:
                if 15 <= x[0] :
                    pygame.draw.rect(pantalla, VERDE, [x[0]+1, x[1]+1, 13, 13])

    else:
        pantalla.fill(ROJO)
        fuente = pygame.font.Font(None, 75)
        txt = fuente.render('GAME OVER', True, (0,0,0))
        txt2 = fuente.render('Press R to restart', True, (0,0,0))
        pantalla.blit(txt, [200,300])
        pantalla.blit(txt2, [150, 360])
        
    pygame.display.flip()
    reloj.tick(120)

pygame.quit()
