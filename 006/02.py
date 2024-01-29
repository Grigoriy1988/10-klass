n = int(input('Введите N:\n')) + 1
for i in range(1, n):
    for dig in str(i):
        if dig == '0' or i % int(dig) != 0:
            break
    else:
        print(i, end=', ')
