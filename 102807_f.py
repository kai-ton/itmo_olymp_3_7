a = int(input())
c = set()
d = []
for i in range(a):
    b = set(input().split())
    d += b - c
    c = b
print(*d)
