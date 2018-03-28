"""
Noah Albertsen and Michael Faikes
4/28/2017
"""

add_library('sound')

import mapClass as m
import player as p
import tile as t
import monster

        
# a collision checker for the player with tiles
# LEFT = 0, UP = 1, RIGHT = 2, DOWN = 4
def didCollide(player, tileMap, direction):
    # player column
    pC = player.getC()
    # player row
    pR = player.getR()
    
    if (direction == 0):
        # checks for a collision with the left-most edge of the screen
        if (pC <= 0 and player.getLeft() <= 0):
            return True
        # checks for a collision with the tile to the left, if the player is not already
        # all the way in the left-most column
        elif (pC - 1 >= 0 and not tileMap.getTileAt(pR, pC - 1).isPassable() and 
                  player.getLeft() <= tileMap.getTileAt(pR, pC - 1).getRight()):
            return True
    elif (direction == 1):
        # checks for a collision with the top-most edge of the screen
        if (pR <= 0 and player.getTop() <= 0):
            return True
        # checks for a collision with the tile above, if the player is not already in
        # the top row
        elif (pR - 1 >= 0 and not tileMap.getTileAt(pR - 1, pC).isPassable() and 
                  player.getTop() <= tileMap.getTileAt(pR - 1, pC).getBottom()):
            return True
    elif (direction == 2):
        # checks for a collision with the right-most edge of the screen
        if (pC >= 9 and player.getRight() >= width):
            return True
        # checks for a collision with the tile to the right, if the player is not 
        # already in the right-most column
        elif (pC + 1 <= 9 and not tileMap.getTileAt(pR, pC + 1).isPassable() and
                  player.getRight() >= tileMap.getTileAt(pR, pC + 1).getLeft()):
            return True
    else:
        # checks for a collision with the bottom-most edge of the screen
        if (pR >= 9 and player.getBottom() >= height):
            return True
        # checks for a collision with the tile below, if the player is not already in 
        # the bottom row
        elif (pR + 1 >= 0 and not tileMap.getTileAt(pR + 1, pC).isPassable() and
              player.getBottom() >= tileMap.getTileAt(pR + 1, pC).getTop()):
            return True
        
# a collision checker for the monster and the player
# Noah Albertsen
def mpCollide(player, enemy):
    pC = player.getC()
    pR = player.getR()
    
    eC = enemy.getC()
    eR = enemy.getR()
    
    if (pC == eC and pR == eR):
        return True
    else:
        return False
        
# a collectables checker for the player with tiles
def collect(player, tileMap):
    global score, pokeList
    # player column
    pC = player.getC()
    # player row
    pR = player.getR()
    
    # if the tile has a collectable, replace it with its default state
    if (tileMap.getTileAt(pR, pC).isCollectable() and
            keyPressed and key == 'z'):
        emptyType = tileMap.getTileAt(pR, pC).getEmptyType()
        tileMap.setTileAt(pR, pC, emptyType)
        ### Michael Faikes ###   
        frameRate(5)
        ballAppears(pC,pR)
        score += 1
        pokeList[score-1] = "ball.png"
        sound = SoundFile(this, "ballPickUp.wav")
        sound.play()
        
### Michael Faikes ###
# draws the pokeball on the screen
def ballAppears(pC, pR):
    global ball
    i = 0
    while(i < 1):
        image(ball, (pC*48) + 7, pR*48)
        i+=1
    
def keyPressed():
    global player, tileMap
    frameRate(10)
    if (key == CODED):
        if (keyCode == LEFT):    
            if (didCollide(player, tileMap, 0)):
                player.move(0, 0)
            else:
                player.move(-48, 0)
        elif (keyCode == RIGHT):
            if (didCollide(player, tileMap, 2)):
                player.move(0, 0)
            else:
                player.move(48, 0)
        elif (keyCode == UP):
            if (didCollide(player, tileMap, 1)):
                player.move(0, 0)
            else:
                player.move(0, -48)
        elif (keyCode == DOWN):
            if (didCollide(player, tileMap, 3)):
                player.move(0, 0)
            else:
                player.move(0, 48)

def setup():
    global tileMap, player, enemy, splashScreen, gameStarted, score, ball, pokeList
    global winScreen, loseScreen, lives, moveCount
    size(480, 500)
    frameRate(10)
    theme = SoundFile(this, "game theme.mp3")
    theme.amp(0.25)
    theme.loop()
    
    # creating a map object (essentially the background, but the player can
    # interact with certain aspects of it (i.e. coins etc.))
    tileMap = m.Map('program2 map.txt', 10)
    
    # creating a player object
    player = p.Player(10)
    
    # creating a monster object
    enemy = monster.Monster(tileMap, player)
    # enemy.move(enemy.getR(), enemy.getC())
    
    ### Michael Faikes ###    
    splashScreen = loadImage("splashScreen.png")
    winScreen = loadImage("winScreen.png")
    loseScreen = loadImage("loseScreen.png")
    ball = loadImage("bigBall.png")
    gameStarted = False
    score = 0
    lives = 3
    pokeList = ["ballOutline.png","ballOutline.png","ballOutline.png","ballOutline.png",
                "ballOutline.png","ballOutline.png"]
    
    strokeWeight(0)
    fill(0)
    moveCount = 0;
    
    
# Michael Faikes
def draw():
    global tileMap, player, enemy, splashScreen, gameStarted, pokeList, loseScreen
    global lives, winScreen, moveCount
    
    # tileMap.display()
    # player.display()
    # collect(player, tileMap)
    # enemy.move(enemy.getR(), enemy.getC())
    # enemy.display()
    
    fill(0)
    rect(0, 480, width, 20)
    
    if ((keyPressed) and (key == ' ')):
        gameStarted = True
    
    count = 1
    
    if(gameStarted == True):
        tileMap.display()
        player.display()
        collect(player, tileMap)
        if (moveCount % 2 == 0):
            enemy.move(enemy.getR(), enemy.getC())
        enemy.display()
        fill(255)
        text("Score ", 10, 495)
        text("Lives "+str(lives) , 435, 495)
        fill(255)
        for i in pokeList:
            count += 1
            image(loadImage(i),12+(count*20),483)
        if(score == 6):
            image(winScreen,0,0)
            gameStarted == False
        if(lives <= 0):
            image(loseScreen,0,0)
            gameStarted == False
    elif(gameStarted == False):
        image(splashScreen,0,0)
    
    if mpCollide(player, enemy):
        sound = SoundFile(this, "pokemon.wav")
        sound.play()
        lives -= 1;
        enemy.setR(1)
        enemy.setC(1)
        player.setR(5)
        player.setC(5)
    
    moveCount += 1