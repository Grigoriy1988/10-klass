from random import randint
def binary_s(L,R,X,A_list):
    k = 0
    while L < R -1:
        k+=1
        c = (L+R)//2
        if X < A_list[c]:
            R = c
        else:
            L = c
    return f'Число {X} найдено\nКоличество сравнений:{k}' if A_list[L] == X else f"НЕ найдено\nКоличество сравнений:{k}"

n = int(input('Введите количество элементов '))
A = [randint(1, 100) for _ in range(n)]
print(f'Массив A:\n{' '.join(str(i) for i in A)}')
A.sort()
print(f'После сортировки:\n{' '.join(str(i) for i in A)}')
x = int(input('Введите число X\n'))
print(binary_s(0,n,x,A))
x = int(input('Введите число X\n'))
print(binary_s(0,n,x,A))