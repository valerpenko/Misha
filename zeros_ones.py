def DiscoverBit(number, bitPos):
    mask = 2**bitPos
    if number & mask == 0:
        return 0
    else:
        return 1
    
def DiscoverBit2(number, bitPos):        
    i=0
    l = [0]*32
    while number > 0:
        l[i]=number % 2
#         if number % 2 == 0:
#             l[i]=0
#         else:
#             l[i]=1
        number= number // 2
        i+=1
            
    return l[bitPos]
#     if l[bitPos] == 0:
#         return 0
#     else:
#         return 1

a = int(input())    

zeros=0
ones=0
for bitPos in range(32):
    if DiscoverBit(a,bitPos)==0:
        zeros+=1
    else:
        ones+=1
print(zeros, ones)    

zeros=0
ones=0
for bitPos in range(32):
    if DiscoverBit2(a,bitPos)==0:
        zeros+=1
    else:
        ones+=1
print(zeros, ones) 