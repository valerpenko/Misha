import math
r=30.0
n=5.0
alfa=math.radians(180/n)
P=2*n*r*math.tan(alfa)
print(P)
print(2*math.pi*r)

P2 = n * math.sqrt(2*r**2*(1.0-math.cos(2.0*alfa)))

print(P2)
