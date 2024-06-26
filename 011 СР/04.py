'''
F(n) = n, если n < 2;
F(n) = F(n // 2)  + F(n % 2), если n ≥ 2.
Определите количество значений n < 2**30, для которых функция F(n) = 27.

'''
def f(n):
    if n < 2:
        return n
    return f(n//2) + f(n%2)

for i in range(2**0,2**10):
    print(f"при {i} f ={f(i)}")

