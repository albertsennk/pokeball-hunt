"""
Noah Albertsen
3/31/2017

Reused code from Project 2, modified with the new tile types
"""

class Tile(object):
    global tileTypes
    # these variables are the paths for the tile images
    grass = "grassTile.png"
    wave = "waterTile.png"
    mountain = "boulder.png"
    sand = "grassTile.png"
    coin = "treasureTile.png"
    gold = "treasureTile.png"
    
    tileTypes = [grass, wave, mountain, sand, coin, gold]
    
    def __init__(self, type, r, c):
        # setting the image based on the type passed to it
        if (type == 'g'):
            self.img = loadImage(tileTypes[0])
            self.passable = True
            self.collectable = False
        elif (type == 'w'):
            self.img = loadImage(tileTypes[1])
            self.passable = False
            self.collectable = False
        elif (type == 'm'):
            self.img = loadImage(tileTypes[2])
            self.passable = False
            self.collectable = False
        elif (type == 's'):
            self.img = loadImage(tileTypes[3])
            self.passable = True
            self.collectable = False
        elif (type == 'c'):
            self.img = loadImage(tileTypes[4])
            self.passable = True
            self.collectable = True
        elif (type == 'e'):
            self.img = loadImage(tileTypes[5])
            self.passable = True
            self.collectable = True
        
        self.type = type
        self.tSize = 48
        self.r = r
        self.c = c
        
    # displays the tile at the appropriate row and column
    # c and r are multiplied by tSize to get correct pixel coordinates
    def display(self):
        image(self.img, self.c * self.tSize, self.r * self.tSize)
        
    # returns the pixel size of each tile (ie one edge is tSize pixels long)
    def getSize(self):
        return self.tSize
    
    # returns boolean, whether or not the tile is passable
    # ie a wave/mountain is not passable, but grass and sand are
    def isPassable(self):
        return self.passable
    
    # returns the row of the tile (y value)
    def getR(self):
        return self.r
    
    # returns the column of the tile (x value)
    def getC(self):
        return self.c
    
    # returns the x value of the right edge
    def getRight(self):
        return self.c * self.tSize + self.tSize
    
    # returns the x value of the left edge
    def getLeft(self):
        return self.c * self.tSize
    
    # returns the y value of the top edge
    def getTop(self):
        return self.r * self.tSize
    
    # returns the y value of the bottom edge
    def getBottom(self):
        return self.r * self.tSize + self.tSize
    
    # returns boolean, whether or not the tile is collectable
    # ie grass/sand are not collectable, but coin and gold are
    def isCollectable(self):
        return self.collectable
    
    # returns the original type if the tile does not have a collectable, but if it does,
    # returns the original type: grass for coins and sand for gold
    def getEmptyType(self):
        # these are already the empty types, so returns the original type
        if (self.type == 'm' or self.type == 'w' or self.type == 'g' or self.type == 's'):
            return self.type
        # for coins, the empty type is grass
        elif (self.type == 'c'):
            return 'g'
        # for the gold bars, the empty type is sand
        elif (self.type == 'e'):
            return 's'
    
    # to string method, used for testing purposes
    def __str__(self):
        str = "Tile type: {}\nRow: {!s} Col: {!s}".format(self.type, self.r, self.c)
        return str