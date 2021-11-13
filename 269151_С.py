a = int(input())
x = input().split()
for i in range(a):
    if x[i] == 'TL':
        print('TL', i + 1)
        break
    if x[i] == 'WA':
        print('WA', i + 1)
        break
else:
    print('AC')
