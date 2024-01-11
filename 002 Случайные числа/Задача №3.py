from random import *
a =randint(100,999)
print(f'Получено число {a}\n'
      f'сотни: {a//100}\n'
      f'десятки: {a%100//10}\n'
      f'единицы: {a%10}'
      f'')