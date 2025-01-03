from random import randrange

PU_TYPES = ["x3", "+3", "stop"]




class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def Distance(self, other):
        dX = self.x - other.x
        dY = self.y - other.y
        dist = ( (dX)**2 + (dY)**2 )**0.5

        axis = 0 if dX<dY else 1

        return dist, axis


# =========================================================================================================================


class PowerUp:
    def __init__(self, pos, t):
        self.pos = pos
        self.type = t


    def Update(self):
        self.pos.y += 10 # no se que v poner en verda


# =========================================================================================================================


class Ball:
    def __init__(self, pos):
        self.pos = pos
        self.v = Vector(0, 0)
    

    def Update(self, dim, tam):
        if(not(0 <= self.pos.x+self.v.x <= dim[0]-tam)):
            self.Bounce(0)
        if(not(0 <= self.pos.y+self.v.y <= dim[1])):
            self.Bounce(1)
        self.pos.x += self.v.x
        self.pos.y += self.v.y
    

    def Bounce(self, axis):
        if(axis == 0):
            self.v.x = -1 * self.v.x
        elif(axis == 1):
            self.v.y = -1 * self.v.y


# =========================================================================================================================


class Racket:
    def __init__(self, pos, tam):
        self.pos = pos
        self.tam = tam
        self.a = pos.x-tam
        self.b = pos.x+tam
        self.move = 0 # -1, 0, 1 // izq stop der

    
    def Update(self, dim):
        v = 15
        if(self.move == 1  and self.b+v <= dim[1] or
           self.move == -1 and self.a-v >= 0 ):
            self.pos.x += self.move * v 
            self.a = self.pos.x-self.tam
            self.b = self.pos.x+self.tam

# =========================================================================================================================


class Brick:
    def __init__(self, pos, color):
        self.pos = pos
        self.color = color


# =========================================================================================================================
# Funciones para crear niveles

def N1(dim, tam):
    bricks = []
    x0 = 40
    y0 = 40
    colors = [(255, 0, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255)]

    x = x0
    y = y0
    for block in range(4):
        
        x1 = x+200
        while(x < x1):
            x += 5
            y = y0
            while(y < dim[1]*2/3):
                y += 5
                bricks.append(Brick(Vector(x, y), colors[block]))
                y += tam
                
            x += tam
        x += 40

    return bricks

# =========================================================================================================================


class Game:
    def __init__(self, dim, tam):
        self.tam = tam # para bricks y balls
        self.dim = dim
        self.stop = 0
        self.powerUps = []
        self.generateBricks = N1
        self.bricks = self.generateBricks(dim, tam)
        self.balls = [Ball(Vector(dim[0]/2-tam/2, dim[1]*5/6 - tam-2))]
        self.started = False
        self.racket = Racket(Vector(dim[0]/2, dim[1]*5/6), 100)
        self.lives = 3

    def Restart(self):
        self.lives -= 1
        self.balls = [Ball(Vector(self.dim[0]/2-self.tam/2, self.dim[1]*5/6 - self.tam-2))]
        self.racket = Racket(Vector(self.dim[0]/2, self.dim[1]*5/6), 100)
        self.started = False
        
        if(self.lives == 0):
            self.bricks = self.generateBricks(self.dim, self.tam)


    def Throw(self):
        self.balls[0].v.x = randrange(-5, 5)
        self.balls[0].v.y = 10
        self.started = True


    def Update(self):
        # mover pelotas
        #       matar pelotas
        if(self.stop > 0):
            self.stop -= 1

        broken = []
        for i in range(len(self.balls)):
            self.balls[i].Update(self.dim, self.tam)
            if(self.stop==0 and self.balls[i].pos.y > self.dim[1]-self.tam): # sin barrera
                broken.append(i)
            elif(self.stop!=0 and self.balls[i].pos.y > self.dim[1]-self.tam): # con barrera
                self.balls[i].Bounce(1)
        
        for n in broken[::-1]:
            self.balls.pop(n)
        
        if(self.balls == []):
            self.Restart()
            

        # romper bloques
        #       soltar powerups
        broken = []
        for i in range(len(self.bricks)):
            for bl in self.balls:
                dist, axis = self.bricks[i].pos.Distance(bl.pos)
                if(dist <= self.tam):
                    broken.append(i)
                    bl.Bounce(axis)
                    #self.powerUps.append(PowerUp(self.bricks[i].pos, PU_TYPES[randrange(0, len(PU_TYPES))]))
                    break

        for n in broken[::-1]:
            self.bricks.pop(n)


        # mover raqueta
        #       rebotar pelotas
        #       coger powerups
        self.racket.Update(self.dim)
        
        for i in range(len(self.balls)):
            if( self.racket.pos.y-self.tam <= self.balls[i].pos.y <= self.racket.pos.y ): # coincide la y?
                if(self.racket.pos.x-self.racket.tam <= self.balls[i].pos.x <= self.racket.pos.x+self.racket.tam):# coincide la x?
                    self.balls[i].Bounce(1)
        
        broken = []
        for i in range(len(self.powerUps)):
            if(self.balls[i].pos.y > self.dim[1]-self.tam):
                broken.append(i)
                pass
            if( self.racket.pos.y-self.tam <= self.powerUps[i].pos.y <= self.racket.pos.y ): 
                if(self.racket.pos.x-self.racket.tam <= self.balls[i].pos.x <= self.racket.pos.x+self.racket.tam):
                    
                    if(self.powerUps[i].type == "x3"):
                        newBs = []
                        for b in self.balls:
                            newBs += b.Multiply()
                        self.balls += newBs

                    elif(self.powerUps[i].type == "+3"):
                        b1 = Ball(Vector(self.dim[0]/2, self.dim[1]*5/6))
                        b1.v.x = 0
                        b1.v.y = -1
                        self.balls.append(b1)

                        b1 = Ball(Vector(self.dim[0]/2, self.dim[1]*5/6))
                        b1.v.x = 0
                        b1.v.y = -1
                        self.balls.append(b1)

                        b1 = Ball(Vector(self.dim[0]/2, self.dim[1]*5/6))
                        b1.v.x = 0
                        b1.v.y = -1
                        self.balls.append(b1)

                    elif(self.powerUps[i].type == "stop"):
                        self.stop = 240


                    self.powerUps.pop(i)
                    i -= 1

        for n in broken[::-1]:
            self.powerUps.pop(n)
