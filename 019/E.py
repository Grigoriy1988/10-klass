def coloboc(line):
    # Для каждой буквы посчитаем, сколько раз она встречается в слове
    temp = [line.count(x) for x in line]
    return temp

n = int(input())
bumps = []
# Создаем список повторений букв в соответствующих словах
for _ in range(n):
    bumps.append(int(input()))
# Список для добавления букв
result = []
for i in range(n):
    line = input()
    count_liter = coloboc(line)
    # Если количество повторений буквы для данной кочки не равно тому, что задано
    # или такого количества повторений вообще не нашлось
    if count_liter.count(bumps[i]) != bumps[i] or bumps[i] not in count_liter:
        break
    # иначе добавляем нужную букву в список
    result.append(line[count_liter.index(bumps[i])])
#  Если не подошла не первая строка, а другая
if len(result) == len(bumps):
    print(''.join(result))
else:
    print('нечленораздельно')