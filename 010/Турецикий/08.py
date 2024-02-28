def count_ways(n, start=1):
    if n == 0:
        return 1
    res = 0
    for i in range(start, n +1):
        res += count_ways(n-i, i)
    return res

n = int(input("Введите натуральное число: "))
ways = count_ways(n)
print("Количество разложений:", ways)