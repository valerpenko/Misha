l = map(int, input().split())
l = list(l)
n = int(input())

for i in range(n):
    p = l[len(l) - 1]
    l.remove(l[len(l) - 1])
    l.insert(0, p)

print(l)
