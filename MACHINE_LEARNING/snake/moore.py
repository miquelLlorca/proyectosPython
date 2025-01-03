'''
Lidenmayer system aka L-system
    https://en.wikipedia.org/wiki/L-system

Moore curve
    https://en.wikipedia.org/wiki/Moore_curve

'''




import pygame
import random
import numpy as np


NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
FONDO = (100, 100, 100)


DIRECTIONS = [
    [ 0,-1],
    [ 1, 0],
    [ 0, 1],
    [-1, 0],
]
class Cursor:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.dir = 0

    def Move(self, step):
        prevPos = [self.x, self.y]
        self.x += step*DIRECTIONS[self.dir][0]
        self.y += step*DIRECTIONS[self.dir][1]
        newPos = [self.x, self.y]
        return [prevPos, newPos]
    
    def Turn(self, angle):
        self.dir += int(angle+'1')
        self.dir = self.dir%4



L = '-RF+LFL+FR-'
R = '+LF-RFR-FL+'

RULES = {
    'L':'-RF+LFL+FR-',
    'R':'+LF-RFR-FL+'
}
AXIOM = 'LFL+F+LFL'

class Moore:
    def __init__(self):
        self.edges = []
        self.cursor = None

    def Step(self, rule, depth, maxDepth):
        # Alphabet: L, R
        # Constants: F, +, −
        # Axiom: LFL+F+LFL
        # Production rules:
        #   L → −RF+LFL+FR−
        #   R → +LF−RFR−FL+

        # tremendo fumadote, agarrense que vienen curvas

        if(depth == maxDepth):
            return
        
        for i in rule:
            if(i == 'L' or i=='R'):
                self.Step(RULES[i], depth+1, maxDepth)
            elif(i == '+' or i == '-'):
                self.cursor.Turn(i)
            elif(i == 'F'):
                self.edges.append(self.cursor.Move(self.step))

        return
    
    def StartAnim(self, maxDepth):
        # clean previous
        self.edges = []

        # set step
        self.step = int(dimensiones[0]/(2**maxDepth))

        # set cursor
        x = self.step*2**(maxDepth-1)  - int(self.step/2)
        y = dimensiones[1] - int(self.step/2)
        self.cursor = Cursor(x,y)

        # empieza recursividad
        self.Step(AXIOM, 0, maxDepth)

    def Draw(self, pantalla):
        for pair in self.edges:
            pygame.draw.line(pantalla, NEGRO, pair[0], pair[1], 3)
        return

# ========================================================================================

dimensiones = [1024, 1024]

# MAIN =================================================================================================================

if(__name__ == "__main__"):

    curve = Moore()
    depth = 1

    pygame.init()
    pantalla = pygame.display.set_mode(dimensiones) 
    pygame.display.set_caption("Moore curve")
    hecho = False
    reloj = pygame.time.Clock()


    while not hecho:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                hecho = True

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    curve.StartAnim(depth)
                
                if evento.key == pygame.K_PLUS:
                    depth += 1
                    curve.StartAnim(depth)
        # LÓGICA---------------------------------------------LÓGICA---------------------------------------------LÓGICA
        
        # DIBUJO---------------------------------------------DIBUJO---------------------------------------------DIBUJO

        pantalla.fill(FONDO)

        curve.Draw(pantalla)

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()
