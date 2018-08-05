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
    return data

def save2file(file, pname, data):
    fileout = ''
    with open(file, "a") as savefile:
        fileout = pname + ': ' + str(data) + '\n'
        savefile.write(fileout)
        savefile.close()
    return fileout

def readFromFile(file):
    fileout = ''
    with open(file, 'r') as readfile:
        fileout = readfile.read()
        readfile.close()
    return fileout
