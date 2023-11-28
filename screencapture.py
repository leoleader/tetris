import numpy as nm 
import time
  
# importing OpenCV 
# import cv2 
  
from PIL import ImageGrab, Image
import pytesseract
  
gameState = None 
scoreImg = None
nextPiece = None
score = None

## setting up piece identification by RGB value
colors = {}
colors[(0, 0, 244, 255)] = 'Navy Blue L piece'
colors[(186, 39, 245, 255)] = 'Purple L piece'
colors[(127, 201, 249, 255)] = 'Cyan step piece'
colors[(116, 250, 76, 255)] = 'light green step piece'
colors[(255, 254, 84, 255)] = 'yellow T piece'
colors[(236, 112, 45, 255)] = 'orange line piece'
colors[(233, 51, 35, 255)] = 'red square piece'

## grabs images of gameState, nextPiece, and score
def takeImage(): 
    global gameState, nextPiece, scoreImg, score
    time.sleep(1)

    ## width: 385 pixels, height: 715
    ## this version of tetris is 10 x 18 blocks so each block is about 39-40 pixels
    gameState = ImageGrab.grab(bbox = (325, 155, 710, 860)) 

    ## this is a 250 x 150 image
    nextPiece = ImageGrab.grab(bbox =(850, 150, 1100, 300)) 

    ## nextpiece is also straightforward, just going to get the color from the middle pixel and
    ## then figure out the piece since each piece is its own color
    nextPieceColor = nextPiece.getpixel((125, 75))
    print("the next piece is: " + colors[nextPieceColor])

    scoreImg = ImageGrab.grab(bbox =(1000, 545, 1200, 600)) 
    ## score is easy, using pytesseract to get the number from the image
    score = int(pytesseract.image_to_string(scoreImg, config='--psm 6'))
    print('the current score is: ' + str(score))

  
# testing 
takeImage() 
gameState.show()


## reading the images

## gamestate is going to be hardest, going to need to map out a pixel from each square in the grid
## and then use the colors to reconstruct where all the pieces are




