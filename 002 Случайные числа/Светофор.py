# print('Зеленый' if 0 <= float(input()) % 5 <= 3 else 'Красный')
time = float(input())
x = time % 5
if x >= 0 and x <= 3:
    print('Зеленый')
else:
    print('Красный')
