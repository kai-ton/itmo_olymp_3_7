a, b = map(int, input().split())
c = [1 for i in range(b)]
d = input()
for i in range(a - 1):
    e = input()
    for j in range(b):
        if d[j] != e[j]:
            c[j] = 0
    d = e
for i in range(b):
    if d[i] == '.':
        c[i] = 0
print(*c, sep='')
