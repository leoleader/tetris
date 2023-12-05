import numpy as nm 
import time
  
# importing OpenCV 
# import cv2 
  
from PIL import ImageGrab, Image
import pytesseract

class Pieces:
    ORGL = 'Orange L Piece' 
    PURPLEL = 'Purple L Piece'
    GREENSTEP = 'Green Step Piece'
    REDSTEP = 'Red Step Piece'
    PINKT = 'Pink T Piece'
    LINE = 'CYAN Line Piece'
    SQUARE = 'Gold Square Piece'
    EMPTY = 'Empty Square'

class ScreenCap:

    ## images to be taken
    gameState = None 
    scoreImg = None
    nextPieceImg = None

    # values
    score = None
    nextPiece = None
    gameGrid = None


    ## setting up piece identification by RGB value
    ## note: line piece RGB value is not orange because its only one that has a 
    ## shape that doesnt use the pixel I chose for next piece
    colors = {}
    colors[(170, 104, 61, 255)] = Pieces.ORGL
    colors[(81,63,166,255)] = Pieces.PURPLEL
    colors[(142, 179, 73, 255)] = Pieces.GREENSTEP
    colors[(182 ,53 ,61 ,255)] = Pieces.REDSTEP
    colors[(164, 62, 154, 255)] = Pieces.PINKT
    colors[(92, 177, 135, 255)] = Pieces.LINE
    colors[(214, 192, 103, 255)] = Pieces.SQUARE
    colors[(2, 2, 2, 255)] = Pieces.EMPTY
    ## grabs images of gameState, nextPiece, and score
    ## resolution = 1980 x 1080
    def takeImage(self): 
        
        global score

        self.gameState = ImageGrab.grab(bbox = (595, 225, 845, 725)) 
        self.gameGrid = self.getGameGrid()


        ## this is a 100 x 350 image
        self.nextPieceImg = ImageGrab.grab(bbox =((875, 250, 975, 600))) 

        ## going to keep nextpiece simple for now and just look at first next piece
        ## just get pixel color then figure out the piece since each piece is its own color
        nextPieceColor = self.nextPieceImg.getpixel((55, 50))
        ## accounting for line being positioned differently than rest
        if (nextPieceColor[0] < 10) and (nextPieceColor[0] < 10) and (nextPieceColor[0] < 10):
            self.nextPiece = Pieces.LINE
        else:
            self.nextPiece = self.determinePiece(nextPieceColor)
        print("the next piece is: " + self.nextPiece)

        self.scoreImg = ImageGrab.grab(bbox =(875, 650, 975, 700)) 
        ## score is easy, using pytesseract to get the number from the image
        score = pytesseract.image_to_string(self.scoreImg, config='--psm 6')
        if '\n' in score:
            score = score[0:len(score)-1]
        self.score = str(score)
        print('the current score is: ' + self.score)

    ## from the given rgba value determines what the next piece is
    ## returns 
    def determinePiece(self, rgba):
        for color in self.colors:
            if (abs(rgba[0] - color[0]) < 20) and (abs(rgba[1] - color[1]) < 20) and (abs(rgba[2] - color[2]) < 20):
                return self.colors[color]
        return 'ERROR: idk'
    
    ## takes pixels from each square of the grid
    def getGameGrid(self):
        ## gameState imgSize is 250 x 500
        ## this version of tetris is 10 x 20 blocks so each block is about 25 pixels
        pixelMap = self.gameState.load()
        ## this representation of the game grid has 0,0 at the top left corner
        gameGrid = {}
        posx = 0
        posy = 0
        for height in range(12, 500, 25):
            for width in range(12, 250, 25):
                rgb = pixelMap[width,height]
                print(rgb)
                gameGrid[(posx, posy)] = rgb
                if posy + 1 == 10:
                    posx += 1
                    posy = 0
                else:
                    posy += 1
        self.gameState.show()
        for key in gameGrid:
            gameGrid[key] = self.determinePiece(gameGrid[key])
        return gameGrid
    
    ## creates a simple string representation of the game board in the terminal
    def printGameState(self):
        for x in range(20):
            row = ''
            for y in range(10):
                row += '| '
                if self.gameGrid[(x, y)] == Pieces.EMPTY:
                    row += '  '
                else:
                    row += 'X '
            row += '|'
            print(row)
            print('-------------------' * 2)

    
# testing 
sc = ScreenCap()
sc.takeImage()
sc.printGameState()


    ## reading the images

    ## gamestate is going to be hardest, going to need to map out a pixel from each square in the grid
    ## and then use the colors to reconstruct where all the pieces are




