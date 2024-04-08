from random import randint

n = int(input('Введите количество элементов '))
A = [randint(0, 10) for _ in range(n)]
print(f'Массив A:\n{' '.join(str(i) for i in A)}')
A = list(reversed(A[:n // 2])) + list(reversed(A[n // 2:]))
print(f'Массив A:\n{' '.join(str(i) for i in A)}')