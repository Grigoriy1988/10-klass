from random import randint

n = int(input('n = '))
a = []
while len(a) != n:
    k = randint(1,n)
    if k not in a:
        a.append(k)
print(*a)
