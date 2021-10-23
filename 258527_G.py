a = 5
b = 1
c = 5
d = 1
e = 5
x = 0
if a != 0 and b != 0 and c != 0:
    f = min(a, c, e)
    a -= f
    c -= f
    e -= f
    x += f
if a != 0 and b != 0 and c != 0:
    f = min(a, c, d)
    a -= f
    c -= f
    d -= f
    x += f
if a != 0 and b != 0 and c != 0:
    f = min(b, c, e)
    b -= f
    c -= f
    e -= f
    x += f
if a != 0 or b != 0 and d != 0 or e != 0:
    while True:
        if a != 0:
            if d != 0:
                a -= 1
                 -= 1
                e -= 1
                x += 1
print(a, b, c, d, e, '/', x)



