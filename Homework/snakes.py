num = int(input())
cnt = 0
l = []
s_revers = ''

while cnt < num:
    l.append(input())
    cnt += 1

for i in range(len(l)-1, -1, -1):
    s_revers = s_revers + l[i]

print(s_revers)
