a = int(input())
x = sorted(list(map(int, input().split())))
print((a - 2) * x[-2] - sum(x[:-2:]))
