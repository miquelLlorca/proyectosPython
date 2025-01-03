from turtle import Screen, Turtle

def cuadricula(n, l):
    for i in range(n+1):
        tortuga.forward(l*n)
        if i == n:
            break
        tortuga.penup()
        if (i+1) % 2 == 0:
            tortuga.left(90)
            tortuga.forward(l)
            tortuga.left(90)
        else:
            tortuga.right(90)
            tortuga.forward(l)
            tortuga.right(90)
        tortuga.pendown()

    if n % 2 == 0:
        tortuga.left(90)
        pimp = 1
    else:
        tortuga.right(90)
        pimp = 0

    for i in range(n+1):
        tortuga.forward(l*n)
        if i == n:
            break
        tortuga.penup()
        if (i+1) % 2 == pimp:
            tortuga.left(90)
            tortuga.forward(l)
            tortuga.left(90)
        else:
            tortuga.right(90)
            tortuga.forward(l)
            tortuga.right(90)
        tortuga.pendown()
            
n = 4
m = 3
h = 5
l = 25
ang = 36.86989765
pantalla = Screen()
pantalla.setup(825, 825)
pantalla.screensize(800,800)
tortuga = Turtle()
tortuga.speed(10)
tortuga.shape('circle')
tortuga.resizemode('user')
tortuga.shapesize(0.4, 0.4)

cuadricula(n, l)
tortuga.penup()
tortuga.right(90)
tortuga.forward(l*n)
tortuga.left(90)
tortuga.pendown()
cuadricula(m, l)
tortuga.penup()
tortuga.right(180)
tortuga.forward(l*m)
tortuga.left(ang)
tortuga.pendown()
cuadricula(h, l)
