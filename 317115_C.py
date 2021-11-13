a = int(input())
b = int(input())
c = int(input())
print(min(a, b, c) * 3 + (a + b + c - min(a, b, c) - max(a, b, c)) * 2 + max(a, b, c))
