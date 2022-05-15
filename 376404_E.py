n = int(input())
a = list(map(int, input().split()))
s = list(map(int, input().split()))
d = 0
flag = 0
h = []
for i in range(n):
    for j in range(a[i], s[i] + 1):
        if j > d:
            d = j
            h.append(j)
            flag = 1
            break
    if flag == 0:
        print(-1)
        break
    flag = 0
else:
    print(*h)
