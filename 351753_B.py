a = int(input())
b = int(input())
c = 0
while a != b:
    c += 1
    if a > b:
        a //= 2
    else:
        b //= 2
print(c)
