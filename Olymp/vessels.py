MA=5
MB=3
N=1
VA=0
VB=0

def Fill(X):
    print(">"+X)
    if X=="A":
        VA=MA
    else:
        VB=MB

def Empty(X):
    print(">"+X)
    if X=="A":
        VA=0
    else:
        VB=0

def Swap(X,Y):
    print("X">"Y")
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


