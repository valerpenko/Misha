a = int(input())
b = int(input())
c = int(input())
d = int(input())
max = 0

if a > b:
    max = a
else:
    max = b

if a > b and a > c:
    max = a
elif b > a and b > c:
    max = b
else:
    max = c

if a > b and a > c and a > d:
    max = a
elif b > a and b > c and b > d:
    max = b
elif c > a and c > b and c > d:
    max = c
else:
    max = d

print(max)