def reduction(s):
    index = 1
    cnt = 1
    res = ""
    while index < len(s):
        if s[index - 1] == s[index]:
            cnt += 1
        else:
            res = res + s[index-1] + str(cnt)
            cnt = 1
        index += 1
    res = res + s[index-1] + str(cnt)

    return res

def dereduction(s):
    index = 1
    decryp = ""
    while index < len(s):
        if (s[index-1]).isdigit():
            decryp = decryp + (s[index - 3] * (int(s[index-2])*10 + int(s[index-1])))
            index += 1
        else:
            decryp = decryp + s[index - 1]*int(s[index])
            index += 2
    return decryp


a = reduction(input())
print(a)
dereduction(a)
print(dereduction(a))