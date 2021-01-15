s = input()
s = s.lower()

l = s.split()
l_new = []

for el in l:
    if el[0] != 'м':
        l_new.append(el)

print(l_new)
