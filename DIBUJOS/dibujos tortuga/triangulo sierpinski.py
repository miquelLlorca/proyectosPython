from turtle import Screen, Turtle
from math import cos
def triangulo(x):
    for i in range(3):
        tortuga.fd(x)
        tortuga.lt(120)
        
def pos(x):
    tortuga.up()
    tortuga.goto(350, -350)
    tortuga.down()
    tortuga.setheading(120)
    tortuga.fd(x)
    tortuga.lt(60)
    triangulo(x)
    
pantalla = Screen()
pantalla.setup(825, 825)
pantalla.screensize(800,800)
tortuga = Turtle()

t = 700
tortuga.up()
tortuga.goto(-350, -350)
tortuga.down()
triangulo(t)
for i in range(10):
    t = t/2
    pos(t)
