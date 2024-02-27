a, b, c, d = map(int, input('Введите четыре числа: ').split())
if a >= b and a >= c and a >= d:
    m = a
elif b >= a and b >= c and b >= d:
    m = b
elif c >= a and c >= b and c >= d:
    m = c
else:
    m = d
print('Наибольшее число ', m)