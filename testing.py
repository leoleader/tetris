import os
from screencapture import TetrisAI
from PIL import Image


def testNextPiece():
    
    directory = os.fsencode('../tetris/images/NextPiece')
    ai = TetrisAI()

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print(filename)
        im = Image.open('../tetris/images/NextPiece/' + str(filename), 'r')
        nextPieceColor = im.getpixel((55, 50))
        print(nextPieceColor)
        print("the next piece is: " + str(ai.determinePiece(nextPieceColor)))

testNextPiece()