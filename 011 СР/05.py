'''
F(n) = 1, если n = 0,
F(n) = F(n // 100) · (n % 10), если n > 0 и n нечётно;
F(n) = F(n // 100), если n > 0 и n чётно.
10**9 ≤ n ≤ 6·109 F(n) = 21.

'''


def f(n):
    print(n)
    if n == 0:
        return 1
    elif n % 2 != 0:
        return f(n // 100) * (n % 10)
    return f(n // 100)


# for i in range(10*9,10000005000):
#     if f(i) ==21:
#         print(f'{i} \t {f(i)}')
f(11131867)