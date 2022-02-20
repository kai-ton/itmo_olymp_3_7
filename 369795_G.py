n, m = map(int, input().split())
a = [0]*(n + 1)
a[1] = 1
for i in range(m):
    z, x = map(int, input().split())
    if a[z] == 1:
        a[x] = 1
    elif a[x] == 1:
        a[z] = 1
print(*a[1:], sep='')
