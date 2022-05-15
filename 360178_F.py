a, b = map(int, input().split())
x = []
f = '.'
c = 0
z = []
for i in range(a):
    x += [input()]
for i in range(a):
    e = 0
    r = 0
    for j in range(b):
        if x[i][j] == '.' and e == 1:
            e = 0
            r += 1
        elif x[i][j] == '#':
            e = 1
    if e == 1:
        r += 1
    z.append(r)
    f = '.'
    for j in range(b):
        if x[i][j] == '.' and f == '#':
            f = '.'
            z.append(c)
            c = 0
        elif x[i][j] == '#':
            c += 1
            f = '#'
    if c > 0:
        z.append(c)
    print(*z)
    z = []
    c = 0
for i in range(b):
    e = 0
    r = 0
    for j in range(a):
        if x[j][i] == '.' and e == 1:
            e = 0
            r += 1
        elif x[j][i] == '#':
            e = 1
    if e == 1:
        r += 1
    z.append(r)
    f = '.'
    for j in range(a):
        if x[j][i] == '.' and f == '#':
            f = '.'
            z.append(c)
            c = 0
        elif x[j][i] == '#':
            c += 1
            f = '#'
    if c > 0:
        z.append(c)
    print(*z)
    z = []
    c = 0
