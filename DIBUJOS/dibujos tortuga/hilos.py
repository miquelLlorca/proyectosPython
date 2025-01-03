from turtle import Screen, Turtle

def hilos(n, xy):
    pos = []
    for i in range(1, n+1):
        pos.append(20*i)
        
    for i in range(n):
        tortuga.up()
        tortuga.goto(xy[0], pos[i]+xy[1])
        tortuga.down()
        tortuga.goto(pos[n-i-1]+xy[0], xy[1])
        
    


n = int(input('n = '))
xy = [int(x) for x in input().split()]

pantalla = Screen()
pantalla.setup(825, 825)
pantalla.screensize(800,800)
tortuga = Turtle()
tortuga.speed(10)
#tortuga.shape('circle')
tortuga.resizemode('user')
tortuga.shapesize(0.4, 0.4)


tortuga.up()
tortuga.goto(xy)
tortuga.down()
tortuga.goto(xy[0]+20*n, xy[1])
tortuga.goto(xy)
tortuga.goto(xy[0], xy[1]+20*n)

hilos(n, xy)
