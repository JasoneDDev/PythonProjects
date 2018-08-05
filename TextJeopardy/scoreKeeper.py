import fileUtils as utils

# this file lets us add/subract/get and set the score.


class ScoreKeeper:
    def __init__(self):
        self.userScore = 0
        self.filename = 'highScore.txt'

    def add2score(self, scoreint):
        self.userScore += scoreint
        # print(self.userScore)

    def subFromScore(self, scoreint):
        self.userScore -= scoreint
        # print(self.userScore)

    def saveScore2File(self, pname):
        utils.save2file(self.filename, pname, self.userScore)

    def getFromFile(self):
        fileText = utils.readFromFile(self.filename)
        return fileText

    def echoScore(self):
        # print(self.userScore)
        return self.userScore
