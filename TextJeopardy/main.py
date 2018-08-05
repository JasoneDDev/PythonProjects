import time as t
from fileUtils import LoadData as lD
from wordBlock import WordBlockClass

# so things to code
# - load external file with "sayings" for saskatchewan
# - we want a "score" for every correct letter and vowel guessed
# - we want to save out a high score
# - for each saying the computer chooses 2 letters and 1 vowel.
# - the player must then guess another 2 letter and 1 vowel.
# - the player gets points for each letter and vowel they guess correct
# - the player can take as many turns as they like but they only have 3 strikes, either letter guesses or sentence
#   guesses then they are out
# - the player then gets a guess as to what the saying is.
# - want to do unit testing on this project
# - want to do profiling on this project afterwards as a clone so I can show the profiled and fixed versions
# - want to do a mock server side communication module.

def addLetters(picks): # need to add cap here so people can;t add all characters and cheat
    for i in picks:
        wbObject.searchAndSwap(wbObject.mainData[wbObject.onSentenceNum], wbObject.visualSentence, i)
        t.sleep(1)
    wbObject.guessedChars = ''.join((wbObject.guessedChars[::]) + (picks))

def letsPlay():
    firstpass = True
    playing = True

    while playing:
        if(firstpass):
            print("Welcome to SK Jeopardy!\n\nThere's many great saying in Saskatchewan, let's see if you know your stuff!")
            t.sleep(2)
            print("Here's how the game is played.\nThe computer will choose 1 vowel and 2 consonants, and we'll fill those in on the board.\n"
                  "Then you get to pick 2 more consonants and one more vowel.\nThen it's time to make a guess!")
            t.sleep(1)
            print("If you guess right you win, but if you guess wrong it's gonna cost you points and then you'll have to pick one more consonant OR vowel"
                  " then guess again.")
            t.sleep(1)
        else:
            print("Are you ready for the next sentence? Awesome, by now you know the rules so let's have a look at the sentence.")
            print(wbObject.showSIP())
            t.sleep(1)
        firstpass = False
        print("\nFirst let's get the computer to pick 4 consonants.")
        compPicks = ''.join(set(wbObject.randomChoice(wbObject.letters, 4)))
        print("The computer picked ", compPicks, ' as the consonants.\n')
        compVpick = ''.join(set(wbObject.randomChoice(wbObject.vowels, 2)))

        print("And for the vowels it picked: ", compVpick, '')
        print("\nLet's add those in and have a look.")
        addLetters(compPicks)
        addLetters(compVpick)

        print(wbObject.showSIP())
        print("\nWow, that looks better! Now it's your turn to pick some.\n")

        conPick = ''
        print('Previously picked letters : {}'.format(wbObject.guessedChars))
        while conPick == '':
            conPick = input("Please type in 2 consonants: ")
        vowPick = ''

        while vowPick == '':
            vowPick = input("Please type in 1 vowel: ")
        print("\nThanks! Let's add those in and see.")
        addLetters(conPick)
        addLetters(vowPick)

        t.sleep(1)

        print('\n', wbObject.showSIP(),'\n', 'Previously guessed characters: ', set(wbObject.guessedChars))
        playing2 = True

        while playing2 == True:
            # pick consonats/vowels
            userPick = input("Please pick another consonant or vowel: ")
            print("Great! Let's add that in and have a look.")
            addLetters(userPick)
            print(wbObject.showSIP())
            t.sleep(1)
            # guess yes
            guessq = input('Would you like to make a guess? (y/n): ')
            if guessq == 'y':
                guess = input('Please type in your guess, make sure to include all , . etc.: ')
                # make guess
                if guess.lower() == wbObject.mainData[wbObject.onSentenceNum].lower():
                    print('you win! ', wbObject.mainData[wbObject.onSentenceNum])

                    if(wbObject.onSentenceNum + 1 >= len(wbObject.mainData)):
                        print("That's it! you made it all the way to the end! Congrats!")
                        playing = False
                        playing2 = False
                        break
                    else:
                        wbObject.nextSentence()
                        playing2 = False
                    #is right? start new word
                else:
                    print("Whoops! That's incorrect, but don't worry you can keep playing.\n")
                    t.sleep(1)
                    #is wrong continue with loop
            else:
                print("No worries, let's add some more letters then.")
                pass
            #guess no: continue loop

wbObject = WordBlockClass(lD("data.txt"))
t.sleep(2)
print(wbObject.showSIP())
letsPlay()

# print(wbObject.mainData[wbObject.onSentenceNum])



