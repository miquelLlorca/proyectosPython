from turtle import Screen, Turtle

pantalla2 = Screen()
pantalla2.setup(825, 825)
pantalla2.screensize(800,800)
tortuga = Turtle()
for i in range(18):
    tortuga.left(20)
    tortuga.circle(20)
    tortuga.forward(50)
