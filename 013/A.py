from random import randint

n = int(input('Введите количество элементов '))
A = [randint(0, 100) for _ in range(n)]
print(f'Массив:\n{' '.join(str(i) for i in A)}')
s = sum(i for i in A)
print(f'Среднее арифметическое {s / n}')
