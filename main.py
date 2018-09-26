from IO import Parser
from IO import Printer
from Algorithms import BoardHandler

if __name__ == "__main__":
    chessBoard = BoardHandler.createChessboard()
    Printer.printChessBoard(chessBoard)
    Printer.printConflictAmount(chessBoard)

    # tes random
    while True:
        print("\n\n")
        x = int(input("Enter 1 to random : "))
        if x == 1:
            chessList = BoardHandler.createPiecesList(chessBoard)
            BoardHandler.randomizer(chessBoard, chessList)
            Printer.printChessBoard(chessBoard)
            Printer.printConflictAmount(chessBoard)


