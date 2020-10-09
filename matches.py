import math

n = 4 #int(input())

#m = n - math.floor(math.sqrt(n))**2

x = math.sqrt(n)
x=math.floor(x)
x=x**2
m=n-x


k = n - m**2

matchesSqare = (2 * m) * (m + 1)
matchesOut = 0

if k <= m and k > 0:
    matchesOut = 2*k + 1
elif k > m and k > 0:
    matchesOut = 2*k + 2

matches = matchesSqare + matchesOut
print(matches)