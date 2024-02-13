def isPrime(n):
    if n == 1:
        return False
    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


a = int(input('Введите натуральное число:\n'))
d = a
while d > 0:
    if not isPrime(d):
        print(f'Число {a} не гиперпростое.')
        break
    d = d // 10
else:
    print(f'Число {a} гиперпростое.')
