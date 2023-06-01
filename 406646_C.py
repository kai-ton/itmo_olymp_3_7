x = int(input())
a = list(input())
b = set()
for i in range(x):
    if a[i] in b:
        b.remove(a[i])
    else:
        b.add(a[i])
print(len(b))
print(*b, sep='')
