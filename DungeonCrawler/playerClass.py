class player:
    def __init__(self):
        self.pos = [] # coordinates in the grid
        self.direction = int() # north, south, east, west
        self.inventory = {}
        self.mapHistory = []

    # print('player created', '\n')