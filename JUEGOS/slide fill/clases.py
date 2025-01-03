import random




# ===========================================================  CONSTANTES Y FUNCIONES AUXILIARES ==============================================================


COLORES = [
    (255, 255, 255),
    (255,   0,   0),
    (  0, 255,   0),
    ( 13, 142, 255),
    (252, 240,   3),
    (  0, 255, 110),
    (  0, 217, 255),
    (247,   0, 255),
    (255, 157,  28),
    (177,  20, 255)
]


def findNextLevel():
    nums = []

    file = open("levels/info", "r")
    nums = [int(x) for x in file.readline().split()]
    file.close()
    nums[1] += 1

    return nums # [ nivel que toca jugar, ultimo nivel creado +1 ]


def calcColor(color):
    newColor = []
    
    for n in color:
        m = 0 if n<50 else (n-50) 
        newColor.append(m)

    return newColor


def select(entities):
    if(entities[0]):
        return "C"
    elif(entities[1]):
        return "G"
    elif(entities[1]):
        return "P"
    else:
        return "B"

# ===========================================================  CLASES  =====================================================================================


# -------------- ENTITIES
#clase padre
class Entity:
    def __init__(self, tipo):
        self.tipo = tipo


class Canon(Entity):
    def __init__(self, pos):
        Entity.__init__(self, tipo = "C")
        self.pos = pos



    #def Disparar():


    #def Update():


class Globo(Entity):
    def __init__(self, pos):
        Entity.__init__(self, tipo = "G")
        self.pos = pos


class Portal(Entity):
    def __init__(self, p1, p2):
        Entity.__init__(self, tipo = "P")
        self.p1 = p1
        self.p2 = p2


# player no necesita heredar de entity
class Player:
    def __init__(self, pos):
        self.posOriginal = pos + []
        self.pos = pos + []
        self.destiny = pos + []
        self.v = [0, 0] # dir , sentido

    def Update(self):
        if(self.pos != self.destiny):
            self.pos[self.v[0]] += self.v[1] #* 0.5 # factor para ajustar velocidad (sin factor estqa bien?)
            if(self.pos == self.destiny):
                self.pos = [int(x) for x in self.pos]

    def Move(self, destiny, v):
        self.destiny = destiny + []
        self.v = v + []


    def Moving(self):
        return not(self.pos == self.destiny)





# --------------- TABLEROS
# clase padre
class Tablero:
    def __init__(self, size, n):
        self.tablero = []
        self.size = size
        self.n = n
        self.colorFill = 0
        self.colorBloque = 0
        self.player = 0
        self.entities = []


    def Set(self, pos, ent, pos2=[0, 0]):
        if(ent == "B"):
            if(self.tablero[pos[0]][pos[1]] == "B"):
                self.tablero[pos[0]][pos[1]] = "0"
            else:
                self.tablero[pos[0]][pos[1]] = "B"

        elif(ent == "C"):
            if(pos not in [e.pos if e.tipo!="P" else [e.pos1, e.pos2] for e in self.entities]):
                self.entities.append(Canon(pos))
        elif(ent == "G"):
            if(pos not in [e.pos if e.tipo!="P" else [e.pos1, e.pos2] for e in self.entities]):
                self.entities.append(Globo(pos))
        elif(ent == "P"):
            posS = [e.pos if e.tipo!="P" else [e.pos1, e.pos2] for e in self.entities]
            if(pos not in posS and pos2 not in posS):
                self.entities.append(Portal(pos, pos2))



    def CheckCell(self, direccion, sentido, p):
        p[direccion] += sentido
        return self.tablero[p[0]][p[1]]


    def Fill(self):
        self.tablero[int(self.player.pos[0])][int(self.player.pos[1])] = "F"


    def Slide(self, direccion, sentido):

        if(not (self.player.Moving())):
            p = self.player.pos + []

            while(True):
                if(0 <= (p[direccion] + sentido) < self.n and
                   self.CheckCell(direccion, sentido, p+[]) != "B"):
                    p[direccion] += sentido
                else:
                    self.player.Move(destiny=p+[], v=[direccion, sentido])
                    break
    

    def Update(self):
        self.Fill()
        self.player.Update()

    def Reset(self):
        self.player.pos = self.player.posOriginal + []

        for i in range(self.n):
            for j in range(self.n):
                if(self.tablero[i][j] == "F"):
                    self.tablero[i][j] = "0"
    

    def Finished(self):
        for i in range(self.n):
            for j in range(self.n):
                if(self.tablero[i][j] == "0"):
                    return False

        # se actualiza la info
        file = open("levels/info", "r") 
        nums = [int(x) for x in file.readline().split()]
        file.close()

        file = open("levels/info", "w")
        if(nums[0]+1>nums[1]):
            file.write("1")
        else:
            file.write(str(nums[0]+1))
        file.write(" ")
        file.write(str(nums[1]))
        file.close()

        return True



# clases hijas de tablero:

class Level(Tablero):
    def __init__(self, id):
        Tablero.__init__(self, n=0, size=0)

        self.id = id
        
        inpFile = open("levels/"+str(id), "r")

        self.size = int(inpFile.readline().split()[0])
        self.n = int(inpFile.readline().split()[0])
        self.colorFill = [int(x) for x in inpFile.readline().split()]
        self.colorBloque = [int(x) for x in inpFile.readline().split()]
        self.player = Player([int(x) for x in inpFile.readline().split()])

        for i in range(self.n):
            self.tablero.append(inpFile.readline().split())

        inpFile.close()




class NuevoTablero(Tablero):
    def __init__(self, seed, n, size):
        Tablero.__init__(self, n=n, size=size)
        random.seed(seed)
        self.seed = seed
        self.colorFill = COLORES[random.randint(0, len(COLORES)-1)]
        self.colorBloque = calcColor(self.colorFill)
        self.player = Player([random.randint(0, n-1),random.randint(0, n-1)])

        self.tablero = []
        for i in range(n):
            self.tablero.append([])
            for j in range(n):
                self.tablero[i].append("0")

        bloques = random.randint(n, n*2)
        for i in range(bloques):
            x = random.randint(0, n-1)
            y = random.randint(0, n-1)
            if([x, y] != self.player.pos):
                self.tablero[x][y] = "B"

    

    def Save(self):
        for i in range(self.n): # todas las posiciones no visitadas se convierten en bloques
            for j in range(self.n):
                if(self.tablero[i][j] == "0"):
                    self.tablero[i][j] = "B"

        for i in range(self.n): # todas las posiciones visitadas se vacian
            for j in range(self.n):
                if(self.tablero[i][j] == "F"):
                    self.tablero[i][j] = "0"


        outFile = open("levels/"+str(self.seed), "w") # se crea un archivo y se escriben los datos del nivel

        outFile.write(str(self.size))
        outFile.write("\n")
        outFile.write(str(self.n))
        outFile.write("\n")
        outFile.write(str(self.colorFill[0])+" "+str(self.colorFill[1])+" "+str(self.colorFill[2]))
        outFile.write("\n")
        outFile.write(str(self.colorBloque[0])+" "+str(self.colorBloque[1])+" "+str(self.colorBloque[2]))
        outFile.write("\n")
        outFile.write(str(self.player.posOriginal[0])+" "+str(self.player.posOriginal[1]))
        outFile.write("\n")

        for l in self.tablero:
            for c in l:
                outFile.write(c+" ")
            outFile.write("\n")

        outFile.close()


        # se actualiza la info
        file = open("levels/info", "r") 
        nums = [int(x) for x in file.readline().split()]
        file.close()

        file = open("levels/info", "w")
        file.write(str(nums[0]))
        file.write(" ")
        file.write(str(nums[1]+1))
        file.close()

    





# ===============================================================================================================
