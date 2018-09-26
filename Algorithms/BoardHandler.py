from random import randint
from IO import Parser


def createChessboard():
    # create a chessboard
    chessBoard = []
    size = 8
    for i in range(size):
        col = []
        for j in range(size):
            col.append(('.', "."))
        chessBoard.append(col)

    # read File's content
    chessPieces = Parser.readFile("Inputs/" + input("Enter filename: ") + ".txt")

    # randomize chess pieces' positions
    randomizer(chessBoard, chessPieces)

    return chessBoard


# clear board from chess pieces
def clearBoard(chessBoard):
    size = len(chessBoard)
    for i in range(size):
        for j in range(size):
            chessBoard[i][j] = ('.', ".")


# Fill board boxes with chess pieces
def fillBoard(chessBoard, row, col, pieceType, color):
    if color == "WHITE":
        if pieceType == "KNIGHT":
            chessBoard[row][col] = ('KNIGHT', "WHITE")
        elif pieceType == "BISHOP":
            chessBoard[row][col] = ('BISHOP', "WHITE")
        elif pieceType == "ROOK":
            chessBoard[row][col] = ('ROOK', "WHITE")
        elif pieceType == "QUEEN":
            chessBoard[row][col] = ('QUEEN', "WHITE")
    elif color == "BLACK":
        if pieceType == "KNIGHT":
            chessBoard[row][col] = ('KNIGHT', "BLACK")
        elif pieceType == "BISHOP":
            chessBoard[row][col] = ('BISHOP', "BLACK")
        elif pieceType == "ROOK":
            chessBoard[row][col] = ('ROOK', "BLACK")
        elif pieceType == "QUEEN":
            chessBoard[row][col] = ('QUEEN', "BLACK")


# Create list of pieces from chess board for randomizer
def createPiecesList(chessBoard):
    size = len(chessBoard)
    piecesList = []
    for row in range(size):
        for col in range(size):
            if chessBoard[row][col] != ('.', "."):
                piecesList.append(chessBoard[row][col])

    return piecesList


# Randomizes chess pieces' position
def randomizer(chessBoard, chessList):
    clearBoard(chessBoard)
    size = len(chessBoard)-1
    for piece in chessList:
        while True:
            row = randint(0, size)
            col = randint(0, size)

            if chessBoard[row][col] == ('.', "."):
                break

        fillBoard(chessBoard, row, col, piece[0], piece[1])