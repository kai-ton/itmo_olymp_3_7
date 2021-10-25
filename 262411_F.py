a, b = list(map(int, input().split()))
x = list(map(int, input().split()))
z = max(x) - b * 5
c = []
for i in range(a):
    if x[i] >= z:
        c.append(1)
    else:
        c.append(0)
print(*c)
