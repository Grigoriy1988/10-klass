def print_dig(n):
    if n > 0:
        print(n % 10)
        print_dig(n // 10)


print_dig(1893)
