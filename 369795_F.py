a = int(input())
x = sorted(list(map(int, input().split())))
b = [0]*a
b[0] = x[0]
for i in range(1, a):
    if i % 2 == 1:
        b[(i + 1) // 2] = x[i]
    else:
        b[-i // 2] = x[i]
print(*b)
