
#print(chessBoard)
def ShowBoard():
    for i in range(0,8):
        print(chessBoard[i])

#chessBoard[0][0]=1
def InsideDesk(moveChoice):
    return 8 > moveChoice[0]>= 0 and 0 <= moveChoice[1] < 8

def IsVacant(moveChoice):
    return chessBoard[moveChoice[0]][moveChoice[1]] == 0

def NextMove(location):
    result=[]
    for offset in offsetChoices:
        moveChoice=[location[0] +offset[0], location[1] +offset[1]]
        if  InsideDesk(moveChoice) and IsVacant(moveChoice):
            result.append(moveChoice)
    return result

#результат - список координат следующих возможных ходов,
#например [[2,2], [2,4], [..], [..], [..], [..], [..], [..]]

def NextMoveCount(location):
    return len(NextMove(location))
#результат - количество возможных ходов из

def HorseMove(nextMoves):
    global moveNum
    min=9
    minLoc=[9,9]
    for move in nextMoves:
        curMoves=NextMoveCount(move)
        if curMoves<min:
            min=curMoves    #Повторный вызов NextMoveCount!!!
            minLoc=move
    moveNum += 1
    chessBoard[horseLoc[0]][horseLoc[1]]=moveNum
    return  minLoc


#представление шахматной доски и ее показ
chessBoard=[[0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0]]
offsetChoices=[[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]]
horseLoc=[0,0]  # текущее положение коня
moveNum=0  #номер текущего шага

moves = NextMove(horseLoc)
while len(moves)>0:
    horseLoc = HorseMove(moves)
    moves = NextMove(horseLoc)
ShowBoard()
