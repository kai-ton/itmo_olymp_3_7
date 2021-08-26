a, b = map(int, input().split())
f = list(list(input()) for i in range(a))
c = 0
d = 100000
e = 0
for y in range(a):
    for x in range(b):
        if f[y][x] == '#':
            continue
        for i in range(a):
            for j in range(b):
                if f[i][j] == '.':
                    continue
                if abs(y - i) + abs(x - j) < d:
                    d = abs(y - i) + abs(x - j)
        e = max(d, e)
        d = 10000
if e == 100000:
    print(-1)
else:
    print(e)
