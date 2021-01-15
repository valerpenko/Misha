    def FullSqare(a,b,c):
        if a*a + b*b == c:
            return True
        else:
            return False

    n = int(input())

    for i in range(n):
        bound = int(i**0.5)
        for a in range(bound+1):
            for b in range(a, bound+1):
                if FullSqare(a,b,i):
                    print(i,a,b)


