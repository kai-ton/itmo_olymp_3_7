x = int(input())
z = list(input())
b = 0
a = 0
for i in z:
    if i == '+':
        a += 1
        b += a
    elif i == '-' and a - 1 <= 0:
        a = 0
    else:
        a -= 1
        b += a
print(b)
