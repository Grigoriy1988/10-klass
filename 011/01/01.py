def f(n):
    if n < 3:
        return 3
    return 2 * n + 5 + f(n - 2)


print(f(3027) - f(3023))

print(2 * 3077 + 5 + 2 * 3025 + 5)
