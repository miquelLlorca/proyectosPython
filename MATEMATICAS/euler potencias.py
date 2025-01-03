def potencia(b, e, m):
    done = False
    term = b
    pot = 1
    print("\n----------{}^{}----------".format(b, e))
    
    while(not done):
        term = term**2
        pot *= 2
        print("P={} -> {} ".format(pot, term), end='')

        if(term>=m):
            term = term%m
            print("=", term)
        else:
            print()

        if(pot == e):
            done = True
        elif(pot*2>e):
            if(e-pot>5):
                tF = potencia(b, e-pot, m)
            else:
                tF = b**(e-pot)

            
            
            print("P={}, ({}+{}), {}*{} = ".format(e, pot, e-pot, term, tF), end='')
            term *= tF
            print(term, "=", term%m)
            done = True

    print("----------{}^{} = {}----------\n".format(b, e, term%m))
    return term%m


b = int(input("Base: "))
e = int(input("Exponente: "))
m = int(input("Modulo: "))

p = potencia(b, e, m)

