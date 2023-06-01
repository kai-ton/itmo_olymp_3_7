n = int(input())
k = min(n, int(input()))
x = []
for i in range(1, n + 1):
    x.append([2, i])
exe = (n * 2 + k - 1) // k
s = n * 2
print(exe)
for i in range(exe):
    print(min(s, k), end=' ')
    for j in range(min(s, k)):
        x[j][0] -= 1
        print(x[j][1], end=' ')
    s -= k
    print()
    x.sort(reverse=True)
