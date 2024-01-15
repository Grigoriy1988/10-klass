number = int(input('Введите натуральное число:\n'))
previous_digit = ''
while number > 0:
    digit = number % 10
    number //= 10
    if digit == previous_digit:
        print('Да.')
        break
    previous_digit = digit
else:
    print('Нет.')
