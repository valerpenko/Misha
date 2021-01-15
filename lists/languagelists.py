n=int(input())
pupillangages=[]
for i in range(n):
    m = int(input())
    onepupil=set()
    for j in range(m):
        l=input()
        onepupil.add(l)
    pupillangages.append(onepupil)
print(pupillangages)

common_lang=pupillangages[0]
all_lang=pupillangages[0]
for i in range(1,len(pupillangages)):
    common_lang = common_lang.intersection(pupillangages[i])
    all_lang = all_lang.union(pupillangages[i])
print(common_lang)
print(all_lang)





