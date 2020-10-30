a, b = map(int, input().split("/"))
r = -1

while r != 0:
    q = a // b
    print(q)
    r = a % b
    a = b
    b = r
