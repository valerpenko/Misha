a = int(input())
b = int(input())
c = int(input())
d = int(input())

def max(x,y):
    if x > y:
        return x
    else:
        return y

print(max(max(a,b),max(c,d)))