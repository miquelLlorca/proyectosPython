import pygame
import random
import numpy as np


class Linea:
    def __init__(self, A, d, ang):
        self.A = A
        self.B = [A[0] + d * np.sin(np.radians(ang)), A[1] - d * np.cos(np.radians(ang))]
        self.d = d
        self.ang =  ang

        
def arbol1(rs, n, da, dt):

    res = 5
    
    if(rs[0].d <= res):
        return []
    elif(rs[0].d>res):
        nrs = []
        for i in range(2**n):
            nrs.append(Linea(rs[i].B, dt*rs[i].d, rs[i].ang+da))
            nrs.append(Linea(rs[i].B, dt*rs[i].d, rs[i].ang-da))

        nrs = nrs + arbol1(nrs, n+1, da, dt)
        return nrs


def arbol2(rs, n):
    dt = 3/4
    da = 70
    res = 10
    
    if(rs[0].d <= res):
        return []
    elif(rs[0].d>res):
        nrs = []
        for i in range(5**n):
            nrs.append(Linea(rs[i].B, 0.75 * dt*rs[i].d, rs[i].ang+da))
            nrs.append(Linea(rs[i].B, dt*rs[i].d, rs[i].ang+da/3))
            nrs.append(Linea(rs[i].B, 0.75 * dt*rs[i].d, rs[i].ang-da))
            nrs.append(Linea(rs[i].B, dt*rs[i].d, rs[i].ang-da/3))
            nrs.append(Linea(rs[i].B, 1.25*dt*rs[i].d, 0))
            
        nrs = nrs + arbol2(nrs, n+1)
        return nrs
    
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)


dimensiones = [1000,1000]
ramas = []

# arbol 1

r = Linea([500, 1000], 300, 0)
ramas.append(r)
dt = 3/4
da = 30
ramas = ramas + arbol1([r], 0, da, dt)
'''
# arbol 2
r = Linea([300, 600], 150, 0)
ramas.append(r)
ramas = ramas + arbol2([r], 0)
'''

ang = False
dis = False
cambio = 0

print()
print("a - angulo entre ramas")
print("d - longitd de la rama")
print("+ / -")
print()



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
                
            if evento.key == pygame.K_KP_MINUS:
                cambio = -1
               
            if evento.key == pygame.K_a:
                ang = True
                dis = False
            
            if evento.key == pygame.K_d:
                ang = False
                dis = True
                
                
    # ---------------------------------------------------LÓGICA---------------------------------------------------
    if(cambio != 0):
        if(ang):
            da += cambio*5
        elif(dis):
            dt += cambio*0.05

        ramas = []
        r = Linea([500, 1000], 300, 0)
        ramas.append(r)
        ramas = ramas + arbol1([r], 0, da, dt)
        cambio = 0
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(NEGRO)
    
    for i in range(len(ramas)):
        pygame.draw.line(pantalla, BLANCO, ramas[i].A, ramas[i].B, 1)
    
    pygame.display.flip()
    reloj.tick(10)

pygame.quit()
