def summa(a, b):
    if a == b:
        return a
    return summa(a,b-1) + b


a,b = map(int, input('Введите два натуральных числа:\n').split())
# print(summa(a,b))

s = 0
for i in range(a,b+1):
    s+=i
print(s)