a = int(input())
b = 1
x = list(map(int, input().split()))
for i in range(len(x)):
    if x[i] % b == 0:
        b += 1
print(b - 1)
