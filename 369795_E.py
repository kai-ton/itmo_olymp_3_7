a = int(input())
b = int(input())
for i in range(39, 0, -1):
    y = b // 2**i
    if y >= 1 and a <= 2**i * y:
        print(2**i * y)
        break
else:
    print(a)
# 824633720832
# 1000000000000
# 549755813888
