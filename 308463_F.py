a, b = list(map(int, input().split()))
x = sorted(list(map(int, input().split())), reverse=True)
z = sorted(list(map(int, input().split())), reverse=True)
for i in range(a - b):
    z.append(0)
c = 0
for i in range(a):
    if x[i] - z[i] > 0:
        c += x[i] - z[i]
print(c)
