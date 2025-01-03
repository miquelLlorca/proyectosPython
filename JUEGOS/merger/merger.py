import pygame
import random
import numpy as np

NEGRO = (0, 0 ,0)
BLANCO = (255,255,255)

NO_CLICK = "a"
MAS_DINERO = "md"
MENOS_TIEMPO = "mt"
MEJORES_TILES = "mts"
IMG_DINERO = "/home/miquel/Pictures/upgradeDollar.png"
IMG_TIEMPO = "/home/miquel/Pictures/upgradeTime.png"
IMG_TILES = "/home/miquel/Pictures/upgradeDollar.png"
FPS = 60

TILECOLOR = {}
color_A = [0, 0, 255]
color_B = [255, 0, 255]
maxPower = 20
maxValue = 2**(maxPower+1)
diff = [(color_B[i]-color_A[i])/maxPower for i in range(3)]
for i in range(1,maxPower+1):
    TILECOLOR[2**i] = [int(color_A[j]+diff[j]*i) for j in range(3)]




# ====================================================================================================================================================================================

class Botones:
    def __init__(self):
        self.posiciones = []
        self.tamaños = []
        self.funciones = []
        self.sprites = []
        self.price = []

    def AddBoton(self, pos, tam, funcion, price, imagen):
        self.posiciones.append(pos)
        self.tamaños.append(tam)
        self.price.append(price)
        self.funciones.append(funcion)
        imagen.set_colorkey(BLANCO)
        self.sprites.append(imagen)

    def Click(self, pos):
        for i in range(len(self.posiciones)):
            click = [(self.posiciones[i][j] 
                      <= pos[j] 
                      <= self.posiciones[i][j]+self.tamaños[i][j])  
                      for j in range(2)]

            if(click[0] and click[1]):
                return self.funciones[i], self.price[i], i
        
        return NO_CLICK, -1, -1


    def UpdatePrice(self, i):
        self.price[i] += self.price[i]/2


    def Draw(self, pantalla):
        for i in range(len(self.funciones)):
            pantalla.blit(self.sprites[i], self.posiciones[i])


# ====================================================================================================================================================================================



class Tablero:
    def __init__(self, x, y, lado):
        self.t = np.zeros((x,y), dtype=int)
        self.t[0][0] = 2
        self.x = x
        self.y = y
        self.lado = lado

        self.seleccion = [-1,-1]
        self.cash = 0
        self.multiplier = 1
        self.timer = 0
        self.delay = 4
        self.newTile = 2

        self.botones = Botones()
    

    def InitializeButtons(self):
        self.botones.AddBoton(pos=[self.lado*(self.x-5), self.lado*self.y+10],
                              tam=[80, 80],
                              funcion=MEJORES_TILES,
                              price=100,
                              imagen=pygame.image.load(IMG_TILES).convert())

        self.botones.AddBoton(pos=[self.lado*(self.x-3), self.lado*self.y+10],
                              tam=[80, 80],
                              funcion=MAS_DINERO,
                              price=100,
                              imagen=pygame.image.load(IMG_DINERO).convert())

        self.botones.AddBoton(pos=[self.lado*(self.x-1), self.lado*self.y+10],
                              tam=[80, 80],
                              funcion=MENOS_TIEMPO,
                              price=100,
                              imagen=pygame.image.load(IMG_TIEMPO).convert())


    def GetDimensiones(self):
        return [self.x*self.lado, self.y*self.lado]

    def GetValue(self, pos):
        return self.t[pos[0]][pos[1]]

    def SetValue(self, pos, v):
        self.t[pos[0]][pos[1]] = v


    def Click(self, pos):
        if(pos[1] < self.y*self.lado):
            self.Select(pos)
        else:
            boton, price, pos = self.botones.Click(pos)
            print(boton)
            if(boton == MAS_DINERO and self.cash > price):
                self.cash -= price
                self.multiplier *= 2
                self.botones.UpdatePrice(pos)
            elif(boton == MENOS_TIEMPO and self.cash > price):
                self.cash -= price
                self.delay /= 2
                self.botones.UpdatePrice(pos)
            elif(boton == MEJORES_TILES and self.cash > price):
                self.cash -= price
                self.newTile *= 2
                self.botones.UpdatePrice(pos)


    def Select(self, pos):
        self.seleccion = [int(p/self.lado) for p in pos]
    
    def DeSelect(self, pos):
        if(self.seleccion == [-1, -1]):
            return

        newPos = [int(p/self.lado) for p in pos]
        if(newPos == self.seleccion):
            self.seleccion = [-1,-1]
            return
        v = self.GetValue(self.seleccion)
        newV = self.GetValue(newPos)

        if(newV == 0):
            self.SetValue(newPos, v)
            self.SetValue(self.seleccion, 0)
        elif(newV == v):
            self.SetValue(newPos, v*2)
            self.SetValue(self.seleccion, 0)

        self.seleccion = [-1,-1]


    def Update(self):
        self.timer += 1
        found = False
        if(self.timer >= int(self.delay*FPS)):
            # Genera nuevo tile
            for i in range(self.x):
                for j in range(self.y):
                    if(self.t[i][j] == 0):
                        if(self.cash > self.multiplier*self.newTile / 2):
                            self.cash -= self.multiplier*self.newTile / 2
                            self.t[i][j] = self.newTile
                            found = True
                        break

                if(found):
                    break
            
            # Suma $
            
            for i in range(self.x):
                for j in range(self.y):
                    self.cash += self.multiplier * self.t[i][j]
            

            self.timer = 0

        return


    def Draw(self, pantalla, dimensiones):

        for i in range(self.x): 
            for j in range(self.y):
                if([i,j] == self.seleccion):
                    continue
                if(self.t[i][j] != 0):
                    pygame.draw.rect(pantalla, TILECOLOR[self.t[i][j]], [i*self.lado, j*self.lado, self.lado, self.lado])
                    fuente = pygame.font.Font(None, 75)
                    txt = fuente.render(str(self.t[i][j]), True, (0,0,0))
                    pantalla.blit(txt, [i*self.lado + 10, j*self.lado])
        
        for i in range(self.x):
            pygame.draw.line(pantalla, NEGRO, [i*self.lado, 0], [i*self.lado, self.y*self.lado], 1)

        for i in range(self.y+1):
            pygame.draw.line(pantalla, NEGRO, [0, i*self.lado], [self.y*self.lado, i*self.lado], 1)

        # Dibujar tile en movimiento

        # Botones y data
        
        fuente = pygame.font.Font(None, 75)
        txt = fuente.render(str(self.cash)+"$", True, (0,0,0))
        pantalla.blit(txt, [10, self.y*self.lado+10])
        
        
        self.botones.Draw(pantalla)



# MAIN =================================================================================================================

if(__name__ == "__main__"):

    tabl = Tablero(8, 8, 100)

    dimensiones = tabl.GetDimensiones()
    dimensiones[1] += 100 # para poner datos


    pygame.init()
    pantalla = pygame.display.set_mode(dimensiones) 
    pygame.display.set_caption("Merger")
    hecho = False
    reloj = pygame.time.Clock()
    tabl.InitializeButtons()

    while not hecho:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                hecho = True

            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                tabl.Click(pos)
            if evento.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                tabl.DeSelect(pos)

        # LÓGICA---------------------------------------------LÓGICA---------------------------------------------LÓGICA
        pos = pygame.mouse.get_pos()

        tabl.Update()
        # DIBUJO---------------------------------------------DIBUJO---------------------------------------------DIBUJO

        pantalla.fill((100, 100, 100))

        tabl.Draw(pantalla, dimensiones)
        #fuente = pygame.font.Font(None, 75)
        #txt = fuente.render('GAME OVER', True, (0,0,0))
        #pantalla.blit(txt, [200,300])

        pygame.display.flip()
        reloj.tick(FPS)

    pygame.quit()
