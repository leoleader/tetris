import os
from screencapture import ScreenCap
from search import SearchProblem
from controller import Controller
from PIL import Image
from pieces import Pieces, PurpleL


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


def test_find_valid_placements():
    sc = ScreenCap()
    bruh = sc.takeImage()
    nextPiece = bruh[1]
    grid = bruh[0]
    score = bruh[2]
    search = SearchProblem(grid, nextPiece, nextPiece, score)
    valid_locs = search.findValidPlacements(grid, nextPiece)
    print(valid_locs)

def test_find_best_placements():

    sc = ScreenCap()
    bruh = sc.takeImage()
    nextPiece = bruh[1]
    grid = bruh[0]
    score = bruh[2]

    search = SearchProblem(grid, nextPiece, nextPiece, score)
    valid_locs = search.findValidPlacements(grid, nextPiece)
    ranked_locs = search.findBestPlacement(valid_locs, nextPiece)

    search.findOptimalPath(ranked_locs)



#purpleL = PurpleL((1,1), 3)
#purpleL.printPiece()

test_find_best_placements()