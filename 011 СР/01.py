import sys
sys.setrecursionlimit(3027)
def f(n):
    if n<11:
        return n
    return f(n-1)+n


print(f(2024) - f(2021))