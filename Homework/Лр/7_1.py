def check1(name, letters):
    # буквы из letters можно использованть повторно
    # например, из "ан" можно составить "анна"
    for i in range(len(name)):
        if name[i] not in letters:
            return "НЕТ"
    return 'ДА'

def check2(name, letters):
    # буквы из letters нельзя использованть повторно
    # # например, из "ан" нельзя составить "анна"
    letters = list(letters)
    for el in name:
        if el not in letters:
            return "НЕТ"
        else:
            letters.remove(el)
    return "ДА"


name = input()
letters = input()

print(check1(name,letters))
print(check2(name,letters))