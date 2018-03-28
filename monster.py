"""
Noah Albertsen, modifying examples from class
"""

# importing the random class
import random

# constants for the different chase states for the monster
WANDER = 0
CHASE = 1

# global constants to defifne the current direction of travel
MOVE_NONE = 0
MOVE_LEFT = 1
MOVE_RIGHT = 2
MOVE_UP = 3
MOVE_DOWN = 4

# a global constant for the minimum distance the player has to be from
# the moster for it to enter the CHASE state
CHASE_DISTANCE = 6

class Monster:
    def __init__(self, tileMap, player):
        self.row = 1
        self.col = 1
        
        self.state = WANDER
        
        self.possibleMoves = self.getPassableMoves(tileMap, self.row, self.col)
        
        self.direction = self.chooseWanderDir(self.possibleMoves)
        
        self.tileMap = tileMap
        
        self.img = loadImage("teamRocketSprite.png")
        
        self.size = 48
        
        self.chaseDist = 6
        
        self.player = player
        
    # given a row and column, returns a list of the possible passable
    # adjacent tiles, i.e. [MOVE_LEFT, MOVE_DOWN2]. returns an empty list 
    # if there are no valid moves
    def getPassableMoves(self, tileMap, row, col):
        # creating the empty list for the possible moves
        passableDirList = []
        
        # checking if up is good to go
        # print(tileMap.getTileAt(row, col))
        if (tileMap.getTileAt(row - 1, col) != -1 and 
                tileMap.getTileAt(row - 1, col).isPassable()):
            passableDirList.append(MOVE_UP)
        # checking if down is good to go
        if (tileMap.getTileAt(row + 1, col) != -1 and 
                tileMap.getTileAt(row + 1, col).isPassable()):
            passableDirList.append(MOVE_DOWN)
        # checking if left is good to go
        if (tileMap.getTileAt(row, col - 1) != -1 and 
                tileMap.getTileAt(row, col - 1).isPassable()):
            passableDirList.append(MOVE_LEFT)
        # checking if right is good to go
        if (tileMap.getTileAt(row, col + 1) != -1 and 
                tileMap.getTileAt(row, col + 1).isPassable()):
            passableDirList.append(MOVE_RIGHT)
            
        # returning the list of passable directions
        return passableDirList
    
    # Gets the coordinates that represent making a move in the given
    # direction, in which moveDir is one of the named constants.
    def getMoveRowCol(self, startRow, startCol, moveDir):
        if (moveDir == MOVE_RIGHT):
            moveTile = [startRow, startCol + 1]
        elif (moveDir == MOVE_LEFT):
            moveTile = [startRow, startCol - 1]
        elif (moveDir == MOVE_UP):
            moveTile = [startRow - 1, startCol]
        elif (moveDir == MOVE_DOWN):
            moveTile = [startRow + 1, startCol]
        else:
            moveTile = [startRow, startCol]
            
        return moveTile
        
    # displaying the monster, updating it based on its current coordinates
    def display(self):
        image(self.img, self.col * self.size, self.row * self.size)
        
    # returning the current row of the monster
    def getR(self):
        return self.row
    
    # returning the current column of the monster
    def getC(self):
        return self.col
    
    # set the monster's row
    def setR(self, r):
        self.row = r
        
    # set the monster's column
    def setC(self, c):
        self.col = c
    
    # randomly choosing from the given list of passable directions
    # we return MOVE_NONE if the list is empty
    def chooseWanderDir(self, dirList):
        
        if (len(dirList) > 0):
            index = random.randint(0, len(dirList) - 1)
            dir = dirList[index]
        else:
            dir = MOVE_NONE
        
        self.direction = dir
    
    # choosing the moster's best chase direction, based on the Manhattan
    # distance
    def chooseChaseDir(self, dirList, playerR, playerC):
        
        # set bestDir to MOVE_NONE, because the bestDir hasn't been
        # calculated yet
        bestDir = MOVE_NONE
        
        # we set bestDist to a large value, so that the first option checked 
        # will automatically be found to be closer
        bestDist = 9999999
        
        # making sure we check every direction in the list
        for move in dirList:
            if (move == MOVE_LEFT):
                tempDist = abs(self.row - playerR) + abs(self.col - 1 - playerC)
                # print("Temp Distance: " + str(tempDist) + ", direction: " + str(move))
                if (tempDist < bestDist):
                    bestDist = tempDist
                    bestDir = MOVE_LEFT
            elif (move == MOVE_RIGHT):
                tempDist = abs(self.row - playerR) + abs(self.col + 1 - playerC)
                # print("Temp Distance: " + str(tempDist) + ", direction: " + str(move))
                if (tempDist < bestDist):
                    bestDist = tempDist
                    bestDir = MOVE_RIGHT
            elif (move == MOVE_UP):
                tempDist = abs(self.row - 1 - playerR) + abs(self.col - playerC)
                # print("Temp Distance: " + str(tempDist) + ", direction: " + str(move))
                if (tempDist < bestDist):
                    bestDist = tempDist
                    bestDir = MOVE_UP
            elif (move == MOVE_DOWN):
                tempDist = abs(self.row + 1 - playerR) + abs(self.col - playerC)
                # print("Temp Distance: " + str(tempDist) + ", direction: " + str(move))
                if (tempDist < bestDist):
                    bestDist = tempDist
                    bestDir = MOVE_DOWN
        
        # returning the best direction to go
        # print("Best move to get to player: " + str(bestDir))
        self.direction = bestDir
    
    # choosing the monster move direction, based on its chase state
    def chooseDirection(self, playerR, playerC):
        if (self.state == CHASE):
            self.chooseChaseDir(self.passableMoves, self.row, self.col)
        else:
            self.chooseWanderDir(self.passableMoves)
        
    # given the player object, update the monster's state based on the pre-defined
    # chase distance/Manhattan distance to the player, and choose the direction
    # based on the current state
    def chooseState(self, player):
        # getting the player row and column
        playerR = player.getR()
        playerC = player.getC()
        
        # calculating the Manhattan distance between the monster and player
        distance = abs(self.row - playerR) + abs(self.col - playerC)
        
        # if the Manhattan distance is <= the chase distance, we set the state
        # to chase, otherwise we set it to wander and call chooseWanderDir to
        # randomly choose the direciton of travel
        if (distance <= self.chaseDist):
            self.state = CHASE
            self.chooseChaseDir(self.passableMoves, playerR, playerC)
            
        else:
            self.state = WANDER
        
    # the monster moves one tile at a time, based on the current passable moves,
    # its chase state, and the best possible direction.
    def move(self, playerR, playerC):
        
        # print("Row,Col before: " + str(self.row) + ", " + str(self.col))
        
        moveToCoords = self.getMoveRowCol(self.row, self.col, self.direction)
        
        row = moveToCoords[0]
        col = moveToCoords[1]
        
        # checking if moveTile is passable
        if (self.tileMap.getTileAt(row, col) != -1 and 
                self.tileMap.getTileAt(row, col).isPassable()):
            # updating the monster's location to the confirmend passable location
            # simplifies movement just by updating its row and column location, 
            # rather than by pixels
            self.row = row
            self.col = col
            
        else:
            # monster has hit a wall, so we must choose a new direction
            self.chooseDirection(playerR, playerC)
        
        # print("Row,Col after: " + str(self.row) + ", " + str(self.col))
            
        self.chooseState(self.player)
        self.passableMoves = self.getPassableMoves(self.tileMap, self.row, self.col)