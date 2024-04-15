from random import randint
n = int(input('Введите количество элементов '))
A = [randint(-1 - 0, 100) for _ in range(n)]
print(f'Массив A:\n{' '.join(str(i) for i in A)}')
A1 = sorted(A[:n//2],reverse=True)
A2 = sorted(A[n//2:])
B = A1 + A2

print(f'После сортировки:\n{' '.join(str(i) for i in B)}')
