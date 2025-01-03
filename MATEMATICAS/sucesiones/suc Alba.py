x = [1]
for i in range(10):
    term = x[i]*(x[i]+1)
    print(term)
    x.append(term)


