
def comp(n):
    while n>10:
        suma = 0
        for x in str(n):
            suma += int(x)
        n = suma
    if n==9:
        return True
    return False

a = input().split()
A = [int(x) for x in a]

for n in A:
    perf = comp(n)
    if perf:
        print(n)
