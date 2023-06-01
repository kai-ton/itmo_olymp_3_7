a = list(input())
K = -1
A = -1
T = -1
p = 0
for i in range(len(a)):
    if a[i] == 'c':
        a[i] = 'C'
        p = i + 1
        break
for i in range(p, len(a)):
    if a[i] == 'a':
        a[i] = 'A'
        p = i + 1
        break
for i in range(p, len(a)):
    if a[i] == 't':
        a[i] = 'T'
        break
print(*a, sep='')
