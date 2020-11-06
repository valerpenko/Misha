def Shift(binList):
    d=binList.pop(0)
    binList.append(d)
binList=[5,3,7,9]
Shift(binList)
print(binList)


binList=[5,3,7,9]
for i in range(0,len(binList)):
    Shift(binList)
    print(binList)
    

binList=[5,3,7,9]
reserv=binList
do
    Shift(binList)
    print(binList)
while reserv!=binList:


