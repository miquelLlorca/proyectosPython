import pygame
import numpy as np

class Nodo:
    def __init__(self, d):
        self.d = d
    
    def calcCurva(self):
        '''
                            ____
                        /           \
                     /                 \
                  /                       \
                /                           \
            A  o                             o  B


            Se calcula el sin() de 0 a 2*pi y lo escala


        '''
        curva = []
        for i  in np.linspace(0, 180, self.d):
            curva.append(500*(self.d/1840)*np.sin(np.radians(i)))
        
        return curva


class OndaEstacionaria:
    def __init__(self, nodo, frecuencia, eje):
        self.nodo = nodo
        self.frecuencia = frecuencia
        self.curva = nodo.calcCurva()
    
    '''
                              ____
                         /           \  
                     /                   \
                  /                         \
                /                             \
            A  o                               o  B                          o  C
                                                \                           /
                                                  \                       /
                                                     \                 /
                                                        \    ____   /
            A  o                             o  B
            frecuencia = numero de nodos


        '''
    










'''
======================================================================================================================
======================================================================================================================
======================================================================================================================
'''

if(__name__=="__main__"):
    
    #ARCO IRIS
    COLORES = [ (255,   0,   0), # ROJO
                (255, 100,   0), # NARANJA
                (255, 255,   0), # AMARILLO
                (  0, 255,   0), # VERDE
                (  0, 100, 255), # AZUL CLARO
                (  0,   0, 255), # AZUL OSCURO
                (200,   0, 255), # MORADO
                ]


    def dibujaCurva(curva, dir, d, n, eje, frecuencia):
        print(curva)
        for i in range(len(curva)):
            pygame.draw.rect(pantalla, COLORES[(frecuencia-1)%len(COLORES)], [n*d + i + 0.2*n, eje + dir*curva[i], 2, 2])



    def dibujaOnda(onda):
        dir = -1
        for i in range(onda.frecuencia):
            dir *= 1
            dibujaCurva(onda.curva, dir, onda.nodo.d, i, eje, onda.frecuencia)

    


    NEGRO = (0, 0 ,0)
    BLANCO = (255, 255, 255)
    VERDE = (0, 255, 0)
    ROJO = (255, 0, 0)
    AZUL = (0, 0, 255)
    VIOLETA = (98, 0, 255)




    dimensiones = [1840,1015]
    eje = dimensiones[1]/2

    ondas = []
    for i in range(7*5):
        ondas.append(OndaEstacionaria(Nodo(int(dimensiones[0]/(i+1))), i+1, eje))
    









    pygame.init()

    pantalla = pygame.display.set_mode(dimensiones) 
    pygame.display.set_caption("Ondas")
    hecho = False
    reloj = pygame.time.Clock()

    while not hecho:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                hecho = True

        # ---------------------------------------------------LÓGICA---------------------------------------------------
        
        
        # ---------------------------------------------------DIBUJO---------------------------------------------------

        pantalla.fill(NEGRO)

        for i in range(len(ondas)):
            dibujaOnda(ondas[i])
            
        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()
