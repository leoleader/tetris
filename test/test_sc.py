import os
from screencapture import ScreenCap
from PIL import Image
from pieces import Pieces


def test_next_piece():
    
    directory = os.fsencode('../tetris/images/NextPiece')
    sc = ScreenCap()
    answers = [Pieces.LINE, Pieces.GREENSTEP, Pieces.ORGL, Pieces.PINKT, Pieces.PURPLEL, Pieces.REDSTEP, Pieces.SQUARE]

    i = -1
    for file in os.listdir(directory):
        i += 1
        filename = os.fsdecode(file)
        print(filename)
        im = Image.open('../tetris/images/NextPiece/' + str(filename), 'r')
        nextPieceColor = im.getpixel((55, 50))
        print(nextPieceColor)
        nextPiece = sc.determinePiece(nextPieceColor)
        print("the next piece is: " + str(nextPiece))
        assert nextPiece == answers[i]
