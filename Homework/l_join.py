l1 = [21, 25, 25, 33, 40, 49, 52, 63, 76]
l2 = [13, 19, 19, 25, 32, 36, 49, 50]
l = []

if l1[0] > l2[0]:
    t = l1
    l1 = l2
    l2 = t

while len(l1) > 0:
    while len(l1) > 0 and l1[0] <= l2[0]:
        l.append(l1.pop(0))

    if len(l1) == 0:
        break
    t = l1
    l1 = l2
    l2 = t

l.extend(l2)
print(l)

count = 1

for i in range(1, len(l)):
    if l[i-1] == l[i]:
        if count == 1:
            count +=1
            print(l[i])
        else:
            count += 1
    else:
        if count > 1:
            print(count)
        count = 1
