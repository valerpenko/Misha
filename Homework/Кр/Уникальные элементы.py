l = map(int, input().split())
l = list(l)
el = ''
minimum = max(l) + 1
count = 0

for i in range(len(l)):
    for j in range(len(l)):
        if l[i] == l[j]:
            count += 1
    if count <= minimum:
        minimum = count
        el = el + ' ' + str(l[i]) + ','
    count = 0

if minimum == 1:
    print(el)
else:
    print('Уникальных елементов нет')
