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

class TetrisAI:

    ## images to be taken
    gameState = None 
    scoreImg = None
    nextPiece = None

    # values
    score = None

    ## setting up piece identification by RGB value
    ## note: line piece RGB value is not orange because its only one that has a 
    ## shape that doesnt use the pixel I chose for next piece
    colors = {}
    colors[(170, 104, 61, 255)] = Pieces.ORGL
    colors[(81,63,166,255)] = Pieces.PURPLEL
    colors[(142, 179, 73, 255)] = Pieces.GREENSTEP
    colors[(182 ,53 ,61 ,255)] = Pieces.REDSTEP
    colors[(164, 62, 154, 255)] = Pieces.PINKT
    colors[(0, 1, 3, 255)] = Pieces.LINE
    colors[(214, 192, 103, 255)] = Pieces.SQUARE
    ## grabs images of gameState, nextPiece, and score
    ## resolution = 1980 x 1080
    def takeImage(self): 
        
        global gameState, nextPiece, scoreImg, score
        time.sleep(1)

        ## gameState imgSize is 250 x 470
        ## this version of tetris is 10 x 20 blocks so each block is about 25 pixels
        gameState = ImageGrab.grab(bbox = (595, 230, 845, 725)) 

        ## this is a 100 x 350 image
        nextPiece = ImageGrab.grab(bbox =((875, 250, 975, 600))) 

        ## going to keep nextpiece simple for now and just look at first next piece
        ## just get pixel color then figure out the piece since each piece is its own color
        nextPieceColor = nextPiece.getpixel((55, 50))
        print("the next piece is: " + self.determinePiece(nextPieceColor))

        scoreImg = ImageGrab.grab(bbox =(875, 650, 975, 700)) 
        ## score is easy, using pytesseract to get the number from the image
        score = pytesseract.image_to_string(scoreImg, config='--psm 6')
        if '\n' in score:
            score = score[0:len(score)-1]
        print('the current score is: ' + str(score))

    ## from the given rgba value determines what the next piece is
    ## returns 
    def determinePiece(self, rgba):
        for color in self.colors:
            if (abs(rgba[0] - color[0]) < 20) and (abs(rgba[1] - color[1]) < 20) and (abs(rgba[2] - color[2]) < 20):
                return self.colors[color]
        return 'ERROR: idk'
    
# testing 
ai = TetrisAI()
ai.takeImage() 


    ## reading the images

    ## gamestate is going to be hardest, going to need to map out a pixel from each square in the grid
    ## and then use the colors to reconstruct where all the pieces are




