from pydoc import cli
import pygame
import random
from PIL import Image
import numpy as np
from pygame.constants import TEXTEDITING



# convierte la imagen a array de numpy 
# luego a array normal quitandole el valor alpha (si lo tiene)
def GetArray(imagen, escala): 
    data = []
    orig = np.asarray(imagen)

    X = int(len(orig)/escala)
    Y = int(len(orig[0])/escala)


    for i in range(X):
        data.append([])

        for j in range(len(orig[i])):
            data[i].append([])
            for k in range(3):
                x = i*escala
                y = j*escala
                if(i*escala >= len(orig)):
                    x = len(orig)-1
                if(j*escala >= len(orig[i])):
                    y = len(orig[i])-1
                
                data[i][j].append(orig[x][y][k])

    return data + []


def GrisearColor(a):
    suma = 0
    for c in a:
        suma += c
    return int(suma/3)


def DiferenciaColor(a, b):
    return abs(GrisearColor(a) - GrisearColor(b))


def MediaPixeles(foto, x, y, res):
    suma = 0
    for i in range(res):
        for j in range(res):
            if(not(x+i>=len(foto)) and not(y+j>=len(foto[0]))):
                suma += GrisearColor(foto[x+i][y+j])
    return int(suma/(res*res))


def Distancia(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5


def CalculaDistancia(clicks):
    print("Clicks:", clicks)
    unidad = Distancia(clicks[0], clicks[1])
    print("Unidad:", unidad)

    largo = Distancia(clicks[2], clicks[3])
    print("Largo:", largo)

    print("Tam. real:",largo/unidad)

    

class Pixeles:
    def __init__(self, imagen, escala):
        self.originalData = GetArray(imagen, escala)
        self.data = self.originalData*1
        self.histData = []

        self.x = len(self.originalData)
        self.y = len(self.originalData[0])

        self.original = False
        self.histograma = False
        self.pantalla = None
        

    def Original(self, imagen):
        self.originalData = GetArray(imagen)
        self.original = True
        self.histograma = False

    def Invertir(self):
        self.original = False
        for i in range(self.x):
            for j in range(self.y):
                for c in range(3):
                    self.data[i][j][c] -= 255
                    self.data[i][j][c] = abs(self.data[i][j][c])
            if(i%100 == 0):
                self.Draw()
    

    def EscalaGrises(self):
        self.original = False
        for i in range(self.x):
            for j in range(self.y):
                for c in range(3):
                    self.data[i][j][c] = GrisearColor(self.originalData[i][j])
            #if(i%100 == 0):
            #    self.Draw()


    def Brillo(self, dir):
        self.original = False
        for i in range(self.x):
            for j in range(self.y):
                for c in range(3):
                    self.data[i][j][c] += dir*25 # dir * cantidad
                    self.data[i][j][c] = 0 if self.data[i][j][c] < 0 else self.data[i][j][c]
                    self.data[i][j][c] = 255 if self.data[i][j][c] > 255 else self.data[i][j][c]
            if(i%100 == 0):
                self.Draw()
        

    def Histograma(self):
        self.EscalaGrises()
        self.histograma = True

        self.histData = []
        for i in range(256):
            self.histData.append(0)

        for i in range(self.x):
            for j in range(self.y):
                self.histData[self.data[i][j][0]] += 1



    def Ecualizar(self):
        return 0


    def Aristas(self, minD):
        self.original = False
        self.histograma = False
        step = int(self.x/100)
        #print("################################################################################################################")
        #print(self.originalData[100:101])
        #print(self.originalData[0][0])
        for i in range(self.x):
            for j in range(self.y):
                if(i<self.x-1):
                    dC = DiferenciaColor(self.originalData[i+1][j], self.originalData[i][j])
                    #print(dC, end="")
                    if(dC < minD):
                        #print(" A A A A A")
                        self.data[i][j] = [255, 255, 255]
                        pass
                    else:
                        self.data[i][j] = [dC, dC, dC]#[0, 0, 0]
                    
                if(j<self.y-1):
                    dC = DiferenciaColor(self.originalData[i][j+1], self.originalData[i][j])
                
                
                    if(dC < minD):
                        self.data[i][j] = [255, 255, 255]
                    else:
                        self.data[i][j] = [dC, dC, dC]#[0, 0, 0]
                    
            #if(i == self.x-1):
            #    print("100%")
            #elif(i%step==0):
            #    print(f"{int(i/step)}%", end="\r")
        #print("################################################################################################################")
        #print(self.originalData[100:101])
        #print()
        #print("################################################################################################################")
        #print()
        #print()
        ##print(self.data[100:101])
        #print(len(self.data), len(self.data[0]))
        #print(len(self.originalData), len(self.originalData[0]))



    def ToAscii(self, resolution, type):
        self.EscalaGrises()
        
        txt = ""
        for i in range(self.x):
            if(i%resolution == 0):
                for j in range(self.y):
                    if(j%resolution == 0):
                        if(type == "media"):
                            gris = MediaPixeles(self.data, i, j, resolution)
                        elif(type == "discreto"):
                            gris = GrisearColor(self.data[i][j])
                        #print(gris, end=" ")
                        if(gris > 245):
                            txt += "  "
                        elif(gris > 235):
                            txt += ". "
                        elif(gris > 215):
                            txt += ".."
                        elif(gris > 200):
                            txt += "--"
                        elif(gris > 175):
                            txt += "-i"
                        elif(gris > 150):
                            txt += "ii"
                        elif(gris > 125):
                            txt += "o-"
                        elif(gris > 100):
                            txt += "xx"
                        elif(gris >  75):
                            txt += "X-"
                        elif(gris >  50):
                            txt += "XX"
                        elif(gris >  25):
                            txt += "@-"
                        elif(gris >=   0):
                            txt += "@@"


                        #txt += " "


                #print()
                txt += "\n"


        return txt


    def Draw(self, pantalla):
        pantalla.fill((128, 246, 255))
        if(not self.histograma):
            for i in range(self.x):
                for j in range(self.y):
                    if(self.original):
                        pygame.draw.rect(self.pantalla, (self.originalData[i][j][0], self.originalData[i][j][1], self.originalData[i][j][2]), [j, i, 1, 1])
                    else:
                        pygame.draw.rect(self.pantalla, (self.data[i][j][0], self.data[i][j][1], self.data[i][j][2]), [j, i, 1, 1])

        else:
            
            wide = int( (self.y - 20) / 256) + 0.25
            
            max = 0
            for i in range(256):
                if(self.histData[i] > max):
                    max = self.histData[i]

            
            for i in range(256):
                h = int(self.histData[i]/max*(self.x-50))
                pygame.draw.rect(self.pantalla, (i, i, i), [10 + i*wide, self.x-10-h, wide, h])
        pygame.display.flip()



if(__name__=="__main__"):     
    name = "latas.png" #input("Name: ")
    imagen = Image.open(name)
    
    escala = 1
    foto = Pixeles(imagen, escala)
    dimensiones = [foto.y, foto.x]
    brillo = False
    aristas = True
    edge_threshold = 150

    clicks = []

    print("- CONTROLES:")
    print("O - mostrar original")
    print("I - invertir colores")
    print("G - escala de grises")
    print("B - cambiar brillo")
    print("   + aumentar")
    print("   - disminuir")
    print("H - muestra histograma")
    print("E - ecualizar")
    print("A - aristas")




    pygame.init()
    pantalla = pygame.display.set_mode(dimensiones) 
    foto.pantalla = pantalla
    pygame.display.set_caption("Editor de fotos")
    hecho = False
    reloj = pygame.time.Clock()

    while not hecho:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                hecho = True

            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if(clicks==[] or pos != clicks[len(clicks)-1]):
                    clicks.append(pos)
                    print(clicks)
                if(len(clicks) == 4):
                    CalculaDistancia(clicks)
                    clicks = []

            if evento.type == pygame.KEYDOWN:

                if brillo:
                    if evento.key == pygame.K_PLUS:    
                        foto.Brillo(1)
                    if evento.key == pygame.K_MINUS:    
                        foto.Brillo(-1)

                if aristas:
                    if evento.key == pygame.K_PLUS:   
                        edge_threshold += 15 
                        foto.Aristas(edge_threshold)
                    if evento.key == pygame.K_MINUS: 
                        edge_threshold -= 15    
                        foto.Aristas(edge_threshold)
                
                if evento.key == pygame.K_i:    
                    foto.Invertir()
                    
                if evento.key == pygame.K_g:    
                    foto.EscalaGrises()
                
                if evento.key == pygame.K_a:    
                    foto.Aristas(edge_threshold)
                    aristas = True

                if evento.key == pygame.K_b:    
                    brillo = True

                if evento.key == pygame.K_h:    
                    if(foto.histograma):
                        foto.histograma = False
                    else:
                        foto.Histograma()

                if evento.key == pygame.K_o:
                    foto.Original(imagen)
                    



        # ---------------------------------------------------LÓGICA---------------------------------------------------
    
        # ---------------------------------------------------DIBUJO---------------------------------------------------

        #pantalla.fill(BLANCO)

        foto.Draw(pantalla)
        
        reloj.tick(60)

    pygame.quit()
