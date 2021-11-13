a = int(input())
x = sorted(list(map(int, input().split())))
b = 0
for i in range(0, a, 2):
    b += abs(x[i] - x[i + 1])
print(b)
