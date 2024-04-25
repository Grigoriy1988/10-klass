s = input('Введите выражение:\n')
list_dig = []
lis_zn = []
p = 0
for i in range(len(s)):
    if not (s[i].isdigit()):
        list_dig.append(int(s[p:i]))
        p = i + 1
        lis_zn.append(s[i])

list_dig.append(int(s[p:]))

while '*' in lis_zn or '/' in lis_zn:
    pdiv = lis_zn.index('/') if '/' in lis_zn else len(lis_zn) + 100
    pmul = lis_zn.index('*') if '*' in lis_zn else len(lis_zn) + 100
    if pdiv < pmul:
        list_dig[pdiv] = list_dig[pdiv] / list_dig[pdiv+1]
        k = list_dig.pop(pdiv+1)
        k = lis_zn.pop(lis_zn.index('/'))
    else:
        list_dig[pmul] = list_dig[pmul] * list_dig[pmul + 1]
        k = list_dig.pop(pmul + 1)
        k = lis_zn.pop(lis_zn.index('*'))


for i in lis_zn:
    if i == '+':
        list_dig[0] = list_dig[0] + list_dig[1]
        k = list_dig.pop(1)
    else:
        list_dig[0] = list_dig[0] - list_dig[1]
        k = list_dig.pop(1)
print(list_dig)

#
# print(*lis_zn)
# print(*list_dig)
