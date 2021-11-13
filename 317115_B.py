a = int(input())
b = 0
c = 0
while b <= a:
    c += 1
    b = c * (c - 1) // 2
print(c - 1)
