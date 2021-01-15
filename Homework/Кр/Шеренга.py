l = map(int, input().split())
l = list(l)
n = int(input())

for i in range(1, len(l)):
    if l[i-1] >= n > l[i]:
        print(i+1)
        break
    if n > l[0]:
        print(1)
        break

