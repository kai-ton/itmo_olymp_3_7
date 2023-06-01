a = int(input())
x = list(map(int, input().split()))
b = max(x)
c = sum(x) - b
print(c + min(c + 1, b))
