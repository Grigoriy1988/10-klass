a = int(input())
b = int(input())
count = 0
for i in range(a):
    s = input()
    # sr = s[::-1]
    # print(sr)
    if s[0:b // 2] != s[b - 1:b // 2 - 1: -1]:
        print(s[0:b // 2], s[b - 1:b // 2 - 1: -1])
        count += 1
print(count)
