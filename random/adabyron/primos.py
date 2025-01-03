
def comp(n):
    if n==1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        print(n)
        return True

A = []
a = ' '
while a != '':
    a = input()
    if a!='':
        A.append(int(a))
    
total = 0
for n in A:
    primo = comp(n)
    if primo:
        total += 1

if total == 0:
    print('No prime numbers were found!')
elif total == 1:
    print('Only one prime number was found!')
elif total > 1:
    print(total, 'prime numbers were found!')
