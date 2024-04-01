from random import randint
n = int(input('Введите количество элементов '))
A = [randint(0,100) for _ in range(n)]
print(f'Массив\n{' '.join(str(i) for i in A)}')
print(f'Четные\n{' '.join(str(i) for i in A if i % 2 == 0)}')
print(f'Не четные \n{' '.join(str(i) for i in A if i % 2 != 0)}')
