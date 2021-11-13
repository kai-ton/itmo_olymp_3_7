n = int(input())
x = int(input())
a = [[i + j * n for i in range(1, n + 1)] for j in range(n)]
if x % 4 == 0:
    [print(*a[j]) for j in range(n)]
elif x % 4 == 1:
    for i in range(n):
        for j in range(n - 1, -1, -1):
            print(a[j][i], end=' ')
        print()
elif x % 4 == 2:
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            print(a[i][j], end=' ')
        print()
else:
    for i in range(n - 1, -1, -1):
        for j in range(n):
            print(a[j][i], end=' ')
        print()
# [print(a[i][j]) for i in range(n) for j in range(n - 1, -1, -1)]
