
x = -2
y = -2
while(x>1000 or x<0 or y>1000 or y<0):
    x = int(input("n = "))
    y = int(input("m = "))

rango = 0
for i in range(x+y):
    rango += (i+1)
rango += (x+1)
print(rango)
