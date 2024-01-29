a, b = map(int, input('Введите границы диапазона:\n').split())
for i in range(a, b + 1):
    count = 0
    for j in range(2, i):
        if i % j == 0:
            count += 1
            if count > 2:
                count = 0
                break
    if count == 2:
        print(i, end=' ')
