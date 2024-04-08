from random import randint

n = int(input('Введите количество элементов '))
A = [randint(-100, 100) for _ in range(n)]
print(f'Массив A:\n{' '.join(str(i) for i in A)}')
B = [i for i in A if i <=0]
C = [i for i in A if i >0]
B.sort()
C.sort(reverse=True)
B= C+B
print(*B)
