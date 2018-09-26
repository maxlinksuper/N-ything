from IO import Parser
from IO import Printer
from Algorithms import BoardHandler
import os

header = "\
_________               .__    __________                   __               __\n\
\_   ___ \  ____   ____ |  |   \______   \_______  ____    |__| ____   _____/  |_\n\
/    \  \/ /  _ \ /  _ \|  |    |     ___/\_  __ \/  _ \   |  |/ __ \_/ ___\   __\\\n\
\     \___(  <_> |  <_> )  |__  |    |     |  | \(  <_> )  |  \  ___/\  \___|  |\n\
 \______  /\____/ \____/|____/  |____|     |__|   \____/\__|  |\___  >\___  >__|\n\
        \/                                             \______|    \/     \/      \n"


colors = {
    'blue': '\033[94m',
    'pink': '\033[95m',
    'green': '\033[92m',
}

menuItems =\
    ["Create a new Chess board",
     "Show the Chess board",
     "Solve with Hill-Climbing",
     "Solve with Simulated Annealing",
     "Solve with Genetic Algorithm",
     "Credit",
     "Exit"
    ]


def colorize(string, color):
    if not color in colors:
        return string

    return colors[color] + string + '\033[0m'


def credit():
    S =\
    """
    >> Created by:
    >>   Kevin Leonardo Limitius    13516049    ChelseaTV Documenter
    >>   Christian Kevin Saputra    13516073    Genetic Algorithm Pioneer
    >>   Tanor Abraham Reyuko       13516088    Simulated Annealing Expert
    >>   Ahmad Faishol Huda         13516094    Hill Climber
    >>   Shandy                     13516097    Main Menu Man, Board Lover, Conflict Searcher
    """
    print(S)


def mainMenu():
    chessBoard = []
    while True:
        if os.name == 'nt':  # Windows
            os.system('cls')
        elif os.name == 'posix':  # Linux
            os.system('clear')

        print(colorize(header, 'pink'))
        i = 1
        for item in menuItems:
            print("[" + str(i) + "] " + colorize(item, 'blue'))
            i += 1

        choice = int(input(">> "))

        try:
            if choice < 1:
                raise ValueError

            # Call the matching function
            if choice == 1:
                chessBoard = BoardHandler.createChessboard()
            if choice == 2:
                Printer.printChessBoard(chessBoard)
            if choice == 6:
                credit()
            if choice == 7:
                exit(0)
        except (ValueError, IndexError):
            pass

        while True:
            text = input("\n>> Press enter to continue.")
            if text == "":
                break
            else:
                print("\n>> You did not press enter.")

        print("\n\n")
