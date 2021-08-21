a, b, c = map(int, input().split())
if a == b:
    print('Draw!')
elif a > b:
    print('Erka', (c + a - b - 1) // (a - b))
else:
    print('Nyar', (c + b - a - 1) // (b - a))
