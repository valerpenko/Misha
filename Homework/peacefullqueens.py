def Peace(Q1,Q2):
    if Q1[0]==Q2[0]:
        return False
    if Q1[1]==Q2[1]:
        return False
    if Q1[0]-Q1[1]==Q2[0]-Q2[1]:
        return False
    #if Q1[0]-Q1[1]==Q2[0]-Q2[1]:  побочная диагональ
    #    return False
    return True

def SQ(n):
    if n==1:
        pass
    else:
        SQ(n-1)
        for attempt in range(1,9):
            for p in pos:
                  if Peace([n,attempt], [p,pos[p]]):
                      pos[n]=attempt
                      return pos
                  else:

pos=[0,0,0,0,0,0,0,0]
print(SQ(8))