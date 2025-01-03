import random
from os import system

class Carton:
    def __init__(self):
        self.nums = []
        self.puntos = 0
        for i in range(15): # se llena de numeros random
            n = random.randint(1, 90)
            while(n in self.nums):
                n = random.randint(1, 90)
            self.nums.append(n)


    def __str__(self):
        cad = ""
        for x in self.nums:
            cad += str(x)
            cad += " "
 
        return cad


    def Diferencia(self, other):
        diff = 0
        for n in self.nums:
            if(n in other.nums):
                diff += 1

        return diff


    def Comprueba(self, n):
        if(n in self.nums):
            self.puntos += 1

        return self.puntos == 15
        

class Player:
    def __init__(self, n):
        self.victorias = 0
        self.cartones = []
        for i in range(n):
            self.cartones.append(Carton())

    def Comprueba(self, n):
        res = False
        for c in self.cartones:
            res = res or c.Comprueba(n)

        return res




players = [Player(1), Player(2), Player(3), Player(4)]
while(True):
    nums = []
    finished = False
    while(not finished):
        
        n = random.randint(1, 90)
        while(n in nums):
            n = random.randint(1, 90)
        nums.append(n)

        for p in players:
            if(p.Comprueba(n)):
                p.victorias += 1
                finished = True
                break

    for p in players:
        print(p.victorias)
    print()
