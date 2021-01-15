def good_disposition(queens):
    return False

def Next_queens(queens):
    return None

queens = [0,1,2,3,4,5,6,7]
while True:
    if good_disposition(queens):
        print(queens)
        break
    else:
        queens = Next_queens(queens)


