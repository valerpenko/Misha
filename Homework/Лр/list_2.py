L = [-8, 8, 6.0, 5, 'строка', -3.1]
summ = 0

for el in L:
    if type(el) == int or type(el) == float:
        summ += el

print(summ)
