'''
Если число a больше единицы, напечатаем перевод в двоичную систему числа,
равного целой части от деления a на два.
В противном случае напечатаем остаток от деления a на два.
'''


def bin(a):
    if a > 1:
        bin(a // 2)
    print(a % 2, end="")

n = int(input('Введите число для перевода '))
bin(n)
