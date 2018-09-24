from random import randint
from IO import Parser


def createChessboard():
    # create a chessboard
    chessBoard = []

    size = int(input("Enter board size : "))
    for i in range(size):
        col = []
        for j in range(size):
            col.append('.')
        chessBoard.append(col)

    # read File's content
    chessPieces = Parser.readFile("Inputs/" + input("Enter filename: ") + ".txt")

    # randomize chess pieces' positions and return list of all pieces location
    pieceLocation = posRandomizer(chessBoard, chessPieces)
    
    return chessBoard, pieceLocation


def fillBoard(chessBoard, row, col, pieceType):
    if pieceType == "KNIGHT":
        chessBoard[row][col] = 'K'
    elif pieceType == "BISHOP":
        chessBoard[row][col] = 'B'
    elif pieceType == "ROOK":
        chessBoard[row][col] = 'R'
    elif pieceType == "QUEEN":
        chessBoard[row][col] = 'Q'


def posRandomizer(chessBoard, chessPieces):
    pieceLocation = [] # location of all pieces
    for piece in chessPieces:
        pieceData = piece.split(" ") 
        # pieceData[0] = Color {WHITE, BLACK}
        # pieceData[1] = Type {KNIGHT, BISHOP, ROOK, QUEEN}
        # pieceData[2] = Amount {1, 2, 3, ..., 64}

        for i in range(int(pieceData[2])):
            # determine board's box (row and col) to be filled
            # also check if the box is filled
            
            while True:
                row = randint(0, len(chessBoard)-1)
                col = randint(0, len(chessBoard)-1)

                # break if the board has not filled
                if chessBoard[row][col] == '.':
                    break

            location = (row, col, pieceData[1])
            pieceLocation.append(location)
            fillBoard(chessBoard, row, col, pieceData[1])

    return pieceLocation



def conflictChecker(chessBoard):
    size = len(chessBoard)
    totalConflict = queenConflict = rookConflict = bishopConflict = knightConflict = 0

    for row in range(size):
        for col in range(size):
            if chessBoard[row][col] == 'R':  # ROOK
                rookConflict += checkHorizontalConflict(chessBoard, row, col)
                rookConflict += checkVerticalConflict(chessBoard, row, col)
                 
            elif chessBoard[row][col] == 'B':  # BISHOP
                bishopConflict += checkDiagonalConflict(chessBoard, row, col)
                    

            elif chessBoard[row][col] == 'Q':  # QUEEN
                queenConflict += checkHorizontalConflict(chessBoard, row, col)
                queenConflict += checkVerticalConflict(chessBoard, row, col)
                queenConflict += checkDiagonalConflict(chessBoard, row, col)

            elif chessBoard[row][col] == 'K':  # KNIGHT
                knightConflict += checkKnightConflict(chessBoard, row, col)

    totalConflict = rookConflict + queenConflict + bishopConflict + knightConflict

    return totalConflict, queenConflict, rookConflict, bishopConflict, knightConflict


def checkHorizontalConflict(chessBoard, row, col):
    count = 0
    # Check left
    for j in range(col-1, -1, -1):
        if chessBoard[row][j] != '.':
            count = count + 1
            break

    # Check right
    for j in range(col+1, len(chessBoard),):
        if chessBoard[row][j] != '.':
            count = count + 1
            break

    return count


def checkVerticalConflict(chessBoard, row, col):
    count = 0
    # check up
    for i in range(row-1, -1, -1):
        if chessBoard[i][col] != '.':
            count = count + 1
            break

    # check down
    for i in range(row+1, len(chessBoard)):
        if chessBoard[i][col] != '.':
            count = count + 1
            break

    return count


def checkDiagonalConflict(chessBoard, row, col):
    size = len(chessBoard)
    count = 0
      
    #check up right
    i = row - 1
    j = col + 1
    while ( i >= 0 ) and ( j < size ) :
        if (chessBoard[i][j]) != '.' :
            count = count + 1
            break
        i = i - 1
        j = j + 1

    #check up left
    i = row - 1
    j = col - 1
    while ( i >= 0 ) and ( j >= 0 ) :
        if (chessBoard[i][j]) != '.' :
            count = count + 1
            break
        i = i - 1
        j = j - 1

    #check down left
    i = row + 1
    j = col - 1
    while (i < size) and ( j >= 0 ) :
        if (chessBoard[i][j]) != '.' :
            count = count + 1
            break
        i = i + 1
        j = j - 1

    # check down right
    i = row + 1
    j = col + 1
    while ( i < 8 ) and ( j < 8 ) :
        if (chessBoard[i][j]) != '.' :
            count = count + 1
            break
        i = i + 1
        j = j + 1

    return count

def checkKnightConflict(chessBoard, row, col):
    deltas = [(-2, -1), (-2, +1), (+2, -1), (+2, +1), (-1, -2), (-1, +2), (+1, -2), (+1, +2)]
    size = len(chessBoard)
    count = 0

    for (i, j) in deltas:
        x = col + j
        y = row + i

        if x >= 0 and y >= 0 and x < size and y < size:
            if(chessBoard[y][x] != '.'):
                count = count + 1
                
    return count
