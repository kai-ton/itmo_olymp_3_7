a = ['a', 'b', 'c', 'd', 'e',
     'f', 'g', 'h', 'i', 'j',
     'k', 'l', 'm', 'n', 'o',
     'p', 'q', 'r', 's', 't',
     'u', 'v', 'w', 'x', 'y', 'z']
b = 0
c = list(input())
for i in range(len(c)):
    if a[i] == c[i]:
        b += 1
    else:
        break
print(b)
