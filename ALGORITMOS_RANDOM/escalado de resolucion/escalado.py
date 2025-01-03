import pygame
from random import randrange

def creaCol():
    return (randrange(0,255), randrange(0,255), randrange(0,255))


NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

esc = 0
colores = []
for i in range(2):
    colores.append([creaCol(), creaCol()])


pygame.init()
dimensiones = [600, 600]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Escalado")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        if evento.type == pygame.KEYDOWN:
            if(evento.key == pygame.K_r):# reset
                esc = 0
                colores = []
                for i in range(2):
                    colores.append([creaCol(), creaCol()])
                    
            if(evento.key == pygame.K_KP_PLUS):# escalado
                esc += 1
                rng = len(colores)
                for i in range(rng-1, -1, -1): # amplia matriz
                    for j in range(rng-2, -1, -1):
                        colores[i].insert(j+1, 0)
                        colores[i].insert(j+2, 0)
                    if(i != rng-1):
                        colores.insert(i+1, [])
                        colores.insert(i+2, [])
                        for j in range(rng + (rng-1)*2):
                            colores[i+1].append(0)
                            colores[i+2].append(0)

                for i in range(0, len(colores), 3): # rellena matriz
                    if(colores[i][0] != 0):
                        for j in range(0, len(colores)-3, 3):
                            colores[i][j+1] = (int(abs(colores[i][j][0]*2/3 - colores[i][j+3][0]*1/3)),
                                               int(abs(colores[i][j][1]*2/3 - colores[i][j+3][1]*1/3)),
                                               int(abs(colores[i][j][2]*2/3 - colores[i][j+3][2]*1/3)))
                                               
                            colores[i][j+2] =(int(abs(colores[i][j][0]*1/3 - colores[i][j+3][0]*2/3)),
                                               int(abs(colores[i][j][1]*1/3 - colores[i][j+3][1]*2/3)),
                                               int(abs(colores[i][j][2]*1/3 - colores[i][j+3][2]*2/3)))
                            
                     
                    if(colores[0][i] != 0):
                        for j in range(0, len(colores)-3, 3):
                            colores[j+1][i] = (int(abs(colores[j][i][0]*2/3 - colores[j+3][i][0]*1/3)),
                                               int(abs(colores[j][i][1]*2/3 - colores[j+3][i][1]*1/3)),
                                               int(abs(colores[j][i][2]*2/3 - colores[j+3][i][2]*1/3)))
                                               
                            colores[j+2][i] =(int(abs(colores[j][i][0]*1/3 - colores[j+3][i][0]*2/3)),
                                               int(abs(colores[j][i][1]*1/3 - colores[j+3][i][1]*2/3)),
                                               int(abs(colores[j][i][2]*1/3 - colores[j+3][i][2]*2/3)))
                            
                for i in range(len(colores)): # rellena matriz
                    if(colores[i][0] != 0 and colores[i][1]==0):
                        for j in range(0, len(colores)-3, 3):
                            colores[i][j+1] = (int(abs(colores[i][j][0]*2/3 - colores[i][j+3][0]*1/3)),
                                               int(abs(colores[i][j][1]*2/3 - colores[i][j+3][1]*1/3)),
                                               int(abs(colores[i][j][2]*2/3 - colores[i][j+3][2]*1/3)))
                                               
                            colores[i][j+2] =(int(abs(colores[i][j][0]*1/3 - colores[i][j+3][0]*2/3)),
                                               int(abs(colores[i][j][1]*1/3 - colores[i][j+3][1]*2/3)),
                                               int(abs(colores[i][j][2]*1/3 - colores[i][j+3][2]*2/3)))
                            
                     
                    if(colores[0][i] != 0  and colores[1][i]==0):
                        for j in range(0, len(colores)-3, 3):
                            colores[j+1][i] = (int(abs(colores[j][i][0]*2/3 - colores[j+3][i][0]*1/3)),
                                               int(abs(colores[j][i][1]*2/3 - colores[j+3][i][1]*1/3)),
                                               int(abs(colores[j][i][2]*2/3 - colores[j+3][i][2]*1/3)))
                                               
                            colores[j+2][i] =(int(abs(colores[j][i][0]*1/3 - colores[j+3][i][0]*2/3)),
                                               int(abs(colores[j][i][1]*1/3 - colores[j+3][i][1]*2/3)),
                                               int(abs(colores[j][i][2]*1/3 - colores[j+3][i][2]*2/3)))
                    
                            
                        
            if(evento.key == pygame.K_KP_MINUS): 
                esc -= 1
    # ---------------------------------------------------LÓGICA---------------------------------------------------
  
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(BLANCO)
    '''
    c1 = creaCol()
    pygame.draw.rect(pantalla, c1, [0,0, 80, 80])
    c2 = creaCol()
    pygame.draw.rect(pantalla, c2, [160,0, 80, 80])


    c3 = (int(abs(c1[0]-c2[0])/2), int(abs(c1[1]-c2[1])/2), int(abs(c1[2]-c2[2])/2))
    pygame.draw.rect(pantalla, c3, [80,0, 80, 80])
    '''
    t = dimensiones[0]/len(colores)
    
    for i in range(len(colores)):
        for j in range(len(colores)):
            pygame.draw.rect(pantalla, colores[i][j], [t*i, t*j, t, t])
    

        
    pygame.display.flip()
    reloj.tick(5)

pygame.quit()
