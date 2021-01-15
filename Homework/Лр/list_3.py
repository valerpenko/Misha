x = input()
summ = 0

for el in x:
    i = int(el)
    if i % 2 == 1:
        summ += i**2

print(summ)
