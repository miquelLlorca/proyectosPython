import numpy as np

class Masa:
    def __init__(self, m, pos, v, ID):
        self.m = m
        self.pos = pos
        self.v = v
        self.id = ID
        self.g = Vector()

    def Gravedad(self, p):
        return (150000 * self.m)/self.pos.Distancia(p)**2                               # (G * m) / r**2
        
    def Move(self, plano, t):
        
        g = Vector(d=0, ang=0)                                                        # g = 0, 0
        for masa in plano.Ms:                                                         # por cada masa distinta a self...
            if(self.id != masa.id): 
                g = g.Sumar(Vector(d = masa.Gravedad(self.pos)*self.m ,               # a g se le suma la g que genera cada masa
                                   ang = self.pos.Angulo(masa.pos)))

        g.ReCalculaXY()                                                               # se recalcula g
        self.pos.x += self.v.x * t  +   0.5 * g.x * t**2                              # se actuliza la pos de self
        self.pos.y += self.v.y * t  +   0.5 * g.y * t**2
        self.g = g
        self.v.x += g.x * t                                                           # se actuliza la v de self
        self.v.y += g.y * t
        #print("g =", g)
        #print("v =", self.v)


# ====================================================================================


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Sumar(self, other):
        return Punto(self.x+other.x, self.y+other.y)

    def Restar(self, other):
        return Punto(self.x-other.x, self.y-other.y)

    def Distancia(self, other):
        aux = self.Restar(other)
        return (aux.x**2 + aux.y**2)**0.5
    
    def Mult(self, n):
        return Punto(self.x*n, self.y*n)

    def Angulo(self, other):
        return Vector(a=self, b=other).Angulo()

# ====================================================================================


class Vector:
    def __init__(self, a = Punto(0, 0), b = Punto(0, 0), d = 0, ang = 0):
        self.a = a
        self.b = b
        self.x = b.x - a.x
        self.y = b.y - a.y
        if(d != 0 and ang != 0):
            self.x = d * np.cos(np.radians(ang))
            self.y = d * np.sin(np.radians(ang))
            print(self.x, self.y)
            self.b = self.b.Sumar(Punto(self.a.x + self.x, self.a.y + self.y))

    def __str__(self):
        result = ""
        result += "< " + str(self.x) + ", " + str(self.y) + " >"
        return result

    def ReCalculaXY(self):
        self.x = self.b.x - self.a.x
        self.y = self.b.y - self.a.y

    def ReCalculaB(self):
        self.b = self.b.Sumar(Punto(self.a.x + self.x, self.a.y + self.y))

    def Modulo(self):
        return ((self.a.x + self.b.x)**2  +  (self.a.y + self.b.y)**2)**0.5

    def Sumar(self, other):
        return Vector(self.a, other.b)

    def Restar(self, other):
        return Vector(self.b, other.b)

    def Mult(self, n):
        return Vector(self.a, self.b.Mult(n))

    def Angulo(self):
        ang = np.arctan(self.y/self.x)

        if(self.x < 0 and self.y > 0):
            return ang + np.pi/2

        if(self.x < 0 and self.y < 0):
            return ang + np.pi

        if(self.x > 0 and self.y < 0):
            return ang + 3*np.pi/2

        return np.degrees(ang)


# ====================================================================================


class Plano:
    def __init__(self, Ms):
        self.Ms = Ms
    
    def Insertar(self, m):
        self.Ms.append(m)

    def Update(self, t):
        for m in self.Ms:
            m.Move(self, t)


# ====================================================================================


if(__name__ == "__main__"):
    m1 = Masa(1, Punto(10, 10), Vector(), 0)
    m2 = Masa(1, Punto(0, 0), Vector(a=Punto(0, 0), b=Punto(0, 0)), 1)
    plano = Plano([m2])

    print(m1.pos.x, m1.pos.y)
    print(m1.pos.Angulo(m2.pos))

    print(np.degrees(m1.pos.Angulo(m2.pos)))
    print(np.sin(m1.pos.Angulo(m2.pos)), np.cos(m1.pos.Angulo(m2.pos)))



    m1.Move(plano, 1)

    print(m1.pos.x, m1.pos.y)


