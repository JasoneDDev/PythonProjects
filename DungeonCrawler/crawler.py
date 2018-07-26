import numpy as np
import time as t
import random as r
from playerClass import player

# things to add: except statements, break classes out into separate objects
# decorators? @ ... do high score.. save out to file and read in from file (high score is time based)
# add pillars vs rocks into dungeon which acts as a wall, cannot walk into that space


def intro():
    print('As the rain comes down you look around and see a small door in the side of the cliffside.' ,'\n',
          'You run over and quickly run in.')
    t.sleep(2)
    print("As you enter you realise it's pitch black inside but it's too late!", '\n')
    t.sleep(2)
    print('The door slams behind you and you hear it lock.', '\n')
    updatePosition(waitingForMove())


def updatePosition(dirMoved):
    direction = dirMoved

    def moveFeedback(cardinal, dir = 'ahead'):

        if dir is 'ahead':
            feedback = "You're now heading " + cardinal + ". As you clumsily move " + str(direction) + " you take in your new surroundings.\nAll you can see surrounding you is darkness.\n"
        elif dir is 'back':
            feedback = "You take a step back.\nYou're still facing " + cardinal + '\n'
        else:
            feedback = "You're now facing " + cardinal + '\n'
        return feedback
    try:

        if direction == 'ahead':
            if player_instance.direction == 0 and player_instance.pos[0] <= 7: # pointing south
                player_instance.pos[0] += 1
                print(moveFeedback('South'))
            elif player_instance.direction == 1 and player_instance.pos[1] >= 1: # pointing west
                player_instance.pos[1] -= 1
                print(moveFeedback('West'))
            elif player_instance.direction == 2 and player_instance.pos[0] >= 1: # pointing north
                player_instance.pos[0] -= 1
                print(moveFeedback('North'))
            elif player_instance.direction == 3 and player_instance.pos[1] <= 7: # pointing east
                player_instance.pos[1] += 1
                print(moveFeedback('East'))
            else :
                print("As you try and move forward you smack right into a wall.", '\n')

        elif direction == 'back':
            player_instance.pos[0] -= 1
            print(moveFeedback(str(directionList[player_instance.direction]), 'back'))

        elif direction == 'left':
            player_instance.direction -= 1
            if player_instance.direction <= -1:
                player_instance.direction = 3
            print(moveFeedback(str(directionList[player_instance.direction]), 'left'))
        elif direction == 'right':
            player_instance.direction +=1
            if player_instance.direction >= 4:
                player_instance.direction = 0
            print(moveFeedback(str(directionList[player_instance.direction]), 'right'))
        print( player_instance.pos, " ", player_instance.direction)

        # her we check if the players position is the same as an item and if so we tell them
        # and let them choose to interact with the item

        locatedItem = findItemInList(player_instance.pos, itemLocations)
        if locatedItem != '':
            print('we found a {0} '.format(locatedItem), player_instance.pos)
            if locatedItem == 'key':
                print('Now if you remember where the door is we can get out of this dismal place.\n')
                updatePosition(waitingForMove())


        else:
            updatePosition(waitingForMove())
    except ValueError as e:
        print('Hit an error: ' + str(e))


def findItemInList(pair, aList):  # checks for coordinate pair in list
    for i in range(1, len(aList)):
        if aList[i] == pair:
            return itemDefs[i][0]
        else:
            return ''




# key location is now randomized per session


itemLocations = [[0,4],[r.randrange(0,8),r.randrange(0,8)],[4,4],[6,6]]
itemDefs = [['exit', 1], ['key', 3], ['pillar', 2], ['pillar', 4]]
directionList = ['South', 'West', 'North', 'East']


def buildRoom(x, y, itemList):
    xAxis = x
    yAxis = y
    itemCount = -1
    room = np.zeros([y,x])

    for i in itemList:
        if itemCount == -1:
            player_instance.pos = i
            itemCount += 1
            continue
        itemCount += 1
        [item_row, item_column] = i
        room[item_row][item_column] = itemDefs[itemCount][1]

    np.asarray(room).reshape(8,8)
    return room


def waitingForMove():
    keyPress = ''
    while keyPress == '':
        keyPress = input('Choose a direction (ahead, back, left right): ')
    return keyPress


player_instance = player()
print(buildRoom(8, 8, itemLocations))
print(intro())





