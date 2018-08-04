# this word block is going to chop the input data one at a time into a couple arrays, one will be the full sentence
# array that we can test against the next will be a list of guessed letters and the 3rd will be a list of uniques
#  letters from the sentence and the 4rth will be the sentence with _ replacing the letters in the main sentence, same
# structure. as the letters are guessed we can replace the letters in the 4rth array that we will display as the
# progress" of the game as well we can show the guessed letters. a inbedded function can do the random computer
# letter/vowel guesses


class WordBlockClass:
    def __init__(self, data):
        self.mainData = data
        self.guessedChars = []
        self.uniqueChars = []
        self.visualSentence = ''
        self.onSentenceNum = 0
        self.makeVisualSentence()
        print("Word Block Data Created.")

    def makeVisualSentence(self):
        self.visualSentence = self.mainData[self.onSentenceNum]
        for i in range(0, len(self.visualSentence)):
            if self.visualSentence[i] != ' ' and self.visualSentence[i] != ',' and self.visualSentence[i] != '.':

                self.visualSentence = self.replaceChar(self.visualSentence, '~', i)

        print(self.visualSentence, end='\n')
        print(self.mainData[self.onSentenceNum])

    def replaceChar(self, sentence, char, index):
        text = sentence[:index] + char + sentence[index + 1:]
        return text
