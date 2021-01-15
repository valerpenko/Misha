l = map(int, input().split())
l = list(l)
el = ''
maximum = 0
count = 0

for i in range(len(l)):
    for j in range(len(l)):
        if l[i] == l[j]:
            count += 1
    if count > maximum:
        maximum = count
        el = l[i]
    count = 0
print(el)
