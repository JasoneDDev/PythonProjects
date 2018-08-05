
import random as r
# this word block is going to chop the input data one at a time into a couple arrays, one will be the full sentence
# array that we can test against the next will be a list of guessed letters and the 3rd will be a list of uniques
#  letters from the sentence and the 4rth will be the sentence with _ replacing the letters in the main sentence, same
# structure. as the letters are guessed we can replace the letters in the 4rth array that we will display as the
# progress" of the game as well we can show the guessed letters. a inbedded function can do the random computer
# letter/vowel guesses


class WordBlockClass:
    def __init__(self, data):
        self.mainData = data
        self.guessedChars = ''
        self.visualSentence = ''
        self.onSentenceNum = 0
        self.makeVisualSentence()
        self.letters = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z')
        self.vowels = ('a', 'e', 'i', 'o', 'u', 'y')
        self.uniqueChars = self.makeUnique(self.mainData[self.onSentenceNum])
        print("Word Block Data Created.")

    def makeVisualSentence(self):
        self.visualSentence = self.mainData[self.onSentenceNum]
        for i in range(0, len(self.visualSentence)):
            if self.visualSentence[i] != ' ' and self.visualSentence[i] != ',' and self.visualSentence[i] != '.':

                self.visualSentence = self.replaceChar(self.visualSentence, '~', i)

        # print(self.visualSentence, end='\n')
        # print(self.mainData[self.onSentenceNum])
        return self.visualSentence

    def makeUnique(self, charArray):
        return ''.join(set(charArray.lower()))


    def replaceChar(self, sentence, char, index):
        text = sentence[:index] + char + sentence[index + 1:]
        return text

    def showSIP(self):  # sentence in progress (sip)
        return self.visualSentence

    def randomChoice(self, selectionArray, numOfReturns = 1):
        return r.sample(selectionArray, numOfReturns)

    def searchAndSwap(self, searchArray, swapArray, letter):

        for i in range(0, len(searchArray)):
            if searchArray[i] == letter:
                swapArray = swapArray[:i] + letter + swapArray[i + 1:]
            elif searchArray[i] == letter.upper():
                swapArray = swapArray[:i] + letter.upper() + swapArray[i + 1:]

        self.visualSentence = swapArray
        return self.visualSentence
        # looks through main data sentence for specific letter, if found we place that letter in the visual sentence
        # at the same index

    def nextSentence(self):
        #resetting for the next sentence in queue
        self.guessedChars = ''
        self.onSentenceNum += 1
        self.makeVisualSentence()
        self.uniqueChars = self.makeUnique(self.mainData[self.onSentenceNum])
        return [self.visualSentence, self.uniqueChars, self.guessedChars]



