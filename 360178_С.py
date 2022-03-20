a = int(input())
x = list(input())
z = 0
c = 0
for i in range(a):
    if x[i] == '.':
        z += 1
    else:
        c += z // 2
        z = 0
print(c + z // 2)
