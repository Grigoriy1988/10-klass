from random import randint


def prime_number(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


n = int(input('Введите количество элементов '))
A = [randint(0, 100) for _ in range(n)]
print(f'Массив A:\n{' '.join(str(i) for i in A)}')
B = [i for i in A if prime_number(i)]
print(f'Массив B:\n{' '.join(str(i) for i in B)}')