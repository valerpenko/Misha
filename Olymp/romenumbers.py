def rome_2_dec(a):
    romedigits={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    decres=0
    a=a[::-1]
    i=0
    curkeynum=0

    romekeys=romedigits.keys()   # "I"
    cur_digit=romedigits[curkeynum]
    while i<len(a):
        if a[i]==cur_digit:
            decres+=romedigits[cur_digit]
            i+=1
        else:
            curkeynum+=1
            cur_digit= romedigits.keys(curkeynum)
    return decres

def dec_2_rome(a):
    pass


# a = input()
# b = input()
#
# a = rome_2_dec(a)
# b = rome_2_dec(b)
#
# summ = a + b
# print(dec_2_rome(summ))

print(rome_2_dec("III"))