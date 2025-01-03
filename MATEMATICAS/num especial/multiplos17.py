
for i in range(1000, 10000):
    n = int(str(i)+str(i)+str(i)+str(i))
    print(n, "->", n%17)
    if(n%17!=0):
        break