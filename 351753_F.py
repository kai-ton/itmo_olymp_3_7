#  «U» — вверх, «D» — вниз, «L» — влево, «R» — вправо.
a, b = map(int, input().split())
y = [list(input()) for j in range(a)]
# print(y)
z, x = 0, 0
for i in range(a):
    for j in range(b):
        # print('следующая ячейка')
        z = i
        x = j
        for k in range(a * b + 1):
            # print(z, x)
            if y[z][x] == 'U':
                z -= 1
            elif y[z][x] == 'D':
                z += 1
            elif y[z][x] == 'L':
                x -= 1
            else:
                x += 1
            if z == -1 or z == a or x == -1 or x == b:
                print(1, end='')
                break
        else:
            print(2, end='')
    print()
