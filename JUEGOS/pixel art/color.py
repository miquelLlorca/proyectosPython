import pygame
from PIL import Image
import numpy as np
import cv2

ALTO_SELECT = 25
ALTO = ALTO_SELECT*5# 25 + 25 + 25 
BORDE = 25
ANCHO = 255 + 2*BORDE # 10 + 255 + 10 

class ColorPicker:
    def __init__(self, pos):
        self.pos = pos
        self.selected = [0, 0, 0]
        self.prev = [0, 0, 0]
        self.move = False
        self.visible = True


    def Click(self, click):
        if( not (self.pos[0] <= click[0] <= self.pos[0]+ANCHO and 
            self.pos[1] <= click[1] <= self.pos[1]+ALTO)):
            return False


        if(click[1] - self.pos[1] < ALTO_SELECT):
            self.move = True

        elif(click[1] - self.pos[1] < ALTO_SELECT*2): # ROJO
            self.selected[0] = click[0] - self.pos[0] - BORDE
        
        elif(click[1] - self.pos[1] < ALTO_SELECT*3): # VERDE
            self.selected[1] = click[0] - self.pos[0] - BORDE
            self.selected[1] = self.selected[1] if self.selected[1] <= 255 else 255
        
        elif(click[1] - self.pos[1] < ALTO_SELECT*4): # AZUL
            self.selected[2] = click[0] - self.pos[0] - BORDE
            self.selected[2] = self.selected[2] if self.selected[2] <= 255 else 255

        
        for i in range(3):
            self.selected[i] = self.selected[i] if self.selected[i] <= 255 else 255
            self.selected[i] = self.selected[i] if self.selected[i] >= 0 else 0
        
        return True

    def UnClick(self):
        self.move = False


    def Move(self, dP):
        self.pos[0] -= dP[0]
        self.pos[1] -= dP[1]


    def Draw(self, pantalla):
        pygame.draw.rect(pantalla, (255, 255, 255), [self.pos[0], self.pos[1], ANCHO, ALTO]) # fondo

        pygame.draw.rect(pantalla, (150, 150, 150), [self.pos[0], self.pos[1], ANCHO, ALTO_SELECT]) # barra para mover

        pygame.draw.rect(pantalla, (255, 000, 000), [self.pos[0]+BORDE, self.pos[1]+ALTO_SELECT, ANCHO-2*BORDE, ALTO_SELECT]) # ROJO
        pygame.draw.rect(pantalla, (000, 255, 000), [self.pos[0]+BORDE, self.pos[1]+ALTO_SELECT*2, ANCHO-2*BORDE, ALTO_SELECT]) # VERDE
        pygame.draw.rect(pantalla, (000, 000, 255), [self.pos[0]+BORDE, self.pos[1]+ALTO_SELECT*3, ANCHO-2*BORDE, ALTO_SELECT]) # AZUL

        pygame.draw.rect(pantalla,   self.selected, [self.pos[0], self.pos[1]+ALTO_SELECT*4, ANCHO, ALTO_SELECT]) # color seleccionado
        pygame.draw.rect(pantalla, (000, 000, 000), [self.pos[0], self.pos[1], ANCHO, ALTO], 5) # bordes

        for i in range(3):
            x = self.pos[0]+BORDE+self.selected[i]
            pygame.draw.line(pantalla, (000, 000, 000), [x, self.pos[1]+ALTO_SELECT*(i+1)], [x, self.pos[1]+ALTO_SELECT*(i+2)], 2)



##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################


def ColorToKey(c):
    return f"{c[0]},{c[1]},{c[2]}"
def KeyToColor(k):
    return [int(x) for x in k.split(",")]



TAM_CELDA = 50


# faltan funciones para guardar/cargar dibujos
# estructura datos:
# { "255,255,255": [(x0,y0), (x1,y1) ...], ...}

class Tablero:
    def __init__(self):
        self.origen = [-9, -9]
        self.escala = 1

        self.pintados = {}

        self.min = [100000, 100000]
        self.max = [-100000, -100000]

        

    def Move(self, v):
        VEL = 5
        self.origen[0] += v[0]*VEL
        self.origen[1] += v[1]*VEL


    def Escalar(self, dx, dim):
        c = [dim[i]*self.escala/2 - self.origen[i] for i in [0,1]]
        self.escala *= dx
        self.origen = [dim[i]*self.escala/2 + self.origen[i]  for i in [0,1]]


    def Borrar(self, pos):
        x = pos[0] - self.origen[0]
        x = int(x/TAM_CELDA)
        y = pos[1] - self.origen[1]
        y = int(y/TAM_CELDA)

        for col in self.pintados:
            if((x,y) in self.pintados[col]):
                self.pintados[col].remove((x,y))
                return True
        return False


    def Pintar(self, pos, color, normalized = False):
        if(not normalized):
            x = pos[0] - self.origen[0]
            x = int(x/TAM_CELDA)
            y = pos[1] - self.origen[1]
            y = int(y/TAM_CELDA)
        else:
            x, y = pos

        key = ColorToKey(color)
        self.Borrar(pos)

        if(not (key in self.pintados)):
            self.pintados[key] = []

        self.pintados[key] += [(x,y)]

        if(x < self.min[0]):
            self.min[0] = x
        if(y < self.min[1]):
            self.min[1] = y

        if(x > self.max[0]):
            self.max[0] = x
        if(y > self.max[1]):
            self.max[1] = y


    def GetRect(self, pos):
        x = pos[0]
        y = pos[1]
        X = TAM_CELDA*x*self.escala + self.origen[0]
        Y = TAM_CELDA*y*self.escala + self.origen[1]
        tam = TAM_CELDA*self.escala
        return [X, Y, tam, tam]


    def DrawImage(self, image):
        paleta = image.GetPalette()
        img = image.GetArray()
        for i in range(len(img)):
            for j in range(len(img[0])):
                self.Pintar((i,j), paleta.getcolor(img[i][j]), normalized=True)
        return

    def Draw(self, pantalla):
        centro = [0-self.origen[i]*self.escala*TAM_CELDA   for i in [0,1]]
        pygame.draw.ellipse(pantalla, (0,0,0), [centro[0], centro[1], 10, 10])

        for k in self.pintados:
            color = KeyToColor(k)
            for pos in self.pintados[k]:
                pygame.draw.rect(pantalla, color, self.GetRect(pos))



##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################

class PixelArtImage:
    def __init__(self, path):
        self.path = path
        self.image = []
        self.simplified = []

    def LoadImage(self):
        self.image = Image.open(self.path)
        #print(self.image)
        #self.image = np.asarray(self.image)
        return

    def Simplify(self, factor):
        # empezar con puntos random o con cuadricula
        # de ahi expandir e ir juntando regiones
        print(self.image.getpixel((0, 1)))
        return

    def Resize(self, dims):
        self.image = self.image.resize(dims)
        return
    
    def Show(self):
        self.image.show()

    def GetArray(self):
        return np.asarray(self.image)

    def GetPalette(self):
        return self.image.palette

if(__name__ == "__main__"):
    '''a = {}
    a["a"] = [1,2,3,4,5]
    a["b"] = [6,7,8,9,10]
    a["c"] = [11,12,13,14,15]
    

    for c in a:
        print(a[c])

    '''
    
    path = "/home/miquel/Downloads/Fondo-de-Ubuntu-22.04.png"
    img = PixelArtImage(path)
    img.LoadImage()
    #img.Simplify(1)
    img.Resize((10,5))
    img.Show()