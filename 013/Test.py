from random import randint


def f(n):
    if n == 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


n = int(input('Введите количество элементов '))
A = [randint(0, 100) for _ in range(n)]
print(f'Массив:\n{' '.join(str(i) for i in A)}')
s = sum(i for i in A if f(i))
k = sum(1 for i in A if f(i))
print(s/k)
