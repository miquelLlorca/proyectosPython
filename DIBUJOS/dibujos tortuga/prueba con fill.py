from turtle import Screen, Turtle

pantalla2 = Screen()
pantalla2.setup(825, 825)
pantalla2.screensize(800,800)
tortuga = Turtle()

j = 3
ang = 360/3
long = 100

tortuga.color('#101010', '#2c95b5')
tortuga.begin_fill()
for i in range(j):
    tortuga.fd(long)
    tortuga.left(ang)
tortuga.end_fill()
