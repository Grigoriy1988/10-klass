from random import randint


def binary_search(L, R, X, A_list):
    k = 0
    while L < R - 1:
        k += 1
        c = (L + R) // 2
        if X < A_list[c]:
            R = c
        else:
            L = c
    return f"A[{L}]={X}\nКоличество сравнений: {k}" if A[L] == X else f"Не нашли!"


n = int(input('Введите количество элементов '))
A = [randint(0, 100) for _ in range(n)]
print(f'Массив A:\n{' '.join(str(i) for i in A)}')
A.sort()
print(f'После сортировки:\n{' '.join(str(i) for i in A)}')
x = int(input('Введите число X:\n'))
print(binary_search(0, n, x, A))
