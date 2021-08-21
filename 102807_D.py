a = input()
c = ''
for i in a:
    if 98 <= ord(i) <= 122:
        c += chr(ord(i) - 1)
    elif i == 'a':
        c += 'z'
    else:
        c += i
print(c)
