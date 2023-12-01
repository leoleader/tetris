import os
from screencapture import ScreenCap
from controller import Controller
from PIL import Image


def testNextPiece():
    
    directory = os.fsencode('../tetris/images/NextPiece')
    ai = ScreenCap()

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print(filename)
        im = Image.open('../tetris/images/NextPiece/' + str(filename), 'r')
        nextPieceColor = im.getpixel((55, 50))
        print(nextPieceColor)
        print("the next piece is: " + str(ai.determinePiece(nextPieceColor)))

testNextPiece()


def testController():
    controller = Controller()
    ##controller.runAI()
    ##controller.hands()
    test = []
    test.extend(['up' for i in range(100)])
    test.append(['space'])
    ##controller.executePath(test)