k1 = 15
k2 = 17
k3 = 21
print('Задача №1')
count = 0
for i in range(15):
    for j in range(12):
        for k in range(10):
            s = i * k1 + j * k2 + k * k3
            if s == 185:
                print(i, j, k)
                count += 1
