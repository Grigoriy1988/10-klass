s = input('Введите строку:\n')
f = False
count = 0
for i in range(len(s)):
    if s[i] != " " and not (f):
        count += 1
        f = True
    elif s[i] == " ":
        f = False
print(f'Найдено слов:{count}')
