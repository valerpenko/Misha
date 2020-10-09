a = int(input())
n = int(input())
mask = 2**n
k = 0


l = []
while a > 0:
    if a % 2 == 0:
        l.insert(0, 0)
        a = a // 2
    else:
        l.insert(0, 1)
        a = a // 2

for i in range(0, len(l)):
    k = k * 10 + l[i]

if k & mask == 0:
    print("0")
else:
    print("1")