a = int(input())
x = sorted(list(map(int, input().split())))
c = 0
d = 0
for i in range(a):
    for j in range(a):
        if i <= x[j]:
            x[j] = -1
            d += 1
            break
    else:
        break
print(d)
