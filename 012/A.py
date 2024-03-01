from random import randrange

a, b = map(int, input().split())
A = [randrange(a, b + 1) for i in range(5)]
print(*A)
