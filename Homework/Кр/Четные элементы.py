l = map(int, input().split())
l = list(l)
res = []

for el in l:
    if el % 2 == 0:
        res.append(el)

print(res)
