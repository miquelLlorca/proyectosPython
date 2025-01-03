import pygame
from random import randint

class Celda:
    def __init__(self, n, mover, mezclar):
        self.n = n
        self.mover = mover
        self.mezclar = mezclar





class Tablero:
    def __init__(self, n, pos, t):
        self.t = int(t/n)
        self.pos = pos
        self.n = n
        self.tablero = []
        for i in range(n):
            self.tablero.append([])
            for j in range(n):
                self.tablero[i].append(Celda(0, False, False))
        
        self.tablero[randint(0, n-1)][randint(0, n-1)].n = 2
        #self.tablero[0][0].n = 32
        self.ocupados = 1
        self.Gameover = False


    def __str__(self):
        sol = ""
        for i in range(self.n):
            for j in range(self.n):
                sol += str(self.tablero[i][j].n)
                sol += " "
            sol += "\n"
        return sol






    def Up(self): ## dir == 0, -1

        newArray = []       # crea un nuevo array
        for i in range(self.n):
            newArray.append([])
            for j in range(self.n):
                newArray[i].append(Celda(0, False, False))


        dir = 1
        direccion = [0, -1]
        iter = [0, 0]

        for iter[0] in range(0, self.n, 1):
            for iter[1] in range(0, self.n, 1):

                newArray[iter[0]][iter[1]] = self.tablero[iter[0]][iter[1]]

                if(self.tablero[iter[0]][iter[1]].mover or self.tablero[iter[0]][iter[1]].mezclar ):

                    newArray[iter[0]][iter[1]].mover = False
                    newPos = [iter[0], iter[1]]
        
                    for l in range(iter[dir]-1, -1, -1):
                        print(l)
                        for i in range(self.n):
                            for j in range(self.n):
                                print(newArray[i][j].n, end=" ")
                                
                            print()
                        print()

                        
                        if(newArray[iter[0]][l].n != newArray[newPos[0]][newPos[1]].n or
                            not newArray[newPos[0]][newPos[1]].mezclar and newArray[iter[0]][l].n == newArray[newPos[0]][newPos[1]].n):
                            newArray[newPos[0]][newPos[1]].mezclar = False
                            print("bump")
                            break
                        elif(newArray[iter[0]][l].n == 0):
                            print("move")
                            newArray[iter[0]][l].n = newArray[newPos[0]][newPos[1]].n
                            newArray[newPos[0]][newPos[1]].n = 0
                            newPos = [iter[0], l]

                        elif(newArray[newPos[0]][newPos[1]].mezclar and newArray[iter[0]][l].n == newArray[newPos[0]][newPos[1]].n):
                            newArray[iter[0]][l].n = newArray[newPos[0]][newPos[1]].n
                            newArray[newPos[0]][newPos[1]].n = 0
                            print("merge")
                            newPos = [iter[0], l]
                            newArray[newPos[0]][newPos[1]].n *= 2
                            newArray[newPos[0]][newPos[1]].mezclar = False
                            self.ocupados -= 1
                            break

                        

                            

                        

                    newArray[newPos[0]][newPos[1]].mezclar = False
                    newArray[newPos[0]][newPos[1]].mover = False
        return True

    def Down():
        return True

    def Left():
        return True

    def Right():
        return True



    def Mover(self, direccion):
        if(self.Gameover): 
            return False


        # Empieza comprobando si hay algo que se mueva y preparando las celdas

        mover = False
        for i in range(self.n):
            for j in range(self.n):
                if(self.tablero[i][j].n != 0):
                    x = i+direccion[0]
                    y = j+direccion[1]

                    if(0<=x and x<self.n and 0<=y and y<self.n):                                              # si el punto al que se mueve esta en el tablero: 
                        if(self.tablero[x][y].n != 0):                                                          # si el punto es distintp  de 0
                            self.tablero[i][j].mover = False                                                       # no se mueve pero se mexcla si sin iguales
                            self.tablero[i][j].mezclar = (self.tablero[x][y].n == self.tablero[i][j].n)
                            if(not mover and self.tablero[x][y].n == self.tablero[i][j].n):
                                mover = True
                        else:                                                                                      # se mueve y se puede mezclar siempre
                            self.tablero[i][j].mover = True
                            self.tablero[i][j].mezclar = True
                            mover = True
                    else:
                        self.tablero[i][j].mover = False                                                      # esta en el borde y por tanto no se puede mover ni mezclar
                        self.tablero[i][j].mezclar = False
                

        if(not mover):      # si no se mueve nada acaba
            return False
        

        newArray = []       # crea un nuevo array
        for i in range(self.n):
            newArray.append([])
            for j in range(self.n):
                newArray[i].append(Celda(0, False, False))


        # se calculan los rangos para los fors
        if(  direccion == [ 0,  1]): # 0..n,  n..0
            inicio = [0, self.n-1]
            final = [self.n, -1]
            ds = [1, -1]
            dir = 1

        elif(direccion == [ 0, -1]): # 0..n,  0..n
            self.Up()

        elif(direccion == [ 1,  0]): # n..0,  0..n
            inicio = [self.n-1, 0]
            final = [-1, self.n]
            ds = [-1, 1]
            dir = 0

        elif(direccion == [-1,  0]): # 0..n,  0..n
            inicio = [0, 0]
            final = [self.n, self.n]
            ds = [1, 1]
            dir = 0

        else:
            inicio = [0, 0]
            final = [0, 0]

        
        '''
        print("rangos(i/f):", inicio, final)
        # se mueven a newArray
        iter = [0, 0]
        for iter[0] in range(inicio[0], final[0], ds[0]):
            for iter[1] in range(inicio[1], final[1], ds[1]):

                newArray[iter[0]][iter[1]] = self.tablero[iter[0]][iter[1]]

                if(self.tablero[iter[0]][iter[1]].mover or self.tablero[iter[0]][iter[1]].mezclar ):
                    print(self.tablero[iter[0]][iter[1]].n)
                    newArray[iter[0]][iter[1]].mover = False
                    newPos = [iter[0], iter[1]]

                    print("iteradores:",iter[0], iter[1])
                    

                    
                    if(direccion[dir] == -1):
                        a = -1
                        b = -1
                        c = -1
                    else:
                        a = 0
                        b = 1
                        c = 1
                    print("cossa:", iter[dir]+a, inicio[dir]+b, c)
                    for l in range(iter[dir]+a, inicio[dir]+b, c):
                        print(l)
                        for i in range(self.n):
                            for j in range(self.n):
                                print(newArray[i][j].n, end=" ")
                                
                            print()
                        print()

                        if(dir == 1):
                            if(newArray[iter[0]][l].n != newArray[newPos[0]][newPos[1]].n or
                               not newArray[newPos[0]][newPos[1]].mezclar and newArray[iter[0]][l].n == newArray[newPos[0]][newPos[1]].n):
                                newArray[newPos[0]][newPos[1]].mezclar = False
                                print("bump")
                                break
                            elif(newArray[iter[0]][l].n == 0):
                                print("move")
                                newArray[iter[0]][l].n = newArray[newPos[0]][newPos[1]].n
                                newArray[newPos[0]][newPos[1]].n = 0
                                newPos = [iter[0], l]

                            elif(newArray[newPos[0]][newPos[1]].mezclar and newArray[iter[0]][l].n == newArray[newPos[0]][newPos[1]].n):
                                newArray[iter[0]][l].n = newArray[newPos[0]][newPos[1]].n
                                newArray[newPos[0]][newPos[1]].n = 0
                                print("merge")
                                newPos = [iter[0], l]
                                newArray[newPos[0]][newPos[1]].n *= 2
                                newArray[newPos[0]][newPos[1]].mezclar = False
                                self.ocupados -= 1
                                break

                        else:
                            if(newArray[l][iter[1]].n != newArray[newPos[0]][newPos[1]].n or
                                not newArray[newPos[0]][newPos[1]].mezclar and newArray[l][iter[1]].n == newArray[newPos[0]][newPos[1]].n):
                                newArray[newPos[0]][newPos[1]].mezclar = False
                                print("bump")
                                break
                            elif(newArray[l][iter[1]].n == 0):
                                print("move")
                                newArray[l][iter[1]].n = newArray[newPos[0]][newPos[1]].n
                                newArray[newPos[0]][newPos[1]].n = 0
                                newPos = [l, iter[1]]

                            elif(newArray[newPos[0]][newPos[1]].mezclar and newArray[l][iter[1]].n == newArray[newPos[0]][newPos[1]].n):
                                newArray[l][iter[1]].n = newArray[newPos[0]][newPos[1]].n
                                newArray[newPos[0]][newPos[1]].n = 0
                                print("merge")
                                newPos = [l, iter[1]] 
                                newArray[newPos[0]][newPos[1]].n *= 2
                                newArray[newPos[0]][newPos[1]].mezclar = False
                                self.ocupados -= 1
                                break

                            

                        

                    newArray[newPos[0]][newPos[1]].mezclar = False
                    newArray[newPos[0]][newPos[1]].mover = False

        for i in range(self.n):
            for j in range(self.n):
                print(newArray[i][j].n, end=" ")
                
            print()
        print()
        self.tablero = newArray + []'''

        if(not self.ocupados == self.n*self.n): # se añade un nuevo numero si hay sitio
            x = randint(0, self.n-1)
            y = randint(0, self.n-1)
            while(not self.tablero[x][y].n == 0):
                x = randint(0, self.n-1)
                y = randint(0, self.n-1)

            self.tablero[x][y].n = 2
            self.ocupados += 1
            return True
        else:
            self.Gameover = True
            return False




    def Draw(self):
        for i in range(self.n):
            for j in range(self.n):
                if(self.tablero[i][j].n == 0):
                    pygame.draw.rect(pantalla, (100, 100, 100), [self.pos[0] + i*self.t + 10, self.pos[1] + j*self.t + 10, self.t - 20, self.t - 20])
                else:
                    if(self.tablero[i][j].n == 2):
                        color = (255, 255, 255)
                    elif(self.tablero[i][j].n == 4):
                        color = (255, 255, 255)
                    elif(self.tablero[i][j].n == 8):
                        color = (255, 255, 255)
                    elif(self.tablero[i][j].n == 16):
                        color = (255, 255, 255)
                    elif(self.tablero[i][j].n == 32):
                        color = (255, 255, 255)
                    elif(self.tablero[i][j].n == 64):
                        color = (255, 255, 255)
                    elif(self.tablero[i][j].n == 128):
                        color = (255, 255, 255)
                    else:
                        color = (255, 255, 255)
                    pygame.draw.rect(pantalla, color, [self.pos[0] + i*self.t + 10, self.pos[1] + j*self.t + 10, self.t - 20, self.t - 20])
                    
                    tamFuente = 0
                    if(len(str(self.tablero[i][j].n)) == 1):
                        tamFuente = 55
                    elif(len(str(self.tablero[i][j].n)) == 2):
                        tamFuente = 65
                    elif(len(str(self.tablero[i][j].n)) == 3):
                        tamFuente = 55

                    fuente = pygame.font.Font(None, tamFuente)
                    txt = fuente.render(str(self.tablero[i][j].n), True, (0, 0, 0))
                    pantalla.blit(txt, [self.pos[0] + i*self.t + 20, self.pos[1] + j*self.t + 20])




NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

direccion = [0, 0]
dimensiones = [800, 800]
tablero = Tablero(6, [50, 50], 700)

pygame.init()
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("2048")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                direccion = [-1, 0]
            if evento.key == pygame.K_RIGHT:
                direccion = [1, 0]
            if evento.key == pygame.K_UP:
                direccion = [0, -1]
            if evento.key == pygame.K_DOWN:
                direccion = [0, 1]

    # ---------------------------------------------------LÓGICA---------------------------------------------------
    if(direccion != [0, 0]):
        tablero.Mover(direccion)
        direccion = [0, 0]
        #print(tablero)
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(NEGRO)

    tablero.Draw()

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
