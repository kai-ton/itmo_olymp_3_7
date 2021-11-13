a = list(input()) + list('BB')
for i in range(len(a) - 2):
    if a[i] == 'B':
        continue
    if a[i + 1] == '-':
        a[i], a[i + 1] = '-', 'W'
    elif a[i + 2] == '-':
        a[i], a[i + 2] = '-', 'W'
    else:
        break
print(*a[:-2:], sep='')
