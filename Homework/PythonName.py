name = input()
hardspel = input().split()
saveindex = map(int, input().split())
favletter = input()
snake_name = ''

for i in range(len(name)):
    if name[i] in hardspel and i not in saveindex:
        snake_name = snake_name + favletter
    else:
        snake_name = snake_name + name[i]

print(snake_name)
