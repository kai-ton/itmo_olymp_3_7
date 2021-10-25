a = int(input())
x = list(map(int, input().split()))
c = 0
for i in range(a // 2):
    c += min(abs(x[i] - x[-i - 1]), 10 - abs(x[i] - x[-i - 1]))
print(c)
