import pygame
from random import randrange
from A_estrella import *

dimBloques = [50, 50]
tam = 20
dimensiones = [dimBloques[0]*tam, dimBloques[1]*tam]


def creaCom(x, y):
    x = [randrange(1,x)*tam, randrange(1,y)*tam]
    return x



class Snake:
    def __init__(self, length):
        self.puntos = 0
        self.cola = []
        self.length = length
        for i in range(length):
            self.cola.append([-1*(i-1)*tam, tam])

        self.mapa = dimBloques + []
        self.tam = tam
        self.maxProf = 3
        self.camino = []
        self.comida = creaCom(dimBloques[0], dimBloques[1])



    def Update(self):

        # si come se actualiza la comida, el camino el timer y la profundidad
        # si no, se mira si ha acbado el timer
        # se mueve la serpiente

        come = False

        if(self.cola[0] == self.comida):
            self.puntos += 1
            self.comida = creaCom(dimBloques[0], dimBloques[1]) 
            while(self.comida in self.cola):
                self.comida = creaCom(dimBloques[0], dimBloques[1]) 

            A_Estrella(self, self.cola[0], self.comida, self.camino, DistanciaBloques, self.maxProf)

            if(self.puntos+1 == 10):
                self.maxProf = 100
            '''elif(self.puntos+1 == 20):
                self.maxProf = 25
            elif(self.puntos+1 == 30):
                self.maxProf = 50
            elif(self.puntos+1 == 50):
                self.maxProf = 50000'''

            come = True

        else:
            if(self.camino == []):
                A_Estrella(self, self.cola[0], self.comida, self.camino, DistanciaBloques, self.maxProf)
        

        self.cola.insert(0, self.camino[0])

        if(not come):
            self.cola.pop(len(self.cola)-1)

        self.camino.pop(0)
        
        





NEGRO = (0, 0 ,0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)



perder = False
snake = Snake(5)



pygame.init()
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption('Snake')
hecho = False
reloj = pygame.time.Clock()

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
            '''
            if evento.key == pygame.K_r: #reset
                puntos = 0
                cola = []
                for i in range(largo):
                    cola.append([-1*(i-1)*15, 15])
                perder = False
                posCom = creaCom()
                dx = cola[0][0]-posCom[0]
                dy = cola[0][1]-posCom[1]
                vel = inicia(dx, dy)'''
                


    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ
    
    snake.Update()
        
        
    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ
    if not perder: 
        pantalla.fill(NEGRO)

        if snake.puntos < 10:
            fuente = pygame.font.Font(None, 500)
            txt = fuente.render(str(snake.puntos), True, (50, 50, 50))
            pantalla.blit(txt, [300,200])
        elif snake.puntos <100:
            fuente = pygame.font.Font(None, 500)
            txt = fuente.render(str(snake.puntos), True, (50, 50, 50))
            pantalla.blit(txt, [175,200])
        elif snake.puntos <1000:
            fuente = pygame.font.Font(None, 500)
            txt = fuente.render(str(snake.puntos), True, (50, 50, 50))
            pantalla.blit(txt, [100,200])
            
        pygame.draw.rect(pantalla, ROJO, [snake.comida[0]+1, snake.comida[1]+1, tam-2, tam-2])
            
        for x in snake.cola:
            pygame.draw.rect(pantalla, VERDE, [x[0]+1, x[1]+1,  tam-2, tam-2])

        for i in range(len(snake.cola)-1):
            pygame.draw.line(pantalla, VERDE, [snake.cola[i][0]+tam/2, snake.cola[i][1]+tam/2], [snake.cola[i+1][0]+tam/2, snake.cola[i+1][1]+tam/2], 5)

        pygame.draw.rect(pantalla, ROJO, [snake.comida[0]+1, snake.comida[1]+1,  tam-2, tam-2])
    
    else:
        pantalla.fill(ROJO)
        fuente = pygame.font.Font(None, 75)
        txt = fuente.render('GAME OVER', True, (0,0,0))
        txt2 = fuente.render('Press R to restart', True, (0,0,0))
        pantalla.blit(txt, [200,300])
        pantalla.blit(txt2, [150, 360])
     
    pygame.display.flip()
    reloj.tick(240)

pygame.quit()
