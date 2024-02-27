def f(n):
    if n == 0:
        return 1
    return n * f(n - 1)


d = int(input("Сколько деталей в ящике:\n"))
a = int(input('Сколько деталей вы хотите взять:\n'))
c = int(f(d) / (f(d - a) * f(a)))
print(f'{c} способов существует')
