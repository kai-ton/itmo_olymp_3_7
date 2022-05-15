a = input()
b = 0
c = 0
d = 0
for i in a:
    if i == '{':
        c = 0
        print(f'{" " * b}{"{"}')
        d = 0
        b += 2
    elif i == '}':
        if d == 1:
            print()
        if c == 1:
            print()
        d = 1
        c = 0
        b -= 2
        print(f'{" " * b}{"}"}', end='')
    elif i == ',':
        d = 0
        c = 0
        print(',')
    else:
        if d == 1:
            print()
        if c == 0:
            print(' ' * b, end='')
        d = 0
        c = 1
        print(i, end='')
