from random import randint

n = int(input('Введите количество элементов '))
A = [randint(-1 - 0, 100) for _ in range(n)]
print(f'Массив A:\n{' '.join(str(i) for i in A)}')
for i in range(n - 1):
    for j in range(n - 2, i - 1, -1):
        if A[j + 1] > A[j]:
            A[j], A[j + 1] = A[j + 1], A[j]
print(f'Массив A:\n{' '.join(str(i) for i in A)}')
