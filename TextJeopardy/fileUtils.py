
def LoadData(dFile):
    data = []
    with open(dFile, "r") as dataFile:
        for line in dataFile:
            data += [line.rstrip()]
        dataFile.close()
    return data