def printFile(filename):
    print("Reading file...")

    with open(filename) as infile:
        print(infile.readlines())
    infile.close()

def printChessBoard(chessBoard):
    size = len(chessBoard) # size = 8
    for row in range(size):
        for col in range(size):
            if col < size-1:
                print(chessBoard[row][col] + " ", end='')
            else:
                print(chessBoard[row][col] + "\n")

