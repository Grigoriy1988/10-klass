from random import randint

n = int(input('Введите количество элементов '))
A = [randint(-1 - 0, 100) for _ in range(n)]
print(f'Массив A:\n{' '.join(str(i) for i in A)}')
k = 0

for i in range(n - 1):
    t = True
    for j in range(n - 2, i - 1, -1):
        k += 1
        if A[j + 1] < A[j]:
            A[j], A[j + 1] = A[j + 1], A[j]
            t = False
    if t:
        break
print(f'количество проходов {k}')
print(f'Массив A:\n{' '.join(str(i) for i in A)}')