import pygame
import random

def te(x, y):
    lista = [[x, y],[x-30, y],[x, y-30],[x+30, y],(255, 0, 0)]
    return lista

def cuadrado(x, y):
    lista = [[x, y],[x+30, y],[x, y+30],[x+30, y+30], (0, 255, 0)]
    return lista

def linea(x, y):
    lista = [[x, y],[x+30, y],[x+60, y],[x+90, y], (0, 0, 255)]
    return lista

def ele(x, y):
    lista = [[x, y],[x+30, y],[x, y-30],[x, y-60], (98, 0, 255)]
    return lista

def eleinv(x, y):
    lista = [[x, y],[x-30, y],[x, y-30],[x, y-60], (98, 0, 255)]
    return lista

def ese(x, y):
    lista = [[x, y],[x-30, y],[x-30, y-30],[x, y+30], (200, 0, 255)]
    return lista

def eseinv(x, y):
    lista = [[x, y],[x+30, y],[x+30, y-30],[x, y+30], (200, 0, 255)]
    return lista

def elegirPieza():
    pos = [120, 60]
    lista = [te(pos[0],pos[1]), cuadrado(pos[0],pos[1]),
             linea(pos[0],pos[1]), ele(pos[0],pos[1]), eleinv(pos[0],pos[1]),
             ese(pos[0],pos[1]), eseinv(pos[0],pos[1])]
    return lista[random.randrange(0, 7)]


FONDO = (77, 75, 224)
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)
vel = [0, 1]
pos = [120, 60]
SCREEN = [[60, 60], [360, 660]] #[10, 20]
iniciar = False
pieza = elegirPieza()
tocaSuelo = False
tocaLado = False
puntos = 0
cuad = []
for i in range(20):
    cuad.append([])
    for j in range(10):
        cuad[i].append(0)


pygame.init()
dimensiones = [420, 750]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption('Tetris')
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                vel[0] = -1
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                vel[0] = 1
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                a = 0
                # girar pieza
            iniciar = True
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                vel[0] = 0
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                vel[0] = 0
        
    #----------------------------------------------LÓGICA----------------------------------------------
                
    if iniciar:
        for i in range(len(cuad)):
            for j in range(len(cuad[0])):
                if cuad[i][j] == 0:
                    break
                else:
                    if j==len(cuad[0])-1:
                        cuad.pop(i)
                        cuad.insert(0, [0,0,0,0,0,0,0,0,0])
                        puntos += 10
                        
        for i in range(2):
            for j in range(4):
                if i == 1:
                    if pieza[j][i] == 630:
                        tocaSuelo = True
                        puntos += 4
                        print('suelo')
                        break
                    else:
                         if j == 3:
                            for k in range(4):
                                y = int(pieza[k][0]/30 -2)
                                x = int(pieza[k][1]/30 -2)
                                op1 = cuad[x+1][y] != 0  
                                if op1:
                                    tocaSuelo = True
                                    tocaLado = False
                                    puntos += 4
                                    print('pieza debajo')
                                    break
                                
                else:
                    if 60 <= pieza[j][i] + vel[i]<= 330:
                         if j == 3:
                             for k in range(4):
                                y = int(pieza[k][0]/30 -2)
                                x = int(pieza[k][1]/30 -2)
                                op1 = cuad[x+vel[i]][y] != 0
                                    
                                if op1:
                                    tocaLado = True
                                    
                                    print('pieza a un lado')
                                    break
                                
                    else:
                        tocaLado = True
                        break
                      
        if tocaSuelo:
            for i in range(4):
                y = int(pieza[i][0]/30 -2)
                x = int(pieza[i][1]/30 -2)
                if x > 0:
                    cuad[x][y] = pieza[4]
            
            pieza = elegirPieza()
            
        else:
            for l in range(4):
                pieza[l][1] += vel[1]*30
                if not tocaLado:
                    pieza[l][0] += vel[0]*30
        tocaLado = False
        tocaSuelo = False
                    
    #----------------------------------------------DIBUJO ----------------------------------------------

    pantalla.fill(FONDO)
    pygame.draw.rect(pantalla, (50, 50, 50), [60, 60, 300, 600])
    if iniciar:
        for i in range(4): #color pieza
            if pieza[i][1] >= 60:
                pygame.draw.rect(pantalla, pieza[4], [pieza[i][0], pieza[i][1], 30,30])
                
        for i in range(4): #borde pieza
            if pieza[i][1] >= 60:
                pygame.draw.rect(pantalla, NEGRO, [pieza[i][0], pieza[i][1], 30,30], 2)

        for i in range(len(cuad)): #color puestas
            for j in range(len(cuad[0])):
                if cuad[i][j] != 0:
                    pygame.draw.rect(pantalla, cuad[i][j], [(j+2)*30, (i+2)*30, 30,30])

        for i in range(len(cuad)): #borde puestas
            for j in range(len(cuad[0])):
                if cuad[i][j] != 0:
                    pygame.draw.rect(pantalla, NEGRO, [(j+2)*30, (i+2)*30, 30,30], 2)
                    
        fuente = pygame.font.Font(None, 75)
        cad = 'Puntos: '+str(puntos)
        txt = fuente.render(cad , True, (0,0,0))
        pantalla.blit(txt, [60,700])
        
    pygame.display.flip()
    reloj.tick(3)

pygame.quit()
