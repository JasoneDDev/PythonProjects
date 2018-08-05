import random as r

def LoadData(dFile):
    data = []
    with open(dFile, "r") as dataFile:
        for line in dataFile:
            data += [line.rstrip()]
        dataFile.close()
    return data

def LoadDataRandom(dFile, seed = 111): # the seed is for unit tests so we always have the same order, otherwise random
    data = []
    with open(dFile, "r") as dataFile:
        for line in dataFile:
            data += [line.rstrip()]
        dataFile.close()

    if seed != 111:
        r.seed(seed)
    r.shuffle(data)
    print(data)
    return data

