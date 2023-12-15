import os
from screencapture import ScreenCap
from search import SearchProblem
from controller import Controller
from PIL import Image
from pieces import Pieces, PurpleL


def test_next_piece():
    
    directory = os.fsencode('../tetris/images/NextPiece')
    sc = ScreenCap()
    answers = {'cyanline.png': Pieces.LINE, 'greenstep.png': Pieces.GREENSTEP, 'orangel.png': Pieces.ORGL, 
               'pinkt.png': Pieces.PINKT, 'purplel.png': Pieces.PURPLEL, 'redstep.png': Pieces.REDSTEP, 'yellowsquare.png': Pieces.SQUARE}

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print(filename)
        im = Image.open('../tetris/images/NextPiece/' + str(filename), 'r')
        nextPieceColor = im.getpixel((105, 75))
        im.putpixel((105, 75), (255, 31, 61))
        #im.show()
        print(nextPieceColor)
        nextPiece = sc.determinePiece(nextPieceColor)
        print("the next piece is: " + str(nextPiece))
        assert nextPiece.piece == answers[filename]


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

#test_find_best_placements()
 
controller = Controller()
controller.runAILowGrav() 