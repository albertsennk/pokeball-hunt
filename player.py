"""
Noah Albertsen
3/31/2017

Reused code from Project 2
"""

class Player(object):
    
    def __init__(self, mapSize):
        self.img = loadImage('oakSprite.png')
        self.pSize = 48
        self.xpos = mapSize/2 * self.pSize
        self.ypos = mapSize/2 * self.pSize
        self.mapSize = mapSize
        self.numLives = 3
        
    # displays the player character
    def display(self):
        image(self.img, self.xpos, self.ypos)
        
    # changes the x and y positions by the input values
    def move(self, xAmt, yAmt):
        self.xpos += xAmt
        self.ypos += yAmt
        
    # returns the center coordinate x value
    def getXCenter(self):
        return self.xpos + self.pSize/2
    
    # returns the center coordinate y value
    def getYCenter(self):
        return self.ypos + self.pSize/2
    
    # returns the x value of the top left corner
    def getX(self):
        return self.xpos
    
    # returns the y value of the top left corner
    def getY(self):
        return self.ypos
    
    # returns the size of the sides (in pixels) ie one side is pSize
    def getSize(self):
        return self.pSize
    
    # returns the tile at the player's current row and column
    def getTile(self, tileMap):
        t = tileMap.getTileAt(self.xpos//self.mapSize, self.ypos//self.mapSize)
        return t
    
    # returns the current column of the player
    def getC(self):
        return (self.xpos + self.pSize/2)//self.pSize
    
    # returns the current row of the player
    def getR(self):
        return (self.ypos + self.pSize/2)//self.pSize
    
    # returns the x value of the left edge
    def getLeft(self):
        return self.xpos
    
    # returns the x value of the right edge
    def getRight(self):
        return self.xpos + self.pSize
    
    #returns the y value of the top edge
    def getTop(self):
        return self.ypos
    
    # returns the y value of the bottom edge
    def getBottom(self):
        return self.ypos + self.pSize
    
    def getNumLives(self):
        return self.numLives
    
    def loseLife(self):
        self.numLives -= 1
        
    def setR(self, r):
        self.ypos = r * (self.pSize)
        
    def setC(self, c):
        self.xpos = c * (self.pSize)