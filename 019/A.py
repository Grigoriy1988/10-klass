def A(line):
    s = ''
    for i in line:
        if i != ' ':
            s+=i
        else:
            break
    return s

word = input('Введите строку: ')
print(A(word))