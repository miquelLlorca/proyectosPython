
a = int(input("Num mayor: "))
b = int(input("Num menor: "))
A = a
B = b
resto = 1234
print()
while(resto != 0):
    resto = a%b
    print(a, "|_", b)
    print(resto, "  ", int(a/b))
    print()
    a = b
    b = resto

print("MCD({}, {}) = {}".format(A, B, a))
print()

print("x = ", int(A/a), "* k")
print("y = ", int(B/a), "* k")
print()

mcm = int(A * (B/a))

print("MCM({}, {}) = {}".format(A, B, mcm))

