def freeDaysInCharge(a,b):
    count=0
    for y in range(a,b):
        count+=freeDaysInYear(y)
    return count

def freeDaysInYear(year):
    monthLen = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30] # 31]
    count=0
    dayNum=13
    if IsFriday(dayNum):
        count+=1
    for i in range (0,len(monthLen)):
        dayNum+=monthLen[i]
        print(dayNum)
        if IsFriday(dayNum):
            count += 1
    return count

def IsFriday(dayNum):
    return True

k=int(input())
days=0
for i in range(0,k):
    a,b = map(int, input().split())
    days+=freeDaysInCharge(a,b)
print(days)