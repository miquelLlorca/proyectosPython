import pygame
import random
import numpy as np


NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)
FONDO = (158, 158, 157)
ENEMY_COLORS = [
    (230, 23, 23), # rojo claro
    (179, 21, 21), # rojo osc
    (73, 133, 230), # azul claro
    (50, 101, 184), # azul osc
    (78, 222, 104), # verde claro
    (55, 153, 73), # verde osc
    (255, 61, 226), # rosa claro
    (194, 39, 171)  # rosa osc
]

ENEMY_SIZES = [
    [3, 10],
    [6, 15]
]
OFFSET = 100
NIVEL = 0
#       vmin, vmax, rmin, rmax
DATA = [[5, 10, 5, 10, 100],
    [10, 15, 10, 20, 125],
    [15, 20, 20, 40, 150],
    [20, 30, 35, 44, 175]
]
class Circulo:
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.bbX = x-r
        self.bbY = y-r
        self.r = r
        self.d = r*2
        self.a = [0, 0]
        self.b = [0, 0]
        self.v = [0, 0]
        self.color = color

    
    def Distancia(self, other):
        sumaRadios = self.r + other.r        
        dx = abs(self.x - other.x)
        if(dx >= sumaRadios):
            return False

        dy = abs(self.y - other.y)
        if(dy >= sumaRadios):
            return False

        dp = np.sqrt(dx**2 + dy**2)
        return dp <= sumaRadios

    
    def Colisiones(self, others):
        for other in others:
            if(self.Distancia(other)):
                return True
        return False


    def CreaRuta(self):
        """
           1
         _____
        0|   |2
         |___|
           3
        
        elige un lado del que salir y uno al que llegar, siempre distintos
        """


        dp = np.random.randint(0,dims[0]+200)
        ladoA = np.random.randint(0,4)
        
        if(ladoA == 0):
            self.a = [-OFFSET, dp]
        elif(ladoA == 1):
            self.a = [dp, -OFFSET]
        elif(ladoA == 2):
            self.a = [dims[0]+OFFSET, dp]
        elif(ladoA == 3):
            self.a = [dp, dims[1]+OFFSET]

        dp = np.random.randint(0,dims[0])
        ladoB = np.random.randint(0,3)
        while(ladoB == ladoA):
            ladoB = np.random.randint(0,4)

        if(ladoB == 0):
            self.b = [0, dp]
        elif(ladoB == 1):
            self.b = [dp, 0]
        elif(ladoB == 2):
            self.b = [dims[0], dp]
        elif(ladoB == 3):
            self.b = [dp, dims[1]]


        self.x, self.y = self.a
        self.v = [self.b[i] - self.a[i] for i in range(2)]
        media = np.sqrt(self.v[0]**2 + self.v[1]**2)
        v = np.random.randint(DATA[NIVEL][0], DATA[NIVEL][1])
        self.v = [100*x/media for x in self.v]
        self.f = np.random.randint(DATA[NIVEL][2], DATA[NIVEL][3])
        self.bbX = self.x-self.r
        self.bbY = self.y-self.r


    def SetPos(self, pos):
        self.x, self.y = pos
        self.bbX = self.x-self.r
        self.bbY = self.y-self.r


    def Mover(self, dt):
        self.x += dt*self.v[0]
        self.y += dt*self.v[1]
            
        self.bbX = self.x-self.r
        self.bbY = self.y-self.r

        dx = (-OFFSET-10 <= self.x <= OFFSET+dims[0]+10)
        dy = (-OFFSET-10 <= self.y <= OFFSET+dims[0]+10)
        if(not (dx and dy)):
            self.CreaRuta()


    def Draw(self, pantalla):
        if(self.color == -1):
            pygame.draw.ellipse(pantalla, BLANCO, [self.bbX, self.bbY, self.d, self.d])
            #pygame.draw.ellipse(pantalla, NEGRO, [self.bbX, self.bbY, self.d, self.d], 2)
        else:
            pygame.draw.ellipse(pantalla, ENEMY_COLORS[self.color], [self.bbX, self.bbY, self.d, self.d])

# ========================================================================================

if(__name__ == "__main__"):
    nEne = 100
    dims = [1000,1000]
    c = int(dims[0]/2)
    level = 1

    player = Circulo(x=c, y=c, r=25, color=-1)
    enemies = [Circulo(x=c, y=c, r=np.random.randint(ENEMY_SIZES[level][0], ENEMY_SIZES[level][1]), 
                color=np.random.randint(0, len(ENEMY_COLORS))) 
                for i in range(nEne)]
    #np.full(fill_value=Circulo(x=c, y=c, r=25), shape=(nEne), dtype=Circulo)

    for i in range(nEne):
        enemies[i].CreaRuta()

    fps = 60
    dead = False
    started = False

    pygame.init()
    pantalla = pygame.display.set_mode(dims) 
    pygame.display.set_caption("Polka Dots!!!!!")
    hecho = False
    reloj = pygame.time.Clock()

    while not hecho:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                hecho = True

            if evento.type == pygame.KEYDOWN:
                started = True

                if(evento.key == pygame.K_r):
                    player = Circulo(x=c, y=c, r=25, color=-1)
                    enemies = [Circulo(x=c, y=c, r=np.random.randint(ENEMY_SIZES[level][0], ENEMY_SIZES[level][1]), 
                                color=np.random.randint(0, len(ENEMY_COLORS))) 
                                for i in range(nEne)]
                    for i in range(nEne):
                        enemies[i].CreaRuta()

                    fps = 60
                    dead = False

        # ---------------------------------------------------LÓGICA---------------------------------------------------
        pos = pygame.mouse.get_pos()
        player.SetPos(pos)

        if(started and not dead):
            for i in range(nEne):
                enemies[i].Mover(1/fps)

            dead = player.Colisiones(enemies)
        # ---------------------------------------------------DIBUJO---------------------------------------------------

        pantalla.fill(FONDO)


        if(dead):
            # guarda datos
            # imprime stats
            # boton restart
            
            print("MUERRTE")
        else:
            player.Draw(pantalla)
            for i in range(nEne):
                enemies[i].Draw(pantalla)


        # fuente = pygame.font.Font(None, 75)
        # txt = fuente.render('GAME OVER', True, (0,0,0))
        # pantalla.blit(txt, [200,300])

        pygame.display.flip()
        reloj.tick(fps)

    pygame.quit()
