x = int(input())
b = 0
c = 0
while x > 0:
    if c != 4:
        c += 1
        x -= 1
        b += 1
    else:
        c = 0
        x -= 10
        b += 1
print(b)
