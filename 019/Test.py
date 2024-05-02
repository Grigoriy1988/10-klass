def E(word):
    temp = [word.count(x) for x in word]
    return temp


n = int(input())
buf = []
for _ in range(n):
    buf.append(int(input()))
result = []
for i in range(n):
    line = input()
    count_lit = E(line)
    if count_lit.count(buf[i]) != buf[i] or buf[i] not in count_lit:
        break
    result.append(line[count_lit.index(buf[i])])
if len(result) == len(buf):
    print(''.join(result))
else:
    print('нечленораздельно')



