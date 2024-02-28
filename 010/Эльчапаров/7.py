m = 2
s = []

def boo(n, m):
    global s
    if all(n%i !=0 for i in range(2, n//2+1)):
        s.append(n)
        w=1
        for i in s:
            w *= i
        print(str(w)+'=',end='')
        print('*'.join(str(i) for i in s))
        return


    elif any(m % i == 0 for i in range(3, m//2+1)):
        boo(n, m+1)

    elif n % m == 0:
        # print('!')
        s.append(m)
        # print(s)
        boo(n // m, m)
    else:
        boo(n, m+1)

n = int(input('Введите натуральное число:'))
boo(n, m)