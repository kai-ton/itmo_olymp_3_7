a = int(input())
b = list(map(int, input().split()))
for i in range(a, 0, -1):
    if b.count(i) == i:
        print(i)
        break
else:
    print(-1)
