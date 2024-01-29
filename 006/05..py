n = int(input())
result = 0
degree = 0  # степень 10
digits = 1  # количество цифр в числе
while True:
    if n < 9 * digits * 10 ** degree:
        result += n // digits
        break
    else:
        n -= 9 * (10 ** degree) * digits
        result += 9 * (10 ** degree)
        degree += 1
        digits += 1
print(result)