f = [1] * 2025
for n in range(8, 2025):
    f[n] = n + 1 + f[n - 2]
print(f[2024] - f[2020])
