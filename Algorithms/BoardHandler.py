from random import randint
from IO import Parser

def createChessboard():
    # create a chessboard
    chessBoard = []

    size = int(input("Enter board size : "))
    for i in range(size):
        list = []
        for j in range(size):
            list.append('.')
        chessBoard.append(list)

    # read File's content
    chessPieces = Parser.readFile("Inputs/" + input("Enter filename: ") + ".txt")

    # randomize chess pieces' positions
    posRandomizer(chessBoard, chessPieces)

    return chessBoard

def fillBoard(chessBoard, row, col, type):
    if type == "KNIGHT":
        chessBoard[row][col] = 'K'
    elif type == "BISHOP":
        chessBoard[row][col] = 'B'
    elif type == "ROOK":
        chessBoard[row][col] = 'R'
    elif type == "QUEEN":
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
                col = randint(0,len(chessBoard)-1)

                # break if the board has not filled
                if(chessBoard[row][col] == '.'):
                    break

            fillBoard(chessBoard, row, col, pieceData[1])




