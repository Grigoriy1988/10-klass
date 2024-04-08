from random import randint

n = int(input('Введите количество элементов '))
A = [randint(-10,10) for _ in range(n)]
print(f'Массив А:\n{' '.join(str(i) for i in A)}')
B = [i for i in A if i < 0 and i % 2 == 0]
print(f'Массив B:\n{' '.join(str(i) for i in B)}')
# A = []
# print('Массив А: ', end='')
# for i in range(n):
#     A.append(randint(-10, 10))
#     print(A[i], end=' ')
# B = []
# j = 0
# print('\nМассив B: ', end='')
# for i in A:
#     if i < 0 and i % 2 == 0:
#         B.append(i)
#         print(B[j], end=' ')
#         j += 1
