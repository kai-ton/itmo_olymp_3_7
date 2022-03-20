n = int(input())
m = int(input())
n, m = min(n, m), max(n, m)
k = int(input())

for j in range(k):
    x = 0
    for i in range(j + 1, m + n, k):
        x += min(n + m - i, i, n)
    print(x, end=' ')
