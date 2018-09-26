# Check horizontal conflict
def checkHorizontalConflict(chessBoard, row, col):
    # Check left
    for j in range(col-1, -1, -1):
        if chessBoard[row][j] != ('.', "."):
            return True

    # Check right
    for j in range(col+1, len(chessBoard),):
        if chessBoard[row][j] != ('.', "."):
            return True

    return False


# check vertical conflict
def checkVerticalConflict(chessBoard, row, col):
    # check up
    for i in range(row-1, -1, -1):
        if chessBoard[i][col] != ('.', "."):
            return True

    # check down
    for i in range(row+1, len(chessBoard)):
        if chessBoard[i][col] != ('.', "."):
            return True

    return False


# check both diagonal conflict
def checkDiagonalConflict(chessBoard, row, col):
    # a piece at (p, q) is on the same diagonal as a piece at (r, s) if abs(p - r) == abs (q - s)
    size = len(chessBoard)

    # check up
    for i in range(row-1, -1, -1):
        for j in range(size):
            if chessBoard[i][j] != ('.', "."):
                if abs(row - i) == abs(col - j):
                    return True

    # check down
    for i in range(row+1, size):
        for j in range(size):
            if chessBoard[i][j] != ('.', "."):
                if abs(row - i) == abs(col - j):
                    return True

    return False


# check conflict for knight (L range)
def checkKnightConflict(chessBoard, row, col):
    deltas = [(-2, -1), (-2, +1), (+2, -1), (+2, +1), (-1, -2), (-1, +2), (+1, -2), (+1, +2)]
    size = len(chessBoard)

    for (i, j) in deltas:
        x = col + j
        y = row + i

        if x >= 0 and y >= 0 and x < size and y < size:
            if chessBoard[y][x] != ('.', "."):
                return True

    return False


# Conflict A checker (same color)
def conflictCheckerA(chessBoard):
    size = len(chessBoard)
    totalConflict = queenConflict = rookConflict = bishopConflict = knightConflict = 0

    for row in range(size):
        for col in range(size):
            if chessBoard[row][col] == ("ROOK", "WHITE"):  # ROOK
                horizontalConflict = checkHorizontalConflict(chessBoard, row, col)
                verticalConflict = checkVerticalConflict(chessBoard, row, col)
                if horizontalConflict or verticalConflict:
                    totalConflict += 1
                    rookConflict += 1

            elif chessBoard[row][col] == ("BISHOP", "WHITE"):  # BISHOP
                if checkDiagonalConflict(chessBoard, row, col):
                    totalConflict += 1
                    bishopConflict += 1

            elif chessBoard[row][col] == ("QUEEN", "WHITE"):  # QUEEN
                horizontalConflict = checkHorizontalConflict(chessBoard, row, col)
                verticalConflict = checkVerticalConflict(chessBoard, row, col)
                diagonalConflict = checkDiagonalConflict(chessBoard, row, col)
                if horizontalConflict or verticalConflict or diagonalConflict:
                    totalConflict += 1
                    queenConflict += 1

            elif chessBoard[row][col] == ("KNIGHT", "WHITE"):  # KNIGHT
                if checkKnightConflict(chessBoard, row, col):
                    totalConflict += 1
                    knightConflict += 1

    return totalConflict, queenConflict, rookConflict, bishopConflict, knightConflict
