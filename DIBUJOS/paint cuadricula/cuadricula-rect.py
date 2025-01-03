from re import S
import click
import pygame
import random
 
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

LADO = 50


class Cuadricula:
    def __init__(self, dimensiones):
        self.dimensiones = dimensiones
        self.escala = 1
        self.origen = [0, 0] # pos en pixeles del origen
        
        self.pintados = [] # solo se guardaran los rects a pintar


    def DrawRect(self, pantalla, pos):
        pygame.draw.rect(pantalla, (50, 50, 50), [self.origen[0] + pos[0], self.origen[1] + pos[1], self.escala*2*LADO, self.escala*LADO])
        pygame.draw.rect(pantalla, NEGRO, [self.origen[0] + pos[0], self.origen[1] + pos[1], self.escala*2*LADO, self.escala*LADO], 1)


    def DrawTablero(self, pantalla):

        for c in self.pintados:
            x = c[0]*self.escala*2*LADO if c[1]%2==0 else (c[0]+0.5)*self.escala*2*LADO
            y = c[1]*self.escala*LADO
            
            self.DrawRect(pantalla, [x, y])


    def Borrar(self, pos):
        i = (pos[0]-self.origen[0])//(LADO*2)
        j = (pos[1]-self.origen[1])//LADO

        for p in range(len(self.pintados)):
            if(self.pintados[p] == [i, j]):
                self.pintados.pop(p)
                break
            

    def Pintar(self, pos):
        i = (pos[0]-self.origen[0])//(LADO*2*self.escala)
        j = (pos[1]-self.origen[1])//(LADO*self.escala)

        if(self.pintados != []):
            if([i, j] != self.pintados[len(self.pintados)-1]):

                pos = -1
                for p in range(len(self.pintados)):
                    if(self.pintados[p] == [i, j]):
                        pos = p
                        break

                if(pos == -1):
                    self.pintados.append([i, j])


            print(self.pintados)
        else:
            self.pintados.append([i, j])

    
    def Mover(self, mover):
        self.origen[0] += mover[0]
        self.origen[1] += mover[1]


    def Escalar(self, dir):
        self.escala *= dir
        self.origen[0] *= dir
        self.origen[1] *= dir


    def Abrir(self, name):
        file = open(name, 'r')
        line = file.readline()

        while(line != ""):
            self.pintados.append([int(float(x)) for x in line.split()])
            line = file.readline()

        file.close()
        

    def Guardar(self):
        file = open(input("File name: "), 'w')
        for p in tabl.pintados:
            file.write(str(p[0])+ " "+str(p[1]))
            file.write("\n")
        file.close()
        print("File saved.")
# ==============================================================================================================

dimensiones = [1800, 1000]

pintar = False
tabl = Cuadricula(dimensiones)
tabl.Abrir("a.txt")
mover = [0, 0]
previousPos = [-1000, -1000]
borrar = False
zoom = 2

pygame.init()
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Cuadricula")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True


        if evento.type == pygame.MOUSEBUTTONDOWN:
            pintar = True
            
        if evento.type == pygame.MOUSEBUTTONUP:
            pintar = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a:
                mover = [5, 0]
            if evento.key == pygame.K_d:
                mover = [-5, 0]
            if evento.key == pygame.K_w:
                mover = [0, 5]
            if evento.key == pygame.K_s:
                mover = [0, -5]
            if evento.key == pygame.K_LSHIFT:
                mover[0] *= 2
                mover[1] *= 2
            if evento.key == pygame.K_SPACE:
                borrar = not borrar
            if evento.key == pygame.K_PLUS:
                tabl.Escalar(zoom)
            if evento.key == pygame.K_MINUS:
                tabl.Escalar(1/zoom)
            if evento.key == pygame.K_g:
                tabl.Guardar()
        if evento.type == pygame.KEYUP:
            mover = [0, 0]




    # ---------------------------------------------------LÓGICA--------------------------------------------------

    tabl.Mover(mover)

    if(pintar):
        pos = pygame.mouse.get_pos()
        #if(previousPos != pos):
        if(not borrar):
            tabl.Pintar(pos)
        else:
            tabl.Borrar(pos)
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill((200, 200, 200))

    tabl.DrawTablero(pantalla)

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
