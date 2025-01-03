import pygame

class Teclado:
    def __init__(self, x, y, t):
        self.teclas = []
        self.x = x
        self.y = y

        posTX = x
        posTY = y
        for c in ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]:
            self.teclas.append(Tecla(c, posTX, posTY, t))
            posTX += t

        posTX = x + t/3
        posTY += t
        for c in ["a", "s", "d", "f", "g", "h", "j", "k", "l", "ñ"]:
            self.teclas.append(Tecla(c, posTX, posTY, t))
            posTX += t

        posTX = x + 2*t/3
        posTY += t
        for c in ["z", "x", "c", "v", "b", "n", "m"]:
            self.teclas.append(Tecla(c, posTX, posTY, t))
            posTX += t


    def EncuentraLetra(self, letra):
        n = 0
        for t in self.teclas:
            if(t.letra == letra):
                return n
            n += 1


    def Draw(self, pulsada):
        for t in self.teclas:
            t.Draw(t.letra==pulsada)
    

    def DrawCamino(self, palabra):
        camino = []
        for c in palabra:
            camino.append(self.EncuentraLetra(c))

        longitud = 0
        for i in range(len(camino)-1):
            p1 = self.teclas[camino[i]].GetCenter()
            p2 = self.teclas[camino[i+1]].GetCenter()
            pygame.draw.line(pantalla, ROJO, p1, p2, 4)

            longitud += ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

        return longitud/100




class Tecla:
    def __init__(self, letra, x, y, t):
        self.letra = letra
        self.x = x
        self.y = y
        self.t = t

    
    def Draw(self, pulsada):
        if(pulsada):
            pygame.draw.rect(pantalla, (0, 0, 150), [self.x+3, self.y+3, self.t-6, self.t-6])
        pygame.draw.rect(pantalla, NEGRO, [self.x+3, self.y+3, self.t-6, self.t-6], 3)

        fuente = pygame.font.Font(None, 75)
        txt = fuente.render(self.letra, True, NEGRO)
        pantalla.blit(txt, [self.x + 20, self.y + 10])


    def GetPos(self):
        return [self.x, self.y]


    def GetCenter(self):
        return [self.x+self.t/2, self.y+self.t/2]





# ========================================================================================================================================

NEGRO = (0, 0 ,0)
ROJO = (255, 0, 0)

teclado = Teclado(100, 500, 150)
pulsado = False
teclaPulsada = ""
palabra = ""


pygame.init()
dimensiones = [1800, 1000]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Longitud palabras")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

        if evento.type == pygame.KEYUP:
            pulsado = False
            teclaPulsada = ""

        if evento.type == pygame.KEYDOWN:
            pulsado = True
            if evento.key == pygame.K_BACKSPACE: # borrar
                teclaPulsada = ""
                palabra = palabra[0:-1] + ""
                pulsado = False

            elif evento.key == pygame.K_a: # letras...
                teclaPulsada = "a"
                palabra += "a"
            elif evento.key == pygame.K_b:
                teclaPulsada = "b"
                palabra += "b"
            elif evento.key == pygame.K_c:
                teclaPulsada = "c"
                palabra += "c"
            elif evento.key == pygame.K_d:
                teclaPulsada = "d"
                palabra += "d"
            elif evento.key == pygame.K_e:
                teclaPulsada = "e"
                palabra += "e"
            elif evento.key == pygame.K_f:
                teclaPulsada = "f"
                palabra += "f"
            elif evento.key == pygame.K_g:
                teclaPulsada = "g"
                palabra += "g"
            elif evento.key == pygame.K_h:
                teclaPulsada = "h"
                palabra += "h"
            elif evento.key == pygame.K_i:
                teclaPulsada = "i"
                palabra += "i"
            elif evento.key == pygame.K_j:
                teclaPulsada = "j"
                palabra += "j"
            elif evento.key == pygame.K_k:
                teclaPulsada = "k"
                palabra += "k"
            elif evento.key == pygame.K_l:
                teclaPulsada = "l"
                palabra += "l"
            elif evento.key == pygame.K_m:
                teclaPulsada = "m"
                palabra += "m"
            elif evento.key == pygame.K_n:
                teclaPulsada = "n"
                palabra += "n"
            elif evento.key == pygame.K_o:
                teclaPulsada = "o"
                palabra += "o"
            elif evento.key == pygame.K_p:
                teclaPulsada = "p"
                palabra += "p"
            elif evento.key == pygame.K_q:
                teclaPulsada = "q"
                palabra += "q"
            elif evento.key == pygame.K_r:
                teclaPulsada = "r"
                palabra += "r"
            elif evento.key == pygame.K_s:
                teclaPulsada = "s"
                palabra += "s"
            elif evento.key == pygame.K_t:
                teclaPulsada = "t"
                palabra += "t"
            elif evento.key == pygame.K_u:
                teclaPulsada = "u"
                palabra += "u"
            elif evento.key == pygame.K_v:
                teclaPulsada = "v"
                palabra += "v"
            elif evento.key == pygame.K_w:
                teclaPulsada = "w"
                palabra += "w"
            elif evento.key == pygame.K_x:
                teclaPulsada = "x"
                palabra += "x"
            elif evento.key == pygame.K_y:
                teclaPulsada = "y"
                palabra += "y"
            elif evento.key == pygame.K_z:
                teclaPulsada = "z"
                palabra += "z"


    # ---------------------------------------------------LÓGICA---------------------------------------------------
    
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill((150, 150, 150))


    teclado.Draw(teclaPulsada)
    longitud = teclado.DrawCamino(palabra)

    pygame.draw.line(pantalla, NEGRO, [0, 300], [dimensiones[0], 300], 1)


    if(palabra != ""):
        fuente = pygame.font.Font(None, 75)
        txt = fuente.render(palabra, True, NEGRO)
        pantalla.blit(txt, [10, 250])
        
        txt = fuente.render(str(round(longitud, 3))+"  cm", True, NEGRO)
        pantalla.blit(txt, [10, 300])

        
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
