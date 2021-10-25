a = input()
b = input()
x = str()
for i in range(len(a) + len(b)):
    if i % 2 == 0:
        x += a[i // 2]
    else:
        x += b[i // 2]
print(x)
