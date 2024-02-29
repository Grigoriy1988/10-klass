def f(n):
    if n < 10:
        return 0
    return f(n // 10) + (n // 10 % 10) - (n % 10)


count = 0
for i in range(1, 100):
    if f(i) == 9:
        print(i)
        count += 1
# print(count)
# for i in range(1,10**6 +1):
#     dig = str(i)
#     if dig[0]=='9' and dig[-1] =='0':
#         count+=1

print(count)
print('111111111')
