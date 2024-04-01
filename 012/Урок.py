from random import randint
n = int(input('Введите n: '))
print('Массив:')
a = []
while len(a)<n:
    k = randint(1,n)
    if not (k in a):
        a.append(k)
print(*a)
