a = int(input())
x = list(input())
z = set(x)
c = []
for i in z:
    c.append([x.count(i),  i])
c.sort(reverse=True)
if c[0][0] > (a + 1) // 2:
    print('NO')
else:
    print('YES')
    while True:
        if c[0][0] == 0 and c[1][0] == 0:
            break
        if c[1][0] != 0:
            print(c[0][1], c[1][1], sep='', end='')
            c[0][0] -= 1
            c[1][0] -= 1
        else:
            print(c[0][1], end='')
            break
        c.sort(reverse=True)
