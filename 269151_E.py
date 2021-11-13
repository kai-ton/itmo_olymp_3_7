# 'abcdefghijklmnopqrstuvwxyz'
a = int(input())
x = sorted(input())
b = 1
for i in range(a - 1):
    if x[i] == x[i + 1]:
        b += 1
    else:
        print(f'({x[i] * b})', end='')
        b = 1
print(f'({x[-1] * b})', end='')
