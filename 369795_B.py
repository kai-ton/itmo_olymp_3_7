w = int(input())
z = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd',
     'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
a = input()
for i in range(26):
    if z[i] not in a:
        print('No')
        break
else:
    print('Yes')
