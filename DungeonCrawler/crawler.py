import numpy as np
import time as t
import random as r
from playerClass import player
from dcIntro import bigText

# things to add: except statements, yields
# High score.. save out to file and read in from file (high score is time based)
# add pillars vs rocks into dungeon which acts as a wall, cannot walk into that space
# add map to use, we'll show current location and traveled areas


def intro():
    bigText('dungeon crawler')
    print('As the rain comes down you look around and see a small door in the side of the cliffside.\nYou run over and quickly run in.')
    t.sleep(2)
    print("As you enter you realise it's pitch black inside but it's too late!", '\n')
    t.sleep(2)
    print('The door slams behind you and you hear it lock.', '\n')
    updatePosition(waitingForMove())


def updatePosition(dirMoved):
    direction = dirMoved

    def moveFeedback(cardinal, dir = 'a'):

        # updating map

        player_instance.mapHistory = mapBuilder(player_instance.pos, player_instance.mapHistory)

        if dir is 'a':
            feedback = "You're now heading " + cardinal + ". As you clumsily move ahead." +\
                       " you take in your new surroundings.\nAll you can see surrounding you is darkness.\n"
        elif dir is 'b':
            feedback = "You take a step back.\nYou're still facing " + cardinal + '\n'
        else:
            feedback = "You're now facing " + cardinal + '\n'
        return feedback
    try:
        if direction == 'm':  # map
            print(player_instance.mapHistory)
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


        # her we check if the players position is the same as an item and if so we tell them
        # and let them choose to interact with the item

        locatedItem = ''
        if 0 <= player_instance.pos[0] < 8 and 0 <= player_instance.pos[1] < 8:
            locatedItem = findItemInList(player_instance.pos)
        if locatedItem != '':
            print('----------------- we found a {0} ----------------------------'.format(locatedItem))
            if locatedItem == 'key':
                bigText('do do do DOOOO!!!!!!!!!')
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
def randomKey():
    pair = [0, 4]
    while pair == [0, 4]:
        pair[0] = r.randrange(0, 8)
        pair[1] = r.randrange(0, 8)
    return pair

itemLocations = [[0, 4], randomKey()]
itemDefs = [['exit', 1], ['key', 3]]
directionList = ['South', 'West', 'North', 'East']



def mapBuilder(coords, map):
    xy = coords
    tempMap = map
    if tempMap == []:
        tempMap = np.zeros([8, 8], dtype=np.int)
        tempMap[:, :] = 1
        tempMap[0, 4] = 8
    elif coords != [0, 4]:
        tempMap[coords[0], coords[1]] = 0
    return tempMap



def buildRoom(x, y, itemList):
    xAxis = x
    yAxis = y
    itemCount = -1
    room = np.zeros([y, x], dtype = np.int)

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
    return room


def waitingForMove():  # takes first letter of the word typed to lowercase and passes it along.
    keyPress = ''
    while keyPress == '':
        print('(m)ap, (a)head, (b)ack, (l)eft (r)ight')
        keyPress = input('Please choose a direction: ')

    return keyPress[0].lower()


player_instance = player()
player_instance.mapHistory = mapBuilder(player_instance.pos, player_instance.mapHistory)
dungeon = buildRoom(8, 8, itemLocations)

    
print(intro())






