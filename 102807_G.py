'''
Берем самые высокие места и слева и справа от них добавляем камней,
чтобы стала ступенька в один камень. На следующей иттерации уже берем места на 1 камень ниже.
И делаем то же самое. И т.д.
На берег камней не добавляем. И в конце проверяем нет ли перепада >1 у берегов с соседями.
'''

z, a, b = map(int, input().split())
x = [a] + list(map(int, input().split())) + [b]
cnt = 0
for j in range(max(x), 0, -1):
    for i in range(z + 2):
        if x[i] == j:
            if i > 1 and x[i - 1] < x[i]:
                cnt += x[i] - x[i - 1] - 1
                x[i - 1] = x[i] - 1
            if i < z and x[i + 1] < x[i]:
                cnt += x[i] - x[i + 1] - 1
                x[i + 1] = x[i] - 1
if x[1] - x[0] > 1 or x[z] - x[z + 1] > 1:
    print(-1)
else:
    print(cnt)
