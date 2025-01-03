from turtle import Screen, Turtle

pantalla = Screen()
pantalla.setup(825, 825)
pantalla.screensize(800,800)
tortuga = Turtle()

pos = []

tortuga.up()
tortuga.goto(150, 150)
ang = 360/5
for i in range(5):
    tortuga.fd(100)
    tortuga.left(ang)
    pos.append(tortuga.pos())

tortuga.down()
tortuga.goto(pos[1])
tortuga.goto(pos[3])
tortuga.goto(pos[0])
tortuga.goto(pos[2])
tortuga.goto(pos[4])

tortuga.up()

pos = []
tortuga.goto(-150, 100)
ang = 360/7
for i in range(7):
    tortuga.fd(100)
    tortuga.left(ang)
    pos.append(tortuga.pos())

tortuga.down()
tortuga.goto(pos[1])
tortuga.goto(pos[3])
tortuga.goto(pos[5])
tortuga.goto(pos[0])
tortuga.goto(pos[2])
tortuga.goto(pos[4])
tortuga.goto(pos[6])

tortuga.goto(pos[2])
tortuga.goto(pos[5])
tortuga.goto(pos[1])
tortuga.goto(pos[4])
tortuga.goto(pos[0])
tortuga.goto(pos[3])
tortuga.goto(pos[6])


tortuga.up()

pos = []
tortuga.goto(-150, -200)
ang = 360/9
for i in range(9):
    tortuga.fd(100)
    tortuga.left(ang)
    pos.append(tortuga.pos())

tortuga.down()

tortuga.goto(pos[1])
tortuga.goto(pos[3])
tortuga.goto(pos[5])
tortuga.goto(pos[7])
tortuga.goto(pos[0])
tortuga.goto(pos[2])
tortuga.goto(pos[4])
tortuga.goto(pos[6])
tortuga.goto(pos[8])


tortuga.goto(pos[3])
tortuga.goto(pos[7])
tortuga.goto(pos[2])
tortuga.goto(pos[6])
tortuga.goto(pos[1])
tortuga.goto(pos[5])
tortuga.goto(pos[0])
tortuga.goto(pos[4])
tortuga.goto(pos[8])
