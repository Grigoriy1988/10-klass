from random import randint


def fibonacci(num):
    a = 1
    b = 1
    while num >= b:
        a, b = b, a + b
    if num == a:
        return True
    return False


n = int(input('Введите количество элементов '))
A = [randint(0, 100) for _ in range(n)]
print(f'Массив A:\n{' '.join(str(i) for i in A)}')
B = [i for i in A if fibonacci(i)]
print(f'Массив B:\n{' '.join(str(i) for i in B)}')