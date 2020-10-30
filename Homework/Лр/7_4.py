s = input()

t = s.replace('0','')

if len(t) % 2 == 0:
    s = s + '0'
else:
    s = s + '1'

print(s)
