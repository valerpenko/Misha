def dec2bin(a):
    l = []
    while a > 0:
        if a % 2 == 0:
            l.insert(0, 0)
            a = a // 2
        else:
            l.insert(0, 1)
            a = a // 2
    return l

def shift(l):
    d = l.pop(0)
    l.append(d)
    return l

def bin2dec(l):
    f = 0
    p = 0
    for i in range(len(l) - 1, -1, -1):
        f = f + l[i] * (2 ** p)
        p += 1
    return f

a = int(input())
l=dec2bin(a)
lr = list(l)
f = 0
max = 0
while True:
    l=shift(l)
    bin2dec()
    if f > max:
        max = f
    if not lr != l:
        break
print(max)
