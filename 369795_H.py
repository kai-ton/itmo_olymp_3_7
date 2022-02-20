n = int(input())
q = 0
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(n - 1):
    if a[i] + a[i + 1] - b[i] > a[i + 1]:
        q += (a[i] + a[i + 1] - b[i])
        a[i], a[i + 1] = a[i] - (a[i] + a[i + 1] - b[i]) + a[i + 1], 0
    elif a[i] + a[i + 1] > b[i]:
        q += (a[i] + a[i + 1] - b[i])
        a[i + 1] -= (a[i] + a[i + 1] - b[i])
print(q)
