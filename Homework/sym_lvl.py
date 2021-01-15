a = int(input())
a = str(a)
sym_lvl = 0

for i in range((len(a)+1)//2):
    if a[i] == a[len(a) - 1 - i]:
        sym_lvl += 1

print(sym_lvl)
