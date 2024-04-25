s = input('Введите строку:\n')
for i in range(len(s)):
    if s[i] == 'а' or s[i] == 'А':
        if s[i] == 'а':
            s = s[:i] + 'б' + s[i + 1:]
        else:
            s = s[:i] + 'Б' + s[i + 1:]
    elif s[i] == 'б' or s[i] == 'Б':
        if s[i] == 'б':
            s = s[:i] + 'а' + s[i + 1:]
        else:
            s = s[:i] + 'А' + s[i + 1:]
print(f'Результат:\n{s}')
