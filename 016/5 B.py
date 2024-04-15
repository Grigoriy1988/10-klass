from random import randint
n = int(input('Введите количество элементов '))
A = [randint(6, 10) for _ in range(n)]
print(f'Массив A:\n{' '.join(str(i) for i in A)}')
A.sort()
print(f'Массив A:\n{' '.join(str(i) for i in A)}')
k  = 1
for i in range(n-1):
    if A[i]!=A[i+1]:
        k+=1
print(k)