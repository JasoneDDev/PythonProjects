import numpy as np
import time as t
import random as r
# things to add: except statements, break classes out into separate objects
# decorators? @ ... do high score.. save out to file and read in from file (high score is time based)
# add pillars vs rocks into dungeon which acts as a wall
def intro():
    print('As the rain comes down you look around and see a small door in the side of the cliffside.' ,'\n',
          'You run over and quickly run in.')
    t.sleep(2)
    print("As you enter you realise it's pitch black inside but it's too late!", '\n')
    t.sleep(2)
    print('The door slams behind you and you hear it lock.', '\n')
    updatePosition(waitingForMove())

def updatePosition(dirMoved):

    try:
        direction = dirMoved

        if direction == 'ahead':
            if player_instance.direction == 0 and player_instance.pos[0] <= 7: # pointing south
                player_instance.pos[0] += 1
                print("You're now heading South", '\n')
                print('As you clumsily move ' + direction + ' you take in your new surroundings.')
            elif player_instance.direction == 1 and player_instance.pos[1] >= 1: # pointing west
                player_instance.pos[1] -= 1
                print("You're now heading West", '\n')
                print('As you clumsily move ' + direction + ' you take in your new surroundings.')
            elif player_instance.direction == 2 and player_instance.pos[0] >= 1: # pointing north
                player_instance.pos[0] -= 1
                print("You're now heading North", '\n')
                print('As you clumsily move ' + direction + ' you take in your new surroundings.')
            elif player_instance.direction == 3 and player_instance.pos[1] <= 7: # pointing east
                player_instance.pos[1] += 1
                print("You're now heading East", '\n')
                print('As you clumsily move ' + direction + ' you take in your new surroundings.')
            else :
                print("As you try and move forward you smack right into a wall.", '\n')

        elif direction == 'back':
            player_instance.pos[0] -= 1

        elif direction == 'left':
            player_instance.direction -= 1
            if player_instance.direction <= -1:
                player_instance.direction = 3
        elif direction == 'right':
            player_instance.direction +=1
            if player_instance.direction >= 4:
                player_instance.direction = 0
        print( player_instance.pos, " ", player_instance.direction)

        # her we check if the players position is the same as an item and if so we tell them and let them choose to interact with the item
        locatedItem = findItemInList(player_instance.pos, itemLocations)
        if locatedItem != '':
            print('we found a {0} '.format(locatedItem), player_instance.pos)
        else:
            updatePosition(waitingForMove())
    except ValueError as e:
        print('Hit an error: ' + e)

def findItemInList(pair, aList):# checks for coordinate pair in list
    for i in range(1, len(aList)):
        if aList[i] == pair:
            return itemDefs[i][0]
        else:
            return ''


class player:
    def __init__(self):
        self.pos = [] # coordinates in the grid
        self.direction = int() # north, south, east, west
        self.inventory = {}

    print('player created', '\n')

# key location is now randomized per session
itemLocations = [[0,4],[r.randrange(0,8),r.randrange(0,8)],[4,4],[6,6]]
itemDefs = [['exit', 1], ['key', 3], ['pillar', 2], ['pillar', 4]]

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





