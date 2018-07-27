import numpy as np
import time as t
import random as r
from playerClass import player

# things to add: except statements... more except statements
# decorators? @ ... do high score.. save out to file and read in from file (high score is time based)
# add pillars vs rocks into dungeon which acts as a wall, cannot walk into that space
# key when found needs to be stored in a list/etc to be used when we return to the door.
# not adding the need to actually pick up the key, this will be automatic


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

    def moveFeedback(cardinal, dir = 'a'):

        if dir is 'a':
            feedback = "You're now heading " + cardinal + ". As you clumsily move ahead." +\
                       " you take in your new surroundings.\nAll you can see surrounding you is darkness.\n"
        elif dir is 'b':
            feedback = "You take a step back.\nYou're still facing " + cardinal + '\n'
        else:
            feedback = "You're now facing " + cardinal + '\n'
        return feedback
    try:
        if direction == 'p':
            print(dungeon)
            updatePosition(waitingForMove())

        if direction == 'a':
            if player_instance.direction == 0 and player_instance.pos[0] < 7: # pointing south
                player_instance.pos[0] += 1
                print(moveFeedback('South'))
            elif player_instance.direction == 1 and player_instance.pos[1] >= 1: # pointing west
                player_instance.pos[1] -= 1
                print(moveFeedback('West'))
            elif player_instance.direction == 2 and player_instance.pos[0] >= 1: # pointing north
                player_instance.pos[0] -= 1
                print(moveFeedback('North'))
            elif player_instance.direction == 3 and player_instance.pos[1] < 7: # pointing east
                player_instance.pos[1] += 1
                print(moveFeedback('East'))
            else :
                print("As you try and move forward you smack right into a wall.", '\n')

        elif direction == 'b':
            player_instance.pos[0] -= 1
            print(moveFeedback(str(directionList[player_instance.direction]), 'b'))

        elif direction == 'l':
            player_instance.direction -= 1
            if player_instance.direction <= -1:
                player_instance.direction = 3
            print(moveFeedback(str(directionList[player_instance.direction]), 'l'))
        elif direction == 'r':
            player_instance.direction +=1
            if player_instance.direction >= 4:
                player_instance.direction = 0
            print(moveFeedback(str(directionList[player_instance.direction]), 'r'))
        print( player_instance.pos, " ", player_instance.direction)

        # her we check if the players position is the same as an item and if so we tell them
        # and let them choose to interact with the item

        locatedItem = ''
        if player_instance.pos[0] >= 0 and player_instance.pos[0] < 8 and \
                player_instance.pos[1] >= 0 and player_instance.pos[1] < 8:
            locatedItem = findItemInList(player_instance.pos)
        if locatedItem != '':
            print('we found a {0} '.format(locatedItem), player_instance.pos)
            if locatedItem == 'key':
                player_instance.inventory[1] = locatedItem
                [item_row, item_column] = player_instance.pos
                dungeon[item_row][item_column] = 0
                print('Added {0} to your inventory'.format(locatedItem))
                print('Now if you remember where the door is we can get out of this dismal place.\n')
                updatePosition(waitingForMove())
            elif locatedItem == 'exit' and 'key' in player_instance.inventory.values():
                print('You found the door!\n'
                      'You quickly pull out the key from your pocket and slip it into the keyhole.\n'
                      'You feel a sigh of relief as the key turns and you hear a click. The door swings open and you '
                      'smell fresh air as you run out of the dungeon!\n'
                      'You made it!')
            elif locatedItem == 'exit':
                print("You found the door, but it seems it's locked. You must have to find something to open it, "
                      "like a key.\n")
                updatePosition(waitingForMove())


        else:
            updatePosition(waitingForMove())
    except ValueError as e:
        print('Hit an error: ' + str(e))


def findItemInList(pair):  # checks for coordinate pair in list

    objectFound = int(dungeon[pair[0]][pair[1]])
    if objectFound != 0:
        for i in range(0, len(itemDefs)):
            if itemDefs[i][1] == objectFound:
                return itemDefs[i][0]

    else:
        return ''

# key location is now randomized per session


itemLocations = [[0, 4], [r.randrange(0, 8), r.randrange(0, 8)]]
itemDefs = [['exit', 1], ['key', 3]]
directionList = ['South', 'West', 'North', 'East']


def buildRoom(x, y, itemList):
    xAxis = x
    yAxis = y
    itemCount = -1
    room = np.zeros([y, x])

    for i in itemList:
        if itemCount == -1:
            player_instance.pos = i
            [item_row, item_column] = i
            room[item_row][item_column] = itemDefs[0][1]
            itemCount += 1
            continue
        itemCount += 1
        [item_row, item_column] = i
        room[item_row][item_column] = itemDefs[itemCount][1]

    np.asarray(room).reshape(8,8)
    print(room)
    return room


def waitingForMove():  # takes first letter of the word typed to lowercase and passes it along.
    keyPress = ''
    while keyPress == '':
        keyPress = input('Choose a direction - ahead, back, left right: ')

    return keyPress[0].lower()


player_instance = player()
dungeon = buildRoom(8, 8, itemLocations)

print(intro())






