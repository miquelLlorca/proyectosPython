
import numpy as np
from numpy import sin, cos
from os import system

# ===========================================================================================================================
# CONSTASNTES Y FUNCIONES AUXILIARES





def calculaRuedas(tamaño):
    a = [-tamaño[0]/2, -tamaño[1]/2]
    b = [ tamaño[0]/2, -tamaño[1]/2]
    c = [ tamaño[0]/2,  tamaño[1]/2]
    d = [-tamaño[0]/2,  tamaño[1]/2]
    return [a,b,c,d]



def rotarPuntos(puntos, ang):
    newP = []
    ang = np.radians(ang)

    for p in puntos:
        newP.append([p[0]*cos(ang)-p[1]*sin(ang), p[0]*sin(ang)+p[1]*cos(ang)]) # Punto(p.x*cos(a)-p.y*sin(a), p.x*sin(a)+p.y*cos(a))

    return newP


def rotaRuedas(rueda, ang):
    extremos = [[-20, 0], [0, 0], [20, 0]]
    extremos = rotarPuntos(extremos, ang)
    return extremos



# ===========================================================================================================================
# CLASES


class Coche:
    def __init__(self, pos, dt, tamaño = [200, 100]):
        self.pos = pos
        self.tamaño = tamaño
        self.v = 0
        self.orientation = 0
        self.steer = 0 # de -60 a 60
        self.a = 0
        self.ruedas = calculaRuedas(tamaño)
        self.dt = dt


    def Steer(self, ang): # input desde el juego
        if(-45 <= self.steer + ang <= 45):
            self.steer += ang


    def Accelerate(self, a): # input desde el juego
        # actualiza a y v
        self.a = a

        if(a>=0):
            self.v = self.v + self.v*self.dt + 0.5*a*self.dt**2
        else:
            newV = self.v + self.v*self.dt + 0.5*a*self.dt**2
            self.v = newV if newV>=0 else 0 

    
    def Turn(self):
        if(self.steer != 0 and self.v != 0):
            # calcula segun STEER y V el angulo a girar

            ang = 1 if self.steer>0 else -1
            self.orientation += ang

            # gira el coche
            self.ruedas = rotarPuntos(self.ruedas, ang)

            # reduce el steer hasta que llega a 0
            if(self.steer>0 and self.steer-ang>0): # positivo y se mantiene en positivo
                self.steer -= ang
            elif(self.steer<0 and self.steer-ang <0): # negativo y se mantiene en negativo
                self.steer -= ang
            else:
                self.steer = 0 # 0 xd


    def Move(self):
        f = [np.cos, np.sin]
        # mueve en la direccion que toca
        for i in range(2):
            self.pos[i] += self.v*f[i](np.radians(self.orientation))

        self.v -= self.v*0.01 if self.v>0 else 0
        if(0 < self.v < 0.005):
            self.v = 0


    def Update(self, debug=False):
        self.Turn()
        self.Move()
        

        if(debug):
            system("clear")
            
            print("DEBUG:")
            print()
            print("pos =", self.pos)
            print("v =", self.v)
            print("a =", self.a)
            print("ori =", self.orientation%360)
            print("str =", self.steer)

