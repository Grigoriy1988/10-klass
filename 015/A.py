from random import randint

n = int(input('Введите количество элементов '))
A = [randint(-10, 10) for _ in range(n)]
print(f'Массив A:\n{' '.join(str(i) for i in A)}')
B = [i for i in A if i < 0 and i %2 == 0]
print(f'Массив B:\n{' '.join(str(i) for i in B)}')
