# def factor(n):
#     ans = []
#     d = 2
#     while d * d <= n:
#         if n % d == 0:
#             ans.append(d)
#             n //= d
#         else:
#             d += 1
#     if n > 1:
#         ans.append(n)
#     return ans

def factor(n, d):
    if d * d <= n:
        if n % d == 0:
            r.append(d)
            factor(n // d, d)
        else:
            factor(n, d + 1)
    elif n > 1:
        r.append(n)
    return '*'.join(str(i) for i in r)


n = int(input())
d = 2
r = []
print(f'{n} = {factor(n, d)}')
