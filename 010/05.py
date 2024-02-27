def A(n, m):
    print('Вызов')
    if n == 0:
        return m + 1
    elif n != 0 and m == 0:
        return A(n - 1, 1)
    return A(n - 1, A(n, m - 1))

print(A(1,3))
print(A(4,2))