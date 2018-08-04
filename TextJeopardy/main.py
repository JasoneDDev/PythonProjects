import pandas as pd
import random as r
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


WordBlockClass(lD("data.txt"))

print()



