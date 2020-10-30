s = input()
# sep = ['']

s = s.lower()
s = s.replace(' ', '')
s = s.replace(',', '')
s = s.replace('.', '')
s = s.replace('!', '')
s = s.replace('?', '')

a = list(s)
b = list(s)

b.reverse()
if a == b:
    print("Палиндром")
else:
    print("Не палиндром")