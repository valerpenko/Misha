a = 10
b = 6
c = 5#int(input())
d = 0

while d != c:
    d = b - (a - d) % b
    if c % b == d:
        print()
    print(d)
    input()
