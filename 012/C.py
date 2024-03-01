x, d = map(int, input('Введите X и D:\n').split())
k = x + d*(5-1)
A = [i for i in range(k,x - 1,-d)]
print(*A)