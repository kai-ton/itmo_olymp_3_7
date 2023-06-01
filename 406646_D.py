n, k = map(int, input().split())
a = list(map(int, input().split()))
print(sorted(a)[(k // 2 + 1) * -1])
