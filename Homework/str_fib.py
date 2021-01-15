n = 6
s = 'ABA'
# Создаем строку фибоначи

index = 0
fibk_1 = 'B'
fibk_2 = 'A'

while index < n:
    fibk = fibk_1 + fibk_2
    fibk_2 = fibk_1
    fibk_1 = fibk
    index += 1

print(fibk)

# Ищем кол во вхождений S в стороку фибоначи

k = 0
p = fibk.find(s)
while p != -1:
    p = fibk.find(s,p+1)
    k += 1
print(k)