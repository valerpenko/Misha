'''Для любого целого k обозначим количество цифр в его десятичной
записи через Ц(k).Дано натуральное число n. Вычислить'''

n = int(input())
s = ''

while len(s) < n:
    s = s + input()

for i in range(1, len(s)):
    if s[i-1] < s[i]:
        print("Нет")
        exit()

print("Да")
