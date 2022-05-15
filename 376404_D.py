a = int(input())
b = list(map(int, input().split()))
c = int(input())
d = list(map(int, input().split()))
e = int(input())
f = list(map(int, input().split()))
q = 0
# print(f)
while len(f) != 0:
    x = 0
    if len(set(d) & set(f)) > 0 and max(set(d) & set(f)) >= 1:
        for i in set(d) & set(f):
            x += b[i - 1]
        if c < x:
            for i in set(d) & set(f):
                f.pop(f.index(i))
                # print(f)
            q += c
            # print(1, q)
        else:
            for i in set(d) & set(f):
                f.pop(f.index(i))
                # print(f)
                q += b[i - 1]
                # print(2, q)
    else:
        for i in f:
            q += b[i - 1]
            # print(3, q)
            f.pop(f.index(i))
            # print(f)
print(q)
