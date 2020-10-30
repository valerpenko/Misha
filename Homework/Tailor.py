import math
Eps, angle = map(float,input().split())
x = math.pi * angle / 180
a = x
k = 2
summ = x

while abs(a)>Eps:
    a = -(a*(x**2/(k*(k+1))))
    k += 2
    summ += a

print(summ)
print(math.sin(x))

a = 1
k = 1
summ = a

while abs(a)>Eps:
    a = -(a*(x**2/(k*(k+1))))
    k += 2
    summ += a

print(summ)
print(math.cos(x))