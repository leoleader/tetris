from screencapture import ScreenCap
import time
import pyautogui

class Controller:
    sc = ScreenCap()

    controls = ['up', 'down', 'left', 'right', 'space', 'shift']

    def runAI(self):
        ## wait 1 second, then loop for 30 seconds
        ## currently takeImage runs at 2 frames a second LOL
        time.sleep(1)
        t_end = time.time() + 60 * .5
        tick = 0
        while time.time() < t_end:  
            self.sc.takeImage()
            tick += 1
        print('ticks: ' + str(tick))
    
    ## testing pyautogui works (it does)
    def hands(self):
        pyautogui.PAUSE = .2
        t_end = time.time() + 60 * .1
        while time.time() < t_end:  
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




 