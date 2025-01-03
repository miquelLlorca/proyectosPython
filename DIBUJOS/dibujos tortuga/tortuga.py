from turtle import Screen, Turtle

pantalla = Screen()
pantalla.setup(825, 825)
pantalla.screensize(800,800)
tortuga = Turtle()
tortuga.pensize(5)
tortuga.pencolor('pink')

for i in range(4):
    tortuga.forward(100)
    if i != 3:
        tortuga.left(90)

tortuga.penup()
tortuga.right(90)
tortuga.forward(100)
tortuga.pendown()
tortuga.pensize(3)
tortuga.pencolor('green')

for i in range(3):
    tortuga.forward(100)
    if i != 2:
        tortuga.right(120)

tortuga.penup()
tortuga.home()
tortuga.pencolor('red')
tortuga.pensize(10)
tortuga.pendown()
tortuga.goto(189,217)
tortuga.setheading(135)
tortuga.forward(75)
tortuga.pensize(1)
tortuga.pencolor('black')
tortuga.circle(50)
tortuga.dot(100)
tortuga.pencolor('white')
t = 'hola'
tortuga.write(t)
pantalla.exitonclick()

