from PIL import ImageGrab
import pytesseract
from pieces import Pieces


## screencap on initialization shouldn't really do anything
## should have takeImage method which returns gameState, score, nextPiece
## so should move all other methods/logic to controller class
class ScreenCap:

    ## images to be taken
    gameStateImg = None 
    scoreImg = None
    nextPieceImg = None

    ## setting up piece identification by RGB value
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
    ## then uses helper methods / libraries to get data from images
    ## returns an array of [gameGrid: [], nextPiece: Piece, score: int]
    def takeImage(self): 

        self.gameStateImg = ImageGrab.grab(bbox = (595, 225, 845, 725)) 
        gameGrid = self.getGameGrid()

        ## this is a 100 x 350 image
        self.nextPieceImg = ImageGrab.grab(bbox =((875, 250, 975, 600))) 

        ## going to keep nextpiece simple for now and just look at first next piece
        ## just get pixel color then figure out the piece since each piece is its own color
        nextPieceColor = self.nextPieceImg.getpixel((55, 50))
        ## accounting for line being positioned differently than rest
        if (nextPieceColor[0] < 10) and (nextPieceColor[0] < 10) and (nextPieceColor[0] < 10):
            nextPiece = Pieces.LINE
        else:
            nextPiece = self.determinePiece(nextPieceColor)
        print("the next piece is: " + nextPiece)

        self.scoreImg = ImageGrab.grab(bbox =(875, 650, 975, 700)) 
        ## score is easy, using pytesseract to read the number from the image
        score = pytesseract.image_to_string(self.scoreImg, config='--psm 6')
        if '\n' in score:
            score = score[0:len(score)-1]
        print('the current score is: ' + str(score))
        return [gameGrid, nextPiece, score]

    ## from the given rgba value determines what the next piece is
    def determinePiece(self, rgba):
        for color in self.colors:
            if (abs(rgba[0] - color[0]) < 20) and (abs(rgba[1] - color[1]) < 20) and (abs(rgba[2] - color[2]) < 20):
                return self.colors[color]
        return 'ERROR: idk'
    
    ## takes pixels from each square of the grid
    ## gameState imgSize is 250 x 500
    ## this version of tetris is 10 x 20 blocks so each block is 25 pixels
    ## returns dictionary of {pos: (x, y), piece: Piece}
    def getGameGrid(self):

        pixelMap = self.gameStateImg.load()

        ## this representation of the game grid has 0,0 at the top left corner
        gameGrid = {}
        posx = 0
        posy = 0

        ## getting pixel from each square
        for height in range(12, 500, 25):
            for width in range(12, 250, 25):
                rgb = pixelMap[width,height]
                gameGrid[(posx, posy)] = rgb
                if posy + 1 == 10:
                    posx += 1
                    posy = 0
                else:
                    posy += 1
        
        ## determining what piece in each square
        for key in gameGrid:
            gameGrid[key] = self.determinePiece(gameGrid[key])
        return gameGrid





