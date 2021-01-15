def mirror(a):
    s = str(a)
    s = s[::-1]
    a = int(s)
    return a


a = int(input())
n = 0
while a != mirror(a):
    a = a + mirror(a)
    n += 1
    print(a)

print(n)
