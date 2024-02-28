def prime_factors(n, divisor=2):
    if n == 1:
        return []
    if n % divisor == 0:
        return [divisor] + prime_factors(n // divisor, divisor)
    else:
        return prime_factors(n, divisor + 1)
number = int(input("Введите число: "))
factors = prime_factors(number)
print(f"Простые сомножители числа {number} = ", '*'.join(str(i) for i in factors))