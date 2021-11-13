a = int(input())
y = list(map(int, input().split(':')))
x = 0
b = 9999999999999999999999999999999999999999999999999999999999999999999999999999
for i in range(a):
    x = list(map(int, input().split(':')))
    if (x[0] - y[0]) * 3600 + (x[1] - y[1]) * 60 + (x[2] - y[2]) < b:
        b = (x[0] - y[0]) * 3600 + (x[1] - y[1]) * 60 + (x[2] - y[2])
    y = x
print(b)
