M = [9, 4, 2, 5 ,7, 1, 8, 6, 3]

pos = 0

while(pos<len(M)):
    menor = pos
    for i in range(pos, len(M)):
        if(M[i]<M[menor]):
            menor = i

    aux = M[pos]
    M[pos] = M[menor]
    M[menor] = aux

    pos += 1

    print(M)
