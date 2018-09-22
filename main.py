from IO import Parser
from IO import Printer
from Algorithms import BoardHandler

if __name__ == "__main__":
    chessBoard = BoardHandler.createChessboard()
    Printer.printChessBoard(chessBoard)
    Printer.printConflictAmount(chessBoard)


