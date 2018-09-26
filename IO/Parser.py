def readFile(filename):
    print(">> Reading file...\n")
    # Read per line & store to list
    with open(filename) as infile:
        content = infile.readlines()
    infile.close()

    # strip newline
    chessPieces = [x.strip() for x in content]

    # transform contents to tuples
    piecesList = []
    for piece in chessPieces:
        pieceData = piece.split(" ")
        # pieceData[0] = Color {WHITE, BLACK}
        # pieceData[1] = Type {KNIGHT, BISHOP, ROOK, QUEEN}
        # pieceData[2] = Amount {1, 2, 3, ..., 64}

        tempTuple = (pieceData[1], pieceData[0])

        for i in range(int(pieceData[2])):
            piecesList.append(tempTuple)

    return piecesList
