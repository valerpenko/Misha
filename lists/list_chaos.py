ch_list=[1,6,"hjh", True, 4.6, False]
for el in ch_list:
    print(el)

for i in range(len(ch_list)):
    print(ch_list[i])

s=0
for el in ch_list:
    if type(el)==int or type(el)==float:
        s+=el
print(s)


