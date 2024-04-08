from random import randint


def fibo(num):
    a = 1
    b = 1
    while num >= b:
        a, b = b, a + b
    if num == a:
        return True
    return False


n = int(input('Введите количество элементов '))
A = [randint(0, 150) for _ in range(n)]
print(f'Массив А:\n{' '.join(str(i) for i in A)}')
B = [i for i in A if fibo(i)]
print(f'Массив B:\n{' '.join(str(i) for i in B)}')
