import pygame
import numpy as np

import random
import sys
# sys.path.append('/home/miquel23/Desktop/proyectosPython/Utils/') 
from colors import *


NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

def convert(param):
    if(type(param) == str):
        return [int(x) for x in param.split(',')]
    if(type(param) == list):
        return ','.join([str(x) for x in param])
    return None

class RandomGradient:
    def __init__(self, gradient, dim_display, tam_gradient, tam_punto):
        self.original_gradient = gradient
        self.dims = dim_display
        self.tam_gradient = tam_gradient
        self.tam_punto = tam_punto

        self.gradient = {} # dict key=pos, value=color_key


    def get_random_color(self, row):
        index = 0
        total_colors = len(self.original_gradient)
        delta = int(total_colors * 0.25)

        # calcula equivalencia en % de row a gradient
        equivalence = int(total_colors * (row/self.tam_gradient[1])) if row > 0 else 0

        index = np.random.randint(equivalence-delta, equivalence+delta+1)
        if(index < 0):
            index = 0
        elif(index >= total_colors):
            index = total_colors - 1
        return index



    def create_new_gradient(self):
        dots_per_row = self.tam_gradient[0]

        for i in range(self.tam_gradient[1]):
            dots = []
            for j in range(dots_per_row):
                while(True):
                    new_dot = np.random.randint(0, self.tam_gradient[0])
                    if(new_dot not in dots):
                        dots.append(new_dot)
                        break

            for dot in dots:
                color = self.get_random_color(i)
                self.gradient[convert([dot, i])] = color


    def draw(self, pantalla, re_paint):
        if(re_paint):
            pantalla.fill(BLANCO)

            step_x = self.dims[0]/self.tam_gradient[0]
            step_y = self.dims[1]/self.tam_gradient[1]
            delta_x = int(self.tam_punto * 0.15)
            delta_y = int(self.tam_punto * 0.15)

            for key in self.gradient.keys():
                col = self.gradient[key]
                rect = convert(key)
                rect[0] *= step_x
                rect[1] *= step_y
                rect[0] += np.random.randint(-delta_x, delta_x)
                rect[1] += np.random.randint(-delta_y, delta_y)

                rect += [self.tam_punto, self.tam_punto]
                pygame.draw.ellipse(pantalla, self.original_gradient[col], rect)

        return False

# MAIN =================================================================================================================

if(__name__ == "__main__"):


    color_A = (255, 162, 0)
    color_B = (51, 119, 255)
    num_steps = 30

    degradado_original = get_gradient(color_A, color_B, num_steps)
    dimensiones = [1000,1000]
    tam = [60,50]
    tam_punto = 35

    random_gradient = RandomGradient(
        gradient=degradado_original,
        dim_display=dimensiones,
        tam_gradient=tam,
        tam_punto=tam_punto
    )
    random_gradient.create_new_gradient()
    re_paint = True


    pygame.init()
    pantalla = pygame.display.set_mode(dimensiones) 
    pygame.display.set_caption("Degradado")
    hecho = False
    reloj = pygame.time.Clock()

    while not hecho:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                hecho = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    random_gradient.create_new_gradient()
                    re_paint = True

        # LÓGICA---------------------------------------------LÓGICA---------------------------------------------LÓGICA
        pos = pygame.mouse.get_pos()
        # DIBUJO---------------------------------------------DIBUJO---------------------------------------------DIBUJO

        

        re_paint = random_gradient.draw(pantalla, re_paint)

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()
