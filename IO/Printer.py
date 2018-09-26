from Algorithms import Checker


# Print chessboard to screen
def printChessBoard(chessBoard):
    size = len(chessBoard) # size = 8
    for row in range(size):
        for col in range(size):

            # no newline if final column has not reached
            if col < size-1:
                # print white
                if chessBoard[row][col][1] == "WHITE":
                    if chessBoard[row][col][0] == "QUEEN":
                        print('Q' + " ", end='')
                    elif chessBoard[row][col][0] == "ROOK":
                        print('R' + " ", end='')
                    elif chessBoard[row][col][0] == "KNIGHT":
                        print('K' + " ", end='')
                    elif chessBoard[row][col][0] == "BISHOP":
                        print('B' + " ", end='')
                    else:
                        print('.' + " ", end='')
                # print black
                else:
                    if chessBoard[row][col][0] == "QUEEN":
                        print('q' + " ", end='')
                    elif chessBoard[row][col][0] == "ROOK":
                        print('r' + " ", end='')
                    elif chessBoard[row][col][0] == "KNIGHT":
                        print('k' + " ", end='')
                    elif chessBoard[row][col][0] == "BISHOP":
                        print('b' + " ", end='')
                    else:
                        print('.' + " ", end='')

            # newline in print because final column is reached
            else:
                # print white
                if chessBoard[row][col][1] == "WHITE":
                    if chessBoard[row][col][0] == "QUEEN":
                        print('Q' + "\n")
                    elif chessBoard[row][col][0] == "ROOK":
                        print('R' + "\n",)
                    elif chessBoard[row][col][0] == "KNIGHT":
                        print('K' + "\n",)
                    elif chessBoard[row][col][0] == "BISHOP":
                        print('B' + "\n",)
                    else:
                        print('.' + "\n",)
                # print black
                else:
                    if chessBoard[row][col][0] == "QUEEN":
                        print('q' + "\n",)
                    elif chessBoard[row][col][0] == "ROOK":
                        print('r' + "\n",)
                    elif chessBoard[row][col][0] == "KNIGHT":
                        print('k' + "\n")
                    elif chessBoard[row][col][0] == "BISHOP":
                        print('b' + "\n")
                    else:
                        print('.' + "\n")


def printConflictAmount(chessBoard):
    total, queen, rook, bishop, knight = Checker.conflictCheckerA(chessBoard)
    print("Total conflict : " + str(total))
    print("Description:")
    print("  Queen  : " + str(queen))
    print("  Rook   : " + str(rook))
    print("  Bishop : " + str(bishop))
    print("  Knight : " + str(knight))
