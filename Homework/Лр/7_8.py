'''Вводится строка — предложение состоящие из нескольких слов.
Слова в строке разделяются пробелами. Причем между словами в
предложении может быть несколько пробелов. Определить и вывести
на экран количество слов в предложении.'''

sentense = input()
word_counter = 1
space_counter = 0
index = 0

while index < len(sentense):
    if space_counter == 0 and sentense[index] == ' ':
        word_counter += 1
        space_counter += 1
        if sentense[index + 1] == ' ':
            index += 1
    index += 1


print(word_counter)
