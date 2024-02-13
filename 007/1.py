def f(n):
    # вариант №1
    # s = 0
    # for i in str(n):
    #     s+=(int(i))
    # вариант №2
    # s = sum(int(i) for i in str(n))
    # вариант №3
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

n = 123
print(f'Сумма цифр числа {n} равна {f(n)}')