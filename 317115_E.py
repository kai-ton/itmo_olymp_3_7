a, b = map(int, input().split())
x = sorted(list(map(int, input().split())), reverse=True)
c = 0
d = 0
if sum(x) >= b:
    for i in range(a):
        if c < b:
            c += x[i]
            d += 1
        else:
            break
    print(d)
else:
    print(-1)
