x = input()
a = -1
b = len(x)
c = x.find('@')
for i in range(len(x)):
    if x[i] == '#' and i < c:
        a = i
    elif x[i] == '#' and i > c:
        b = i
        break
print(b - a - 1)

