x, d = map(int, input('Введите X и D:\n').split())
A = [i for i in range(x, x + d*(5-1)+1, d)]
print(*A)
