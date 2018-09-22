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

    # randomize chess pieces' positions
    posRandomizer(chessBoard, chessPieces)

    return chessBoard


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

            fillBoard(chessBoard, row, col, pieceData[1])


def conflictChecker(chessBoard):
    size = len(chessBoard)
    totalConflict = queenConflict = rookConflict = bishopConflict = knightConflict = 0

    for row in range(size):
        for col in range(size):
            if chessBoard[row][col] == 'R':  # ROOK
                horizontalConflict = checkHorizontalConflict(chessBoard, row, col)
                verticalConflict = checkVerticalConflict(chessBoard, row, col)
                if horizontalConflict or verticalConflict:
                    totalConflict += 1
                    rookConflict += 1

            elif chessBoard[row][col] == 'B':  # BISHOP
                if checkDiagonalConflict(chessBoard, row, col):
                    totalConflict += 1
                    bishopConflict += 1

            elif chessBoard[row][col] == 'Q':  # QUEEN
                horizontalConflict = checkHorizontalConflict(chessBoard, row, col)
                verticalConflict = checkVerticalConflict(chessBoard, row, col)
                diagonalConflict = checkDiagonalConflict(chessBoard, row, col)
                if horizontalConflict or verticalConflict or diagonalConflict:
                    totalConflict += 1
                    queenConflict += 1

            elif chessBoard[row][col] == 'K':  # KNIGHT
                if checkKnightConflict(chessBoard, row, col):
                    totalConflict += 1
                    knightConflict += 1

    return totalConflict, queenConflict, rookConflict, bishopConflict, knightConflict


def checkHorizontalConflict(chessBoard, row, col):
    # Check left
    for j in range(col-1, -1, -1):
        if chessBoard[row][j] != '.':
            return True

    # Check right
    for j in range(col+1, len(chessBoard),):
        if chessBoard[row][j] != '.':
            return True

    return False


def checkVerticalConflict(chessBoard, row, col):
    # check up
    for i in range(row-1, -1, -1):
        if chessBoard[i][col] != '.':
            return True

    # check down
    for i in range(row+1, len(chessBoard)):
        if chessBoard[i][col] != '.':
            return True

    return False


def checkDiagonalConflict(chessBoard, row, col):
    # a piece at (p, q) is on the same diagonal as a piece at (r, s) if abs(p - r) == abs (q - s)
    size = len(chessBoard)

    # check up
    for i in range(row-1, -1, -1):
        for j in range(size):
            if chessBoard[i][j] != '.':
                if abs(row - i) == abs(col - j):
                    return True

    # check down
    for i in range(row+1, size):
        for j in range(size):
            if chessBoard[i][j] != '.':
                if abs(row - i) == abs(col - j):
                    return True

    return False

def checkKnightConflict(chessBoard, row, col):
    deltas = [(-2, -1), (-2, +1), (+2, -1), (+2, +1), (-1, -2), (-1, +2), (+1, -2), (+1, +2)]
    size = len(chessBoard)

    for (i, j) in deltas:
        x = col + j
        y = row + i

        if x >= 0 and y >= 0 and x < size and y < size:
            if(chessBoard[y][x] != '.'):
                return True

    return False
