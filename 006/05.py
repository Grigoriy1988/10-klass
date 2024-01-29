n = 10000
sum_first, sum_second = 0, 0
for first in range(1, n + 1):
    for i in range(1, first):
        if first % i == 0:
            sum_first += i
    for i in range(1, sum_first):
        if sum_first % i == 0:
            sum_second += i
    if (sum_second == first and sum_second != sum_first and sum_second < sum_first):
        print(sum_second, sum_first)
    sum_first, sum_second = 0, 0
