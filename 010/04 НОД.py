def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


a, b = map(int, input('Введите два натуральных числа:\n').split())
print(f'НОД({a},{b}) = {gcd(a, b)}')
