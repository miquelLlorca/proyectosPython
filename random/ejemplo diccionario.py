def printdic(d):
    for elemento in d.keys(): #d.keys() devuelve una lista con los elementos, tambien se puede usar ''for x in d''
        print(elemento, '-->', d[elemento])
    
d = {}

d['Ivan'] = '644340370'
d['Alba'] = '640741193'
d['Miquel'] = '646849907'
d['Maria'] = '987654321'
d['wetj'] = '67564534232'

print(list(d.keys()))
print()

printdic(d)

print()

del d['wetj']
printdic(d)


