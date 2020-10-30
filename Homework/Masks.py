mask = 'a*y' #input()
filename = 'andrey'#input()

# checking symbols before asterisc

index = 0
while index < len(filename) and mask[index] != '*':
    if mask[index] != filename[index] and mask[index] != '?':
        print("False")
        exit()
    index += 1

if index < len(filename) and mask[index] == '*':

    # checking symbols after asterisc

    index = len(mask) -1
    while index >= 0 and mask[index] != '*':
        if mask[index] != filename[index] and mask[index] != '?':
            print("False")
            exit()
        index -= 1

print('True')
