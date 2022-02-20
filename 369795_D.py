x = input()
y = input()
b = int(x) / int(y)
for i in '0', '1', '2', '3', '4', '5', '6', '7', '8', '9':
    if i in x and i in y:
        x2 = x.replace(i, '')
        y2 = y.replace(i, '')
        if x2 != '' and y2 != '' and y2 != '0' and y2 != '00' and y2 != '000' and b == int(x2) / int(y2):
            print('Yes')
            break
else:
    print('No')
