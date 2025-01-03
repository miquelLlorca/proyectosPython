from turtle import Screen, Turtle
import random

random.seed(24)
def creaCol():
    col = '#'
    lista = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    for i in range(6):
        col += lista[random.randrange(len(lista))]
    return col


pantalla = Screen()
pantalla.setup(825, 825)
pantalla.screensize(800,800)
tortuga = Turtle()



long = 100

tortuga.up()
tortuga.right(90)
tortuga.fd(350)
tortuga.right(90)
tortuga.fd(50)
tortuga.right(180)
tortuga.down()

for j in range(20, 2, -1):
    tortuga.color('#101010', creaCol())
    tortuga.begin_fill()
    ang = 360/j
    for i in range(j):
        tortuga.fd(long)
        tortuga.left(ang)
    tortuga.end_fill()
