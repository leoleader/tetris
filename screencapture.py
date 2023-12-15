from PIL import ImageGrab, Image
from mss import mss
import pytesseract
import pieces


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
    colors[(192, 135, 97)] = pieces.OrangeL()
    colors[(113, 101, 181,255)] = pieces.PurpleL()
    colors[(167, 200, 104, 255)] = pieces.GreenStep()
    colors[(189, 98, 100 ,255)] = pieces.RedStep()
    colors[(175, 104, 174, 255)] = pieces.PinkT()
    colors[(87, 160, 126)] = pieces.Line()
    colors[(186, 169, 93, 255)] = pieces.Square()
    colors[(2, 2, 2, 255)] = pieces.Pieces.EMPTY

    ## grabs images of gameState, nextPiece, and score
    ## then uses helper methods / libraries to get data from images
    ## returns an array of [gameGrid: [], nextPiece: Piece, score: int]
    def takeImage(self): 

        with mss() as sct:
            screenshot1 = sct.grab({'left': 595, 'top': 225, 'width': 250, 'height': 500})
            screenshot3 = sct.grab({'left': 875, 'top': 650, 'width': 100, 'height': 50})


        self.gameStateImg = Image.frombytes('RGB', screenshot1.size, screenshot1.rgb)
        gameGrid = self.getGameGrid()

        nextPiece = self.getNextPiece()
        print("the next piece is: " + str(nextPiece.piece))

        self.scoreImg = Image.frombytes('RGB', screenshot3.size, screenshot3.rgb)
        ## score is easy, using pytesseract to read the number from the image
        score = pytesseract.image_to_string(self.scoreImg, config='--psm 6')
        if '\n' in score:
            score = score[0:len(score)-1]
        print('the current score is: ' + str(score))
        return [gameGrid, nextPiece, score]

    def getNextPiece(self):
        with mss() as sct:
            screenshot = sct.grab({'left': 875, 'top': 250, 'width': 100, 'height': 350})
        self.nextPieceImg = Image.frombytes('RGB', screenshot.size, screenshot.rgb)
        print('bruh: ' + str(self.nextPieceImg.size))

        ## going to keep nextpiece simple for now and just look at first next piece
        ## just get pixel color then figure out the piece since each piece is its own color
        nextPieceColor = self.nextPieceImg.getpixel((105, 75))
        print(nextPieceColor)
        ## accounting for line being positioned differently than rest
        nextPiece = self.determinePiece(nextPieceColor)
        return nextPiece

    ## from the given rgba value determines what the next piece is
    def determinePiece(self, rgba):
        print('color is: ' + str(rgba))
        for color in self.colors:
            if (abs(rgba[0] - color[0]) < 30) and (abs(rgba[1] - color[1]) < 30) and (abs(rgba[2] - color[2]) < 30):
                return self.colors[color]
        print('uh oh')
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
        for height in range(24, 1000, 50):
            for width in range(24, 500, 50):
                rgb = pixelMap[width,height]
                gameGrid[(posx, posy)] = rgb
                if posy + 1 == 10:
                    posx += 1
                    posy = 0
                else:
                    posy += 1
        
        ## determining what piece in each square
        for key in gameGrid:
            if ((gameGrid[key][0] < 45) and (gameGrid[key][1] < 45) and (gameGrid[key][2] < 45)):
                gameGrid[key] = pieces.Pieces.EMPTY
            else:
                gameGrid[key] = pieces.Square()
        return gameGrid
