x = int(input())
b = 0
s = 0
v = 0
fladgoc = 0
while True:
    if fladgoc == 1:
        break
    b += 1
    for i in range(4**b):
        if s + b <= x:
            s += b
            v += 1
        else:
            fladgoc = 1
            break

