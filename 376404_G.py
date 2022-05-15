a, b = map(int, input().split())
c = 0
v = 0
x = []
for i in range(a):
    x.append(list(input()))
for i in range(a):
    for j in range(b):
        if x[i][j] == '/' or x[i][j] == '\\':
            v += 0.5
            c = abs(c - 1)
        elif c == 1 and '.':
            v += 1
    c = 0
print(int(v))
