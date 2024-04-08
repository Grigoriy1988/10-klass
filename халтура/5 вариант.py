x = float(input('Введите число x '))
y = 0
for i in range(1, 4):
    k = 0
    for g in range(3, 6):
        k = k + 2 * x - i ** 2 + g
    y = y + k
print(f'f({x})= {y}')
# если не изучали F строки, то вывод как в строке 10
print('f(', x, ') = ', y)
