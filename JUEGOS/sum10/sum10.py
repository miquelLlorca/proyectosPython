import pygame
import random

from pygame import event

FONDO = (150, 150, 150)
SELECT = (0, 150, 200)
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)


class Tablero:
    def __init__(self):
        self.seleccion = [-1, -1]
        self.filas = []
        for i in range(3):
            self.filas.append([])
            for j in range(9):
                self.filas[i].append(random.randint(1, 9))


    def Ajustar(self):
        lineas = []
        for i in range(len(self.filas)):
            if(not (True in [n!=-1 for n in self.filas[i]])):
                lineas.append(i)

        for n in lineas[::-1]:
            self.filas.pop(n)


    def Extender(self):
        newNums = []
        for i in range(len(self.filas)):
            for j in range(len(self.filas[i])):
                if(self.filas[i][j] != -1):
                    newNums.append(self.filas[i][j])

        for n in newNums:
            if(len(self.filas[len(self.filas)-1]) == 9):
                self.filas.append([])
            self.filas[len(self.filas)-1].append(n)


    def Seleccionar(self, pos, res):
        x = (pos[1]//50)
        y = (pos[0]//50)

        if(self.seleccion == [-1, -1]):
            self.seleccion = [x, y]
            return

        previo = self.seleccion + []
        self.seleccion = [x, y]
        
        if(x >= len(self.filas) or previo[0] >= len(self.filas)):
            return
        if(x == len(self.filas) and y >= len(self.filas[len(self.filas)-1])):
            return
        if(previo[0] == len(self.filas) and previo[1] >= len(self.filas[len(self.filas)-1])):
            return



        diff = [previo[0]-x, previo[1]-y]

        if(diff[0] == 0 and diff[1] == 0): # selecciona el mismo
            return
        

        a = self.filas[previo[0]][previo[1]]
        b = self.filas[x][y]
        print(a, b)
        if(a == -1 or b == -1): # uno de los seleccionados es -1
            return


        # seleccion horizontal
        if(diff[0] == 0 and diff[1] != 0): 
            if(abs(diff[1]) != 1):
                dir = int(diff[1]/abs(diff[1]))
                aux = y + dir

                while(aux != y+diff[1]): # se comprueban espacios vacios entre nums
                    if(self.filas[x][aux] != -1):
                        return
                    aux += dir

            if(a == b or a+b == 10):
                self.filas[previo[0]][previo[1]] = -1
                self.filas[x][y] = -1
                
            return


        # seleccion vertical
        if(diff[0] != 0 and diff[1] == 0): 
            if(abs(diff[0]) != 1):
                dir = int(diff[0]/abs(diff[0]))
                aux = x + dir

                while(aux != x+diff[0]): # se comprueban espacios vacios entre nums
                    if(self.filas[aux][y] != -1):
                        return
                    aux += dir

            if(a == b or a+b == 10):
                self.filas[previo[0]][previo[1]] = -1
                self.filas[x][y] = -1
  
            return


        # seleccion diagonal
        if(abs(diff[0]) == abs(diff[1])):  
            if(abs(diff[0]) != 1):
                dir1 = int(diff[0]/abs(diff[0]))
                dir2 = int(diff[1]/abs(diff[1]))
                aux1 = x + dir1
                aux2 = y + dir2
                while(aux1 != x+diff[0]): # se comprueban espacios vacios entre nums
                    if(self.filas[aux1][aux2] != -1):
                        return
                    aux1 += dir1
                    aux2 += dir2

            if(a == b or a+b == 10):
                self.filas[previo[0]][previo[1]] = -1
                self.filas[x][y] = -1
  
            return


        # seleccion de ultimo de linea al primero de la siguiente
        if(diff[0] != 0 and abs(diff[1]) == 1): 
            menorY, aux, aux2 = (previo[1], previo[0], x) if previo[1] < y else (y, x, previo[0])
   
            while(aux < 9):
                if(self.filas[aux][menorY] != -1): # esto se supone que compueba el final de la linea y el siguiente el principio
                    return
                aux += 1

            aux = 0
            while(aux < aux2):
                if(self.filas[aux][menorY+1] != -1):
                    return
                aux += 1

            if(a == b or a+b == 10):
                self.filas[previo[0]][previo[1]] = -1
                self.filas[x][y] = -1
            
            return
            




# ==============================================================================================================================================================


res = 50
dimensiones = [9*res,18*res]
tabl = Tablero()


pygame.init()
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Sum10")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

        if evento.type == pygame.MOUSEBUTTONDOWN:
            tabl.Seleccionar(pygame.mouse.get_pos(), res)
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                tabl.Extender()

    # ---------------------------------------------------LÓGICA---------------------------------------------------
    
    tabl.Ajustar()

    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(FONDO)


    pygame.draw.rect(pantalla, SELECT, [tabl.seleccion[1]*res, tabl.seleccion[0]*res, res, res])
    
    for i in range(8):
        pygame.draw.line(pantalla, NEGRO, [res*(i+1), 0], [res*(i+1), dimensiones[1]], 2)
        
    for i in range(17):
        pygame.draw.line(pantalla, NEGRO, [0, res*(i+1)], [dimensiones[0], res*(i+1)], 2)

    
    for i in range(len(tabl.filas)):
        for j in range(len(tabl.filas[i])):
            if(tabl.filas[i][j] != -1):
                fuente = pygame.font.Font(None, 75)
                txt = fuente.render(str(tabl.filas[i][j]), True, (50, 50, 50))
                pantalla.blit(txt, [j*res+12, i*res+4])



    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
