a = int(input())

l = []
while a > 0:
    if a % 2 == 0:
        l.insert(0, 0)
        a = a // 2
    else:
        l.insert(0, 1)
        a = a // 2

lr = list(l)
f = 0
max = 0
while True:
    f = 0
    d = l.pop(0)
    l.append(d)
    p = 0
    for i in range(len(l) - 1, -1, -1):
        f = f + l[i] * (2 ** p)
        p += 1
    if f > max:
        max = f
    if not lr != l:
        break

print(max)
