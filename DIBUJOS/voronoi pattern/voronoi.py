import pygame


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.modulo = (x**2 + y**2)**0.5

    def Draw(self):
        pygame.draw.ellipse(pantalla, NEGRO, [self.x-5, self.y-5, 10, 10])

    def Modulo(self):
        return self.modulo

    def PuntoMedio(self, other):
        return Punto((self.x+other.x)/2, (self.y+other.y)/2)



class Bisectriz:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.pm = p1.PuntoMedio(p2)

    def Draw(self):
        pygame.draw.rect(pantalla, AZUL, [self.pm.x-5, self.pm.y-5, 10, 10])





class Plano:
    def __init__(self):
        self.puntos = []
        self.bs = []
        self.n = 0

    def Append(self, punto):
        if(self.n == 0):
            self.puntos.append(punto)
            self.n = 1

        else:
            pos = -1
            for i in range(self.n):
                if(self.puntos[i].Modulo() > punto.Modulo()):
                    self.puntos.insert(i, punto)
                    pos = i
                    self.n += 1
                    break
            if(pos == -1):
                pos = self.n
                self.puntos.insert(pos, punto)
                self.n += 1


            if(pos-3 >= 0):
                self.bs.append(Bisectriz(self.puntos[pos-3], punto))
            if(pos-2 >= 0):
                self.bs.append(Bisectriz(self.puntos[pos-2], punto))
            if(pos-1 >= 0):
                self.bs.append(Bisectriz(self.puntos[pos-1], punto))
            if(pos+1 < self.n):
                self.bs.append(Bisectriz(self.puntos[pos+1], punto))
            if(pos+2 < self.n):
                self.bs.append(Bisectriz(self.puntos[pos+2], punto))
            if(pos+3 < self.n):
                self.bs.append(Bisectriz(self.puntos[pos+3], punto))


                
        

    def Draw(self):
        for p in self.puntos:
            p.Draw()

        for b in self.bs:
            b.Draw()





NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)
  

plano = Plano()





pygame.init()
dimensiones = [1800,1000]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Voronoi")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            plano.Append(Punto(x, y))
    # ---------------------------------------------------LÓGICA---------------------------------------------------
  
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill((150, 150, 150))

    plano.Draw()

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
