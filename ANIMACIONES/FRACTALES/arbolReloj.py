import pygame
import random
import numpy as np

    
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)



class Linea:
    def __init__(self, A, d, ang):
        self.A = A
        self.B = [A[0] + d * np.sin(np.radians(ang)), A[1] - d * np.cos(np.radians(ang))]
        self.d = d
        self.ang =  ang






def arbolReloj(rs, n, da, dt):# ramas, nivel, dAngulo[0, 1], dTamaño
    res = 20
    
    if(rs[0].d <= res):
        return []
    elif(rs[0].d>res):
        nrs = []
        for i in range(2**n):
            nrs.append(Linea(rs[i].B, dt*rs[i].d, rs[i].ang+da[0]))
            nrs.append(Linea(rs[i].B, dt*rs[i].d, rs[i].ang-da[1]))

        nrs = nrs + arbolReloj(nrs, n+1, da, dt)
        return nrs





dimensiones = [1000,1000]
ramas = []

dt = 6/8
da = [0,0]
r = Linea([500, 500+100/dt], 100/dt, 0) # punto, longitud, angulo
ramas.append(r)
ramas = ramas + arbolReloj([r], 0, da, dt)
step = 0

ang = False
dis = False
cambio = 0

pygame.init()
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Arbol fractal")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_KP_PLUS:
                cambio = 1
                print('+')
            if evento.key == pygame.K_KP_MINUS:
                cambio = -1
                print('-')

                
    # ---------------------------------------------------LÓGICA---------------------------------------------------
    if(step == 1):

        da[1] -= 1
        if(da[1]%60 == 0):
            da[0] += 360/12/6
        if(da[1] == -360):
            da[1] = 0

        ramas = []
        dt = 6/8
        r = Linea([500, 500+200/dt], 200/dt, 0) # punto, longitud, angulo
        ramas.append(r)
        ramas = ramas + arbolReloj([r], 0, da, dt)

        step = 0

    step += 1
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(NEGRO)
    
    for i in range(1, len(ramas)):
        pygame.draw.line(pantalla, BLANCO, ramas[i].A, ramas[i].B, 1)
    
    pygame.display.flip()
    reloj.tick(6)

pygame.quit()
