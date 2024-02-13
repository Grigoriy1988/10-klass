def tr(a, b, c):
    if a < b + c and b < c + a and c < a + b:
        return True
    return False


a, b, c = map(float, input('Введите стороны треугольника\n').split())
if tr(a, b, c):
    print('Треугольник существует')
else:
    print('Треугольник не существует')
