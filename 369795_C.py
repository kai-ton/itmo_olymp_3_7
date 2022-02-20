n = int(input())
m = int(input())
q = 'n', 0
x = 0
z = n * m / 3
c = 0
if n % 3 == 0 or m % 3 == 0:
    print(0)
else:
    if abs(c - z) > abs(z - n // 3 * m):
        c = abs(z - n // 3 * m)
        x = (n - n // 3) * m
        q = 'n', n // 3
    elif abs(c - z) > abs(z - (n // 3 + 1) * m):
        c = abs(z - n // 3 * m)
        x = (n - (n // 3 + 1)) * m
        q = 'n', n // 3 + 1
    elif abs(c - z) > abs(z - m // 3 * n):
        c = abs(z - m // 3 * n)
        x = (m - m // 3) * n
        q = 'm', n // 3
    elif abs(c - z) > abs(z - (m // 3 + 1) * n):
        c = abs(z - m // 3 * n)
        x = (m - (m // 3 + 1)) * n
        q = 'm', n // 3 + 1
if q[0] == 'n':
    n -= q[1]
else:
    n -= q[1]
if n % 2 == 0 or m % 2 == 0:
    print(x - (m * n // 2))
else:
    print(min(x - (m * (n - 1) // 2), x - ((m - 1) * n // 2)))
