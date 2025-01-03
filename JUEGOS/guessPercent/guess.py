#from this import d ????
import pygame
from random import randrange

'''
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

class Area:
    def __init__(self, dimensiones):
        self.a = randrange(100, dimensiones[0]-100)
        self.b = randrange(100, dimensiones[1]-100)

        self.x = randrange(5, dimensiones[0]-self.a-5)
        self.y = randrange(5, dimensiones[1]-self.b-5)

        self.dir = 0 if self.a>self.b else (1 if self.b>self.a else randrange(0, 1))

        self.percent = randrange(0, 100)
        self.color = (randrange(0, 255), randrange(0, 255), randrange(0, 255))
        self.guess = -1
        self.guessPos = -1



    def Check(self, click):
        if(self.dir == 0):
            if(click[0] >= self.x):
                self.guess = round(100*(click[0] - self.x)/self.a)
                self.guessPos = click[0]
        elif(self.dir == 1):
            if(click[1] >= self.y):
                self.guess = round(100*(click[1] - self.y)/self.b)
                self.guessPos = click[1]



    def Draw(self, pantalla, pos, fill):
        # seleccion o solucion:
        if(fill):
            if(self.dir == 0):
                pygame.draw.rect(pantalla, self.color, [self.x, self.y, pos[0]-self.x, self.b])
            elif(self.dir == 1):
                pygame.draw.rect(pantalla, self.color, [self.x, self.y, self.a, pos[1]-self.y])
        elif(self.guess != -1):
            if(self.dir == 0):
                pygame.draw.rect(pantalla, self.color, [self.x, self.y, self.guessPos-self.x, self.b])
            elif(self.dir == 1):
                pygame.draw.rect(pantalla, self.color, [self.x, self.y, self.a, self.guessPos-self.y])

        # perimetro
        pygame.draw.rect(pantalla, NEGRO, [self.x, self.y, self.a, self.b], 5)

        # direccion
        if(self.dir == 0):
            pygame.draw.line(pantalla, NEGRO, [self.x+self.a/2, self.y], [self.x+self.a/2-15, self.y-15], 5)
            pygame.draw.line(pantalla, NEGRO, [self.x+self.a/2, self.y], [self.x+self.a/2-15, self.y+15], 5)
        elif(self.dir == 1):
            pygame.draw.line(pantalla, NEGRO, [self.x, self.y+self.b/2], [self.x-15, self.y+self.b/2-15], 5)
            pygame.draw.line(pantalla, NEGRO, [self.x, self.y+self.b/2], [self.x+15, self.y+self.b/2-15], 5)
        
        # % a acertar
        fuente = pygame.font.Font(None, 50)
        txt = fuente.render(str(self.percent), True, NEGRO)
        pantalla.blit(txt, [self.x+5, self.y+5])

        # % acertado
        if(self.guess != -1):
            txt = fuente.render(str(self.guess), True, NEGRO)
            pantalla.blit(txt, [self.x+55, self.y+5])

        # info
        fuente = pygame.font.Font(None, 50)
        txt = fuente.render((f"{'%'} Guesser"), True, NEGRO)
        pantalla.blit(txt, [self.x+5, self.y+self.b+5])
        fuente = pygame.font.Font(None, 31)
        txt = fuente.render("SPACE to skip lvl", True, NEGRO)
        pantalla.blit(txt, [self.x+5, self.y+self.b+45])


# ================================================================================================================================

dimensiones = [1000,1000]
A = Area(dimensiones)
fill = False

pygame.init()
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Guess")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

        if evento.type == pygame.MOUSEBUTTONDOWN:
            fill = True

        if evento.type == pygame.MOUSEBUTTONUP:
            fill = False
            A.Check(pygame.mouse.get_pos())

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                A = Area(dimensiones)
    # ---------------------------------------------------LÓGICA---------------------------------------------------
  
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill((150, 150, 150))

    A.Draw(pantalla, pygame.mouse.get_pos(), fill)

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
