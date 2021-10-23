a = int(input())
b = list(map(int, input().split()))
c = 0
for i in range(a-1, 0, -1):
    if b[i] < b[i-1]:
        c += b[i-1] - b[i]
        b[i-1] -= b[i-1] - b[i]
print(c)
