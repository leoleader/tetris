import time
import pyautogui

from screencapture import ScreenCap
from pieces import Pieces


## Manages the screencapture, image->data conversion, and gameState
class Controller:

    # current gamestate values, gotten from sc.takeImage()
    gameGrid = None
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

    ## test method to run AI
    def runAI(self):
        ## wait 1 second, then loop for 30 seconds
        ## currently takeImage runs at 2 frames a second LOL
        time.sleep(1)
        end_time = time.time() + 60 * .5
        start_time = time.time()
        tick = 0
        while time.time() < end_time:  
            self.getGameState()
            self.printGameState()
            tick += 1
        print('ticks: ' + str(tick))
        print('time elapsed: ' + str(end_time - start_time))
    

    ##########################################################################

    ## testing pyautogui works (it does)
    def hands(self):
        pyautogui.PAUSE = .2
        end_time = time.time() + 60 * .1
        while time.time() < end_time:  
            pyautogui.press('shift')
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('space')
    
    ## takes in a list of actions (keys) and then executes them
    def executePath(self, actions):
        time.sleep(1)
        pyautogui.PAUSE = .01
        for action in actions:
            pyautogui.press(action)

    
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




controller = Controller()
controller.runAI()