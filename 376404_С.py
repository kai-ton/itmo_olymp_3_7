n_samokatov = 0
mesto = 0
l, d, n = map(int, input().split())
a = list(map(int, input().split())) + [l]
dokuda = 0
while True:
    for i in a:
        if mesto + d >= i:
            dokuda = i
    n_samokatov += 1
    if dokuda == mesto and mesto != l:
        print(-1)
        break
    mesto = dokuda
    if mesto == l:
        print(n_samokatov)
        break
