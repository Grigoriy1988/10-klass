from random import randint
n = int(input('Введите количество элементов '))
A = [randint(-10,10) for _ in range(n)]
print(f'Массив А:\n{' '.join(str(i) for i in A)}')
buf1 = A[0]
for i in range(n-1):
    buf2 = A [i+1]
    A[i+1] = buf1
    buf1 = buf2
A[0] = buf2
print(f'Массив А:\n{' '.join(str(i) for i in A)}')