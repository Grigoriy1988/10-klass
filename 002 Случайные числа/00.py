# Пример

# import random
# #from random import * #подключение всего модуля
# print(f'случайное целое число:\n{randint(10,60)}')
# print(f'случайное дробное число на отрезке [0,1):\n{random()}')
# print(f'случайное дробное число:\n{uniform(1, 35) }')
print('Введите три целых числа:')
a, b = [int(i) for i in input().split()]
if a > b:
    m = a
if b > a:
    m =b
print(f'Максимальное число {m}')
