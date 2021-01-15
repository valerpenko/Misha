count = 0
summ = 0
maximum = -1
s = input()

for el in s:
    if el.isdigit():
        el = int(el)
        print(el)
        count += 1
        summ += el
        if el > maximum:
            maximum = el

print('Количество', count)
print('Сумма', summ)
if maximum == -1:
    print('В строке цифр нет')
else:
    print('Максимальная цифра', maximum)