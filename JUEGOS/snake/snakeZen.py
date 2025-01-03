import pygame
from random import randrange
from pygame.locals import *

class Snake:
    def __init__(self, t):
        self.v = [-1, 0] #direccion y sentido

        self.length = 5
        self.cola = [[0, 0] for i in range(self.length)]

        self.puntos = 0
        self.t = t

    def mover(self, newV, crece):
        dir = newV[0]
        sentido = newV[1]

        for i in range(self.length):
            self.cola[i][dir] += sentido


        if(not crece):
            self.cola.pop(self.length-1)
        else:
            self.length += 1
            self.puntos += 1

        self.cola.insert(0, [0, 0])
    
        self.v = newV + []
        







def visible(x, c, t):
    return -t <= c[0] + x[0]*t < c[0]*2 and -t <= c[1] + x[1]*t < c[1]*2


def creaCom(lim):
    x = [randrange(-lim, lim), randrange(-lim, lim)]
    while x in serpiente.cola:
        x = [randrange(-lim, lim), randrange(-lim, lim)]

    x[0] = centro[0] + x[0]*serpiente.t
    x[1] = centro[1] + x[1]*serpiente.t

    return x

#================================================================================================================

NEGRO = (0, 0 ,0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

dimensiones = [1000, 1000]
centro = [int(dimensiones[0]/2), int(dimensiones[1]/2)]

vel = [-1, 0]
tam = 40
serpiente = Snake(t=tam)
posCom = creaCom(int(dimensiones[0]/tam))
fps = 15


pygame.init()
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption('SnakeZen')
hecho = False
reloj = pygame.time.Clock()

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
for joystick in joysticks:
    print(joystick.get_name())



while not hecho:
    for evento in pygame.event.get():
        #print(evento)
        if evento.type == pygame.QUIT: 
            hecho = True
        
        elif evento.type == pygame.JOYBUTTONDOWN:
            
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                if vel[0] != 0:
                    vel = [0,  1]
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                if vel[0] != 0:
                    vel = [0, -1]
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                if vel[0] != 1:
                    vel = [1,  1]
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                if vel[0] != 1:
                    vel = [1, -1]

        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                if vel[0] != 0:
                    vel = [0,  1]
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                if vel[0] != 0:
                    vel = [0, -1]
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                if vel[0] != 1:
                    vel = [1,  1]
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                if vel[0] != 1:
                    vel = [1, -1]

            '''   
            if evento.key == pygame.K_r: #reset
                vel = [0,0]
                puntos = 0
                cola = []
                for i in range(3):
                    cola.append([-1*(i-1)*15, 15])
                perder = False
                posCom = creaCom()'''

    #-------------------------------------------LOGICA----------------------------------------

    posCom[vel[0]] += vel[1]*tam
    come = (posCom == centro)
    serpiente.mover(vel, come)

    if(come):
        posCom = creaCom(int(dimensiones[0]/tam))


    '''
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
        if posCom == cola[0]:
            posCom = creaCom()
            puntos += 1
            cola.append([None])
            if puntos % 10 == 0:
                fps += 2
            print(puntos)'''
            
    #-------------------------------------------DIBUJO----------------------------------------
    

    pantalla.fill(NEGRO)

    fuente = pygame.font.Font(None, 500)
    txt = fuente.render(str(serpiente.puntos), True, (50, 50, 50))
    pantalla.blit(txt, [300,200])
    
        

    pygame.draw.rect(pantalla, ROJO, [posCom[0]+2, posCom[1]+2, tam-4, tam-4])
    pygame.draw.rect(pantalla, VERDE, [posCom[0]+2*tam/5, posCom[1]-tam/5, tam/5, 3*tam/5])


        
    for i in range(serpiente.length):
        x = serpiente.cola[i]
        if(visible(x, centro, serpiente.t)):
            pygame.draw.rect(pantalla, VERDE, [centro[0]+x[0]*serpiente.t+2, 
                                               centro[1]+x[1]*serpiente.t+2, serpiente.t-4, serpiente.t-4])
            if(i<serpiente.length-1):
                y = serpiente.cola[i+1]
                pygame.draw.line(pantalla, VERDE, [centro[0]+ (x[0]+0.5)*serpiente.t, centro[1]+ (x[1]+0.5)*serpiente.t],
                                                  [centro[0]+ (y[0]+0.5)*serpiente.t, centro[1]+ (y[1]+0.5)*serpiente.t], 5)

    pygame.draw.line(pantalla, (255, 255, 255), [p+serpiente.t/2 for p in posCom] , [p+serpiente.t/2 for p in centro])

    if(vel[0] == 0):
        pygame.draw.rect(pantalla, NEGRO, [centro[0]+serpiente.t/5, centro[1]+serpiente.t/5, 3*serpiente.t/5, serpiente.t/5])
        pygame.draw.rect(pantalla, NEGRO, [centro[0]+serpiente.t/5, centro[1]+3*serpiente.t/5, 3*serpiente.t/5, serpiente.t/5])
    else:
        pygame.draw.rect(pantalla, NEGRO, [centro[0]+serpiente.t/5, centro[1]+serpiente.t/5, serpiente.t/5, 3*serpiente.t/5])
        pygame.draw.rect(pantalla, NEGRO, [centro[0]+3*serpiente.t/5, centro[1]+serpiente.t/5, serpiente.t/5, 3*serpiente.t/5])

    pygame.display.flip()
    reloj.tick(fps)

pygame.quit()
