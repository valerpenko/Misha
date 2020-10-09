a = int(input())
cnt = 0
l = []

while a > cnt:
    l.append(int(input()))
    cnt += 1

for i in range(a-2):
    for j in range(a-i-1):
        if l[j] > l[j+1]:
            #l[j], l[j+1] = l[j+1], l[j]
            t=l[j]
            l[j]=l[j+1]
            l[j+1]=t

print(l)
