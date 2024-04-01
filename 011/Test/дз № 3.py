'''
F(n) = 0, если n = 0,
F(n) = F(n // 8) + n % 8, если n > 0 и n чётно;
F(n) = F(n // 8), если n > 0 и n нечётно.
Определите количество значений n, таких что 89 ≤ n ≤ 810, для которых F(n) = 2.
'''


def f(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return f(n // 8) + n % 8
    return f(n // 8)






# k = 0
# for i in range(8 ** 3, 8 ** 4 + 1):
#     if f(i) == 2:
#         k += 1
# print(k)

print(10 * 5 ** 9 - 9 * 5 ** 8)
