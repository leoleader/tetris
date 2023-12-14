import time
import pyautogui

from screencapture import ScreenCap
from search import SearchProblem
from pieces import Pieces


## Manages the screencapture, image->data conversion, and gameState
class Controller:

    # current gamestate values, gotten from sc.takeImage()
    gameGrid = None
    currPiece = None
    nextPiece = None
    score = None

    ## initializing sc and gs
    sc = ScreenCap()

    ## initializing controls
    controls = ['up', 'down', 'left', 'right', 'space', 'shift']

    ## takes sc image, sets gamestate values
    def getGameState(self):
        state_vals = self.sc.takeImage()
        self.gameGrid = state_vals[0]
        self.nextPiece = state_vals[1]
        self.score = state_vals[2]

    ## test method to run AI with low gravity
    def runAILowGrav(self):
        ## wait 2 seconds, then loop for 30 seconds
        ## currently takeImage runs at 2 frames a second LOL
        time.sleep(2)
        end_time = time.time() + 60 * 2
        start_time = time.time()
        tick = 0
        ## rn just gonna ignore first piece and space it
        self.currPiece = self.sc.getNextPiece()
        print('starting piece is: ' + str(self.currPiece))
        pyautogui.press('space')
        ## begin play
        while time.time() < end_time:  
            time.sleep(.3)
            self.getGameState()
            self.sc.gameStateImg.save(f'/Users/dylanmccann/tetris/images/Search/search{tick}.png')
            search = SearchProblem(self.gameGrid, self.nextPiece, self.currPiece, self.score)
            valid_locs = search.findValidPlacements(self.gameGrid, self.currPiece)
            ranked_locs = search.findBestPlacement2(valid_locs, self.currPiece)
            path = search.findOptimalPath(ranked_locs)
            self.executePath(path)
            self.currPiece = self.nextPiece
            tick += 1
        print('ticks: ' + str(tick))
        print('time elapsed: ' + str(end_time - start_time))
    

    ##########################################################################

    
    ## takes in a list of actions (keys) and then executes them
    ## add feature to replace list of downs with single space press
    def executePath(self, actions):
        pyautogui.PAUSE = 0.1
        while len(actions) > 0:
            if 'left' in actions or 'right' in actions or 'up' in actions:
                action = actions.pop(0)
                pyautogui.press(action)
            else:
                pyautogui.press('space')
                break

    
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
