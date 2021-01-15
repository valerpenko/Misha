l = map(int, input().split())
l = list(l)

p = l[len(l)-1]
l.remove(l[len(l)-1])
l.insert(0, p)

print(l)
