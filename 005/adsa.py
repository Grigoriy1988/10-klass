a = int(input('Введите начало отрезка: '))
b = int(input(' Введите конец отрезка: '))
h = int(input('Введите шаг: '))
if h > 0:
    a, b = min(a, b), max(a, b) + 1
else:
    b, a = min(a, b) - 1, max(a, b)
for x in range(a, b, h):
    print(x)
