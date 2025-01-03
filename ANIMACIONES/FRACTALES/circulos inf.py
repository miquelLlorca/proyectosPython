import pygame
import random
import numpy as np
from pygame.constants import MOUSEBUTTONUP
from os import system

    
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

def Distance(a, b):
    return [a[0]-b[0], a[1]-b[1]]

def Module(distance):
    return ( distance[0]**2 + distance[1]**2 )**0.5

def GetCirclePoints(pos, n):
    points = []
    ang = 0
    dA = 360/n
    while(ang != 360):
        p = [pos[0] + 0.5, pos[1] + 0.5]
        p[0] += np.cos(np.radians(ang))/2
        p[1] += np.sin(np.radians(ang))/2
        points.append(p)
        ang += dA

    return points

def GetCircleData(points):
    max = points[0] + []
    min = points[0] + []

    for p in points:
        for i in range(2):
            if(p[i] > max[i]):
                max[i] = p[i]
            if(p[i] < min[i]):
                min[i] = p[i]
            #print(p)
            #print("max ", max)
            #print("min ", min)
            #print()
    return min[0], min[1], (max[0]-min[0]), (max[1]-min[1])



class Square:
    def __init__(self):
        self.v = [1, 1]
        self.b = [1, 0]
        self.c = [0, 0]
        self.d = [0, 1]


    def CalculaPos(self, pos, escala):
        vs = []
        vs.append([ self.v[i]*escala + pos[i] for i in range(2)])
        vs.append([ self.b[i]*escala + pos[i] for i in range(2)])
        vs.append([ self.c[i]*escala + pos[i] for i in range(2)])
        vs.append([ self.d[i]*escala + pos[i] for i in range(2)])
        return vs


    def MovePoint(self, newPos):
        self.b = newPos

        side1 = Distance(self.v, self.b)
        len1 = Module(side1)
        len2 = 1/len1
        
        side2 = [side1[i]*len2/len1 for i in [1, 0]]
        side2[0] *= -1

        self.d = [ side2[i] + self.v[i] for i in range(2)]
        self.c = [ side2[i] + self.b[i] for i in range(2)]

        #print("Update position")
        #print("len1 =", len1)
        #print("side1 =", side1)
        #print("len2 =", len2)
        #print("side2 =", side2)
        #print("prod =", len1*len2)
        #print("Square:")
        #print([round(self.c[i], 3) for i in range(2)], end = " // ")
        #print([round(self.b[i], 3) for i in range(2)])
        #print([round(self.d[i], 3) for i in range(2)], end = " // ")
        #print([round(self.v[i], 3) for i in range(2)])

        return 0


    def Draw(self, pantalla, pos, escala):
        vs = self.CalculaPos(pos, escala)
        for i in range(4):
            pygame.draw.ellipse(pantalla, NEGRO, [vs[i][0]-4, vs[i][1]-4, 8, 8])
        pygame.draw.polygon(pantalla, NEGRO, vs, 1)




class Circle:
    def __init__(self, points):
        self.x = self.y = self.dX = self.dY = 0
        if(points != []):
            self.x, self.y, self.dX, self.dY = GetCircleData(points)
        

    def __str__(self):
        cad = ""
        cad += str(self.x)
        cad += " / "
        cad += str(self.y)
        cad += " / "
        cad += str(self.dX)
        cad += " / "
        cad += str(self.dY)
        return cad






def DrawScreen(dimensiones, pantalla, cuadrado, circulos, escala, pos):
    pantalla.fill((150, 150, 150))
    
    st = [-10, 0]
    end = [11, 0]
    for i in range(11):
        pygame.draw.line(pantalla, NEGRO, [ st[i]*escala + pos[i] for i in range(2)], [ end[i]*escala + pos[i] for i in range(2)], 1)
        st[1] += -1
        end[1] += -1

    st = [11, -10]
    end = [11, 0]
    for i in range(21):
        pygame.draw.line(pantalla, NEGRO, [ st[i]*escala + pos[i] for i in range(2)], [ end[i]*escala + pos[i] for i in range(2)], 1)
        st[0] += -1
        end[0] += -1


    for c in circulos:
        x = c.x*escala + pos[0]
        y = c.y*escala + pos[1]
        dx = c.dX*escala
        dy = c.dY*escala
        if(not(dx > 2*dimensiones[0] or dy > 2*dimensiones[1] or # si es muy grande
               x > dimensiones[0] or y>dimensiones[1] or         # si la pos pilla fuera (+)
               x+dx < 0 or y+dy < 0                              # si pos+d pilla fuera  (-)
        )):
            pygame.draw.ellipse(pantalla, NEGRO, [x, y, dx, dy], 1)

    cuadrado.Draw(pantalla, pos, escala)
    
    pygame.display.flip()






dimensiones = [1000,1000]

escala = 100
squarePos = [200, 200]

cuadrado = Square()
move = False
step = 1
runAnimation = False
movePoint = 0


# faltaria implementar el algoritmo para recorrer la cuadricula
# https://youtu.be/hSsRcpIsunk
# pinta complicao, i shall give it a thought
'''
. . . 4 4 . . .
. . 4 3 3 4 . .
. 4 3 2 2 3 4 .
4 3 2 1 1 2 3 4
. . . S . . . .
'''

start1 = [0, -1]
end1   = [0, -1]
start2 = [1, -1]
end2   = [1, -1]
iter1 = start1 + []
iter2 = start2 + []

c = Circle([])
c.x = 0
c.y = 0.5
c.dX = 1
c.dY = 1
circulos = [c]




pygame.init()
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Arbol fractal")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

        if evento.type == pygame.MOUSEBUTTONDOWN:
            move = True
            oldPos = pygame.mouse.get_pos()
        if evento.type == pygame.MOUSEBUTTONUP:
            move = False


        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_KP_PLUS:
                escala /= 0.9
                print('+')
            if evento.key == pygame.K_KP_MINUS:
                escala *= 0.9
                print('-')
            if evento.key == pygame.K_SPACE:
                runAnimation = not(runAnimation)
            if evento.key == pygame.K_a:
                print('a')
            if evento.key == pygame.K_d:
                print('d')
            if evento.key == pygame.K_r:
                escala = 913.9181488855504#100
                squarePos = [58, -405]#[200, 200]
                
    # ---------------------------------------------------LÓGICA---------------------------------------------------

    # test para crear el circulo inicial

    #newP = cuadrado.b+[]
    #if(newP[0] > 10):
    #    newP[0] = -10
    #newP[0] += 0.1
    #cuadrado.MovePoint(newP)

    if(move):
        pos = pygame.mouse.get_pos()
        squarePos = [  squarePos[i] + (pos[i]-oldPos[i])  for i in range(2)]
        oldPos = [pos[0], pos[1]]


    if(runAnimation):
        #step = 0
        # diagonal 1

        circlePoints = GetCirclePoints(iter1, 32)
        transformedCircle = []

        for p in circlePoints:
            cuadrado.MovePoint(p)
            transformedCircle.append(cuadrado.d)

            DrawScreen(dimensiones, pantalla, cuadrado, circulos, escala, squarePos)

        #if(step < 10):
        #    circulos.append(Circle(circlePoints))
        circulos.append(Circle(transformedCircle))
        
        system("clear")
        print(f"Circulos: {len(circulos)}")
        if(iter1 == end1):
            start1[0] += -1
            end1[1] += -1
            iter1 = start1 + []
            step += 1
        else:
            iter1[0] += 1
            iter1[1] += -1




        # diagonal 2

        circlePoints = GetCirclePoints(iter2, 32)
        transformedCircle = []

        for p in circlePoints:
            cuadrado.MovePoint(p)
            transformedCircle.append(cuadrado.d)
            DrawScreen(dimensiones, pantalla, cuadrado, circulos, escala, squarePos)

        #if(step < 10):
        #    circulos.append(Circle(circlePoints))
        circulos.append(Circle(transformedCircle))
        
        system("clear")
        print(f"Circulos: {len(circulos)}")
        print(f"Step: {step}")
        print(f"Escala: {escala}")
        print(f"Pos: {squarePos}")

        if(iter2 == end2):
            start2[1] += -1
            end2[0] += +1
            iter2 = start2 + []
        else:
            iter2[0] += 1
            iter2[1] += 1
    
    
   
    

    # ---------------------------------------------------DIBUJO---------------------------------------------------


    # EN ESTE CASO NO SE SIGUE LA TIPICA ESTRUCTURA DE LOGICA - DIBUJO
    # ESTAN INTERCALADAS PARA FACILITAR LA ANIMACION 

    DrawScreen(dimensiones, pantalla, cuadrado, circulos, escala, squarePos)
    reloj.tick(20)

pygame.quit()
