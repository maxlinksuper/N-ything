def readFile(filename):
    print("Reading file...\n")
    # Read per line & store to list
    with open(filename) as infile:
        content = infile.readlines()
    infile.close()

    # strip newline
    content = [x.strip() for x in content]
    return content

