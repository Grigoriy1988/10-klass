from random import randint
n = int(input('Введите количество элементов '))
A = [randint(0,100) for _ in range(n)]
s1 = sum(A[i] for i in range(0,n,2))
s2 = sum(A[i] for i in range(1,n,2))
print(f'Массив\n{' '.join(str(i) for i in A)}')
print(f'Знакопеременную сумма {s1-s2}')