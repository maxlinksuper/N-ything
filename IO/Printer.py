from Algorithms import Checker
import os


def printDir(path):
    fileList = os.listdir(path)
    print(">> List of input files:")

    for name in fileList:
        print("  >> " + name)


# Print chessboard to screen
def printChessBoard(chessBoard):

    if not chessBoard:
        print("ChessBoard is empty! You have to create it first.")
        return

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

    printConflictAmount(chessBoard)


def printConflictAmount(chessBoard):
    totalA, queenA, rookA, bishopA, knightA = Checker.conflictChecker(chessBoard)
    # totalB, queenB, rookB, bishopB, knightB = Checker.conflictCheckerB(chessBoard)

    print("Total conflict A : " + str(totalA))
    print("Description:")
    print("  Queen  : " + str(queenA))
    print("  Rook   : " + str(rookA))
    print("  Bishop : " + str(bishopA))
    print("  Knight : " + str(knightA))
    # print("\n")
    # print("Total conflict B : " + str(totalB))
    # print("Description:")
    # print("  Queen  : " + str(queenB))
    # print("  Rook   : " + str(rookB))
    # print("  Bishop : " + str(bishopB))
    # print("  Knight : " + str(knightB))
