# check if a position is inside the board
def checkBoundary(i,j):
    return i >= 0 and j >= 0 and i < 8 and j < 8


# Check box
def checkBox(chessBoard, row, col, color):
    if chessBoard[row][col] != ('.', ".") and chessBoard[row][col][1] == color:
        return True
    else:
        return False


# Check horizontal conflict
def checkHorizontalConflict(chessBoard, row, col, color):
    # Check left
    for j in range(col-1, -1, -1):
        if checkBox(chessBoard, row, j, color):
            return True

    # Check right
    for j in range(col+1, len(chessBoard)):
        if checkBox(chessBoard, row, j, color):
            return True

    return False


# check vertical conflict
def checkVerticalConflict(chessBoard, row, col, color):
    # check up
    for i in range(row-1, -1, -1):
        if checkBox(chessBoard, i, col, color):
            return True

    # check down
    for i in range(row+1, len(chessBoard)):
        if checkBox(chessBoard, i, col, color):
            return True

    return False


# check both diagonal conflict
def checkDiagonalConflict(chessBoard, row, col, color):
    # a piece at (p, q) is on the same diagonal as a piece at (r, s) if abs(p - r) == abs (q - s)
    size = len(chessBoard)

    # check up left
    i = row-1
    for j in range(col-1, -1, -1):
        if checkBoundary(i, j) and checkBox(chessBoard, i, j, color):
            return True
        else:
            i -= 1

    # check Up right
    i = row-1
    for j in range(col+1, size):
        if checkBoundary(i, j) and checkBox(chessBoard, i, j, color):
            return True
        else:
            i -= 1

    # check down left
    i = row+1
    for j in range(col-1, -1, -1):
        if checkBoundary(i, j) and checkBox(chessBoard, i, j, color):
            return True
        else:
            i += 1

    # check down right
    i = row+1
    for j in range(col+1, size):
        if checkBoundary(i, j) and checkBox(chessBoard, i, j, color):
            return True
        else:
            i += 1

    # check up
    # counter = 0
    # for i in range(row-1, -1, -1):
    #     if counter == 2:
    #         break
    #
    #     for j in range(size):
    #         if counter == 2:
    #             break
    #
    #         if abs(row - i) == abs(col - j) and chessBoard[i][j] != ('.', "."):
    #             if chessBoard[i][j][1] == color:
    #                 return True
    #             else:
    #                 counter += 1
    #
    # # check down
    # counter = 0
    # for i in range(row+1, size):
    #     if counter == 2:
    #         break
    #
    #     for j in range(size):
    #         if counter == 2:
    #             break
    #
    #         if abs(row - i) == abs(col - j) and chessBoard[i][j] != ('.', "."):
    #             if chessBoard[i][j][1] == color:
    #                 return True
    #             else:
    #                 counter += 1

    return False


# check conflict for knight (L range)
def checkKnightConflict(chessBoard, row, col, color):
    deltas = [(-2, -1), (-2, +1), (+2, -1), (+2, +1), (-1, -2), (-1, +2), (+1, -2), (+1, +2)]

    for (i, j) in deltas:
        x = col + j
        y = row + i

        if checkBoundary(y, x):
            if checkBox(chessBoard, y, x, color):
                return True

    return False


# Conflict A checker (same color)
def conflictCheckerA(chessBoard):
    size = len(chessBoard)
    totalConflict = queenConflict = rookConflict = bishopConflict = knightConflict = 0

    for row in range(size):
        for col in range(size):
            if chessBoard[row][col] == ("ROOK", "WHITE"):  # ROOK
                horizontalConflict = checkHorizontalConflict(chessBoard, row, col, "WHITE")
                verticalConflict = checkVerticalConflict(chessBoard, row, col, "WHITE")
                if horizontalConflict or verticalConflict:
                    totalConflict += 1
                    rookConflict += 1

            elif chessBoard[row][col] == ("BISHOP", "WHITE"):  # BISHOP
                if checkDiagonalConflict(chessBoard, row, col, "WHITE"):
                    totalConflict += 1
                    bishopConflict += 1

            elif chessBoard[row][col] == ("QUEEN", "WHITE"):  # QUEEN
                horizontalConflict = checkHorizontalConflict(chessBoard, row, col, "WHITE")
                verticalConflict = checkVerticalConflict(chessBoard, row, col, "WHITE")
                diagonalConflict = checkDiagonalConflict(chessBoard, row, col, "WHITE")
                if horizontalConflict or verticalConflict or diagonalConflict:
                    totalConflict += 1
                    queenConflict += 1

            elif chessBoard[row][col] == ("KNIGHT", "WHITE"):  # KNIGHT
                if checkKnightConflict(chessBoard, row, col, "WHITE"):
                    totalConflict += 1
                    knightConflict += 1

            elif chessBoard[row][col] == ("ROOK", "BLACK"):  # ROOK
                horizontalConflict = checkHorizontalConflict(chessBoard, row, col, "BLACK")
                verticalConflict = checkVerticalConflict(chessBoard, row, col, "BLACK")
                if horizontalConflict or verticalConflict:
                    totalConflict += 1
                    rookConflict += 1

            elif chessBoard[row][col] == ("BISHOP", "BLACK"):  # BISHOP
                if checkDiagonalConflict(chessBoard, row, col, "BLACK"):
                    totalConflict += 1
                    bishopConflict += 1

            elif chessBoard[row][col] == ("QUEEN", "BLACK"):  # QUEEN
                horizontalConflict = checkHorizontalConflict(chessBoard, row, col, "BLACK")
                verticalConflict = checkVerticalConflict(chessBoard, row, col, "BLACK")
                diagonalConflict = checkDiagonalConflict(chessBoard, row, col, "BLACK")
                if horizontalConflict or verticalConflict or diagonalConflict:
                    totalConflict += 1
                    queenConflict += 1

            elif chessBoard[row][col] == ("KNIGHT", "BLACK"):  # KNIGHT
                if checkKnightConflict(chessBoard, row, col, "BLACK"):
                    totalConflict += 1
                    knightConflict += 1

    return totalConflict, queenConflict, rookConflict, bishopConflict, knightConflict

def conflictCheckerB(chessBoard):
    size = len(chessBoard)
    totalConflict = queenConflict = rookConflict = bishopConflict = knightConflict = 0
