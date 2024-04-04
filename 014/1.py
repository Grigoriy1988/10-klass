from random import randint

n = int(input('Введите количество элементов '))
A = [randint(0, 5) for _ in range(n)]
print(f'Массив:\n{' '.join(str(i) for i in A)}')
m1 = 0
m2 = 0
for i in range(1, n):
    if A[i] >= A[m1]:
        if m1 == m2:
            m1, m2 = i, m1
        elif A[m2] <= A[m1]:
            m1, m2 = i, m1
    else:
        if m2 == m1:
            m2 = i
        elif A[i] >= A[m2]:
            m2 = i
print('Максимальный элемент: ', 'A[', m1, ']=', A[m1])
print('Второй максимум:', 'A[', m2, ']=', A[m2])
