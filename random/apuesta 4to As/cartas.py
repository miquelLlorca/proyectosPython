import random
from os import system
class Carta:
    def __init__(self, num, palo):
        self.num = num
        self.palo = palo


class Baraja:
    def __init__(self):
        self.cartas = []
        for i in range(4):
            for j in range(13):
                self.cartas.append(Carta(j+1, chr(64 + i+1)))


    def __str__(self):
        cad = ""
        for c in self.cartas:
            cad += "({}, {}) -> ".format(c.num, c.palo)

        return cad


    def Barajar(self, n):
        for i in range(n):
            a = random.randrange(0, 52)
            b = random.randrange(0, 52)

            aux = self.cartas[a]
            self.cartas[a] = self.cartas[b]
            self.cartas[b] = aux


    def Buscar4As(self):
        ases = 0
        for i in range(52):
            if(self.cartas[i].num == 1):
                ases += 1
                if(ases == 4):
                    return i+1





baraja = Baraja()

i = 0
pA = 0 # elige siempre la ultima
pB = 0 # elige random
pC = 0 # elige siempre la misma carta random
posC = random.randrange(4, 53)

while(True):
    i += 1

    baraja.Barajar(100)

    pos = baraja.Buscar4As()

    if(pos == 52):
        pA += 1
    
    if(pos == random.randrange(4, 53)):
        pB += 1

    if(pos == posC):
        pC += 1

    if(i%1000 == 0):
        system('clear')
        print("i =", i)
        print("A = {} -> {}%".format(pA, (pA/i)*100))
        print("B = {} -> {}%".format(pB, (pB/i)*100))
        print("C = {} -> {}%".format(pC, (pC/i)*100))


