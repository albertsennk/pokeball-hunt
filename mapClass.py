"""
Noah Albertsen
3/31/2017

Reused code from Project 2
"""

import tile

class Map(object):
    # as of right now, only square maps are accepted
    def __init__(self, path, mapSize):
        self.path = path
        self.mapSize = mapSize
        self.tSize = 48
        
        # creating a 2D array for the tile objects
        self.tileMap = [[0 for i in range(self.mapSize)] for j in range(self.mapSize)]
        
        # opening the map text file
        f = open(self.path, 'r')
        
        # processing through each line of the file
        for i in range(self.mapSize):
            newLine = f.readline()
            # creating a list of strings, using the default split
            lineList = newLine.split()
            
            # processing through the lineList, creating a new tile for each subset
            for j in range(self.mapSize):
                self.tileMap[i][j] = tile.Tile(lineList[j], i, j)
                
    # for each tile in the tileMap, call the tile's display method
    def display(self):
        for i in range(self.mapSize):
            for j in range(self.mapSize):
                self.tileMap[i][j].display()
                
    # returns the tile at a given row and column
    def getTileAt(self, r, c):
        # if the indices given are out of range, return -1
        if (r < 0 or r > self.mapSize or c < 0 or c > self.mapSize):
            return -1
        else:
            return self.tileMap[r][c]
        
    # sets the tile at the given position to the type listed
    # this really creates a new tile, and replaces the one at the given position
    def setTileAt(self, r, c, type):
        # if the indices given are out of range, do nothing
        if (r < 0 or r > self.mapSize or c < 0 or c > self.mapSize):
            True
        else:
            self.tileMap[r][c] = tile.Tile(type, r, c)
    
    def pixel2Row(self, x):
        return x // width
    
    def pixel2Col(self, y):
        return y // height