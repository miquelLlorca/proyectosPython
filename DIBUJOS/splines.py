import pygame
import random
 
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)
FONDO = (150, 150, 150)


def SumaVectores(a, b):
    return [a[j] + b[j] for j in range(2)]
def RestaVectores(a, b):
    return [a[j] - b[j] for j in range(2)]
def MultiplicaVector(a, b):
    return [a[j]*b for j in range(2)]
def DivideVector(a, b):
    return [a[j]/b for j in range(2)]

class Spline:
    def __init__(self, max, res):
        self.max = max
        self.res = res
        self.n = 0
        self.puntos = []
        self.rectas = []
        self.curva = []

        self.animation = False
        self.animCounter = 0
        self.rectaAux = []
        self.anchos = []

    def NotFull(self):
        return (self.n < self.max)


    def Add(self, pos):
        self.puntos.append(pos)
        self.n += 1
        

    def Clear(self):
        self.curva = []
        self.animation = False
        self.animCounter = 0
        self.rectaAux = []
        self.anchos = []


    def StartAnimation(self):
        for i in range(1, self.n):
            self.rectas.append(DivideVector(RestaVectores(self.puntos[i], self.puntos[i-1]), self.res))
        self.animation = True
        return


    def CalculaPunto(self, puntos):

        if(len(puntos) <= 2):
            # p + count * v / res
            self.curva.append(
                SumaVectores( 
                    MultiplicaVector(
                        DivideVector(
                            RestaVectores(puntos[1], puntos[0]), 
                            self.res), 
                        self.animCounter), 
                    puntos[0])
                )

        else:
            aux = []
            for i in range(1,len(puntos)):
                # p + r*count
                p = SumaVectores(
                        MultiplicaVector(
                            DivideVector(
                                RestaVectores(puntos[i], puntos[i-1]), 
                                self.res), 
                            self.animCounter), 
                        puntos[i-1]
                    )

                aux.append(p)
                self.rectaAux.append(p)
                self.anchos.append(1)

            self.CalculaPunto(aux+[])
        return


    def Update(self, fps):
        if( not self.animation):
            return
        if(self.n<=2):
            self.animation = False
            return
        if(self.animCounter >= self.res):
            self.animation = False
            self.animCounter = 0
            return

        for i in range(int(self.res/fps)):
            self.anchos = []
            self.rectaAux = []
            for i in range(self.n - 1):
                # p + r*count
                self.rectaAux.append(SumaVectores(
                                        MultiplicaVector(
                                            self.rectas[i], 
                                            self.animCounter), 
                                        self.puntos[i])
                                    )
                self.anchos.append(1)

            self.CalculaPunto(self.rectaAux+[])
            self.animCounter += 1

            if(self.animCounter >= self.res):
                self.animation = False
                self.animCounter = 0
                return
        #self.animation = False


    def Draw(self, pantalla, pressed):
        for i in range(self.n):
            pygame.draw.ellipse(pantalla, NEGRO, [self.puntos[i][0]-3, self.puntos[i][1]-3, 6, 6])
            if(i>0):
                pygame.draw.line(pantalla, NEGRO, self.puntos[i-1], self.puntos[i], 1)

        if(self.n > 1 and pressed):
            pygame.draw.ellipse(pantalla, NEGRO, [pos[0]-3, pos[1]-3, 6, 6])
            pygame.draw.line(pantalla, NEGRO, self.puntos[len(self.puntos)-1], pos, 1)

        if(self.animation):
            for i in range(1, len(self.rectaAux)):
                pygame.draw.line(pantalla, NEGRO, self.rectaAux[i], self.rectaAux[i-1], self.anchos[i])
        
        for i in range(len(self.curva)):
            pygame.draw.ellipse(pantalla, AZUL, [self.curva[i][0]-5, self.curva[i][1]-5, 10, 10])
        
        if(len(self.curva) == self.res):
            pygame.draw.ellipse(pantalla, AZUL, [self.puntos[-1][0]-5, self.puntos[-1][1]-5, 10, 10])
            
            


# ========================================================================================


# MAIN =================================================================================================================

if(__name__ == "__main__"):

    dimensiones = [1800,1000]
    
    pos = [-1, -1]
    pressed = False
    max = 50
    res = 1000
    curva = Spline(max, res)
    fps = 60

    pygame.init()
    pantalla = pygame.display.set_mode(dimensiones) 
    pygame.display.set_caption("Splines")
    hecho = False
    reloj = pygame.time.Clock()

    while not hecho:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                hecho = True

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if(curva.NotFull()):
                    pressed = True

            elif evento.type == pygame.MOUSEBUTTONUP:
                if(curva.NotFull()):
                    curva.Add(pos)
                    pressed = False
                    pos = [-1, -1] 

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    curva.StartAnimation()

                if evento.key == pygame.K_r:
                    pos = [-1, -1]
                    pressed = False
                    curva = Spline(max, res)

                if evento.key == pygame.K_c:
                    curva.Clear()

        # LÓGICA---------------------------------------------LÓGICA---------------------------------------------LÓGICA
        
        curva.Update(fps)

        if(pressed):
            pos = pygame.mouse.get_pos()
        
        # DIBUJO---------------------------------------------DIBUJO---------------------------------------------DIBUJO

        pantalla.fill(FONDO)
     
        curva.Draw(pantalla, pressed)

        
        #fuente = pygame.font.Font(None, 75)
        #txt = fuente.render('GAME OVER', True, (0,0,0))
        #pantalla.blit(txt, [200,300])

        pygame.display.flip()
        reloj.tick(fps)

    pygame.quit()
