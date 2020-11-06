
def Fill(X,VA,VB,MA,MB):
    print(">"+X)
    if X=="A":
        VA=MA
    else:
        VB=MB
    return  VA,VB

def Empty(X,VA,VB):
    print(">"+X)
    if X=="A":
        VA=0
    else:
        VB=0
    return  VA,VB

def Swap(X,Y, VA, VB, MA, MB):
    print(X+">"+Y)
    if X=="A":
        if MB-VB>VA:
            VB=VB+VA
            VA=0
        else:
            VA=VA-(MB-VB)
            VB=MB
    else:
        if MA-VA>VB:
            VA=VA+VB
            VB=0
        else:
            VB=VB-(MA-VA)
            VA=MA
    return VA, VB

MA=5
MB=3
N=1
VA=0
VB=0
VA, VB =  Fill("A",VA,VB,MA,MB)
print(VA,VB)
VA,VB= Swap("A","B",VA, VB, MA, MB)
print(VA,VB)

while VA!=N and VB!=N:
    VA, VB = Fill("A", VA, VB, MA, MB)
    VA, VB = Swap("A", "B", VA, VB, MA, MB)
print(VA,VB)