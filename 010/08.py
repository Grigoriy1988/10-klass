# https://neerc.ifmo.ru/wiki/index.php?title=%D0%9D%D0%B0%D1%85%D0%BE%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5_%D0%BA%D0%BE%D0%BB%D0%B8%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%B0_%D1%80%D0%B0%D0%B7%D0%B1%D0%B8%D0%B5%D0%BD%D0%B8%D0%B9_%D1%87%D0%B8%D1%81%D0%BB%D0%B0_%D0%BD%D0%B0_%D1%81%D0%BB%D0%B0%D0%B3%D0%B0%D0%B5%D0%BC%D1%8B%D0%B5
<<<<<<< HEAD
# https://www.youtube.com/watch?v=O3k9OrwIvbA
# https://habr.com/ru/articles/329948/


def p(dat):
    while len(dat) > 1:
        print('+'.join(str(i) for i in dat))
        count.append('+'.join(str(i) for i in dat))
        k = min(dat[:-1])
        i = dat.index(k)
        dat[i] += 1
        dat[-1] -= 1
        if dat[-1] == 0:
            dat.pop(-1)


count=[]
n = int(input())
p([1] * n)
print(len(count))
=======
#https://www.youtube.com/watch?v=O3k9OrwIvbA
def p(n):
    if n == 0:
        return 1
    else:

>>>>>>> origin/main
