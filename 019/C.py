rim = {'I': 1, 'V': 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
rim_set = {'I', 'V', "X", "L", "C", "D", "M"}


def R(dig):
    print(dig)
    prev = dig[-1]
    res = rim[prev]
    for cur in dig[-2::-1]:
        if rim[cur] >= rim[prev]:
            res += rim[cur]
        else:
            res -= rim[cur]
        prev = cur
    return res


def C(line1):
    line = line1
    for i in range(len(line)):
        if line[i] not in rim_set:
            # print(line[i])
            line = line[:i] + ' ' + line[i + 1:]
    list_rim = [x for x in line.split()]
    for i in list_rim:
        line1 = line1.replace(i, str(R(i)))
    print(line1)


word = input('Введите строку:')
C(word)
print(word)
