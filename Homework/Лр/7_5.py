'''Для любого целого k обозначим количество цифр в его десятичной
записи через Ц(k).Дано натуральное число n. Вычислить'''

n = int(input())
sum = 0

for i in range(n):
    sum += len(str(i))/(i**2)

print(sum)
