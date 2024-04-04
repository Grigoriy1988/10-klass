from random import randint

n = int(input('Введите количество элементов '))
A = [randint(0, 5) for _ in range(n)]
print(f'Массив:\n{' '.join(str(i) for i in A)}')
x = int(input('Что ищем:\n'))
f = False
s = []
for i in range(n):
    if A[i] == x:
        f = True
        s.append(' A[' + str(i) + ']=' + str(A[i]))
if f:
    print('Нашли:', ', '.join(i for i in s))
else:
    print('Ничего не нашли.')
