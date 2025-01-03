n  = int(input('k = '))

for i in range(n):
    a = 3*(i+1)- 2
    print('a{} = {}'.format(i+1,a),end='')
    if i != n-1:
        print(', ',end='')
print('.')
