a = int(input())
x = list(map(int, input().split()))
b = 0
for i in range(1, a):
    b += abs(x.index(i) - x.index(i + 1))
print(b)
