z = input()
x = str()
for i in range(len(z)):
    if z[i] in '*/-+':
        x += f' {z[i]} '
    else:
        x += z[i]
print(x)
