# tetris

# CS 4100 Final Project - Tetris AI

Current Status: Search problem works well, ML still work in progress

[First Time Playing](https://drive.google.com/file/d/1yLJpew49aWK2GLV6rdkJCKcbWQKFBY0B/view?usp=sharing)

Project RunDown:
Tetris AI that plays the game for you! 

# Program Functionality:
- Continuously takes images of game state using PIL
- Reads and manipulate image pixel data to pull info like
    - Current Piece
    - Next Piece
    - Block Locations
    - Held Piece
- Uses pytesseract to get current score
- Converts pulled gamestate info into gameState class object

- Search Method: 
- Uses gameState object and formulated search problem to find:
    - Optimal Piece Location
    - Optimal Path to End Location (A* Search Algorithm)
- Converts path to series of keyboard commands and executes using pyautogui

Reinforcement Learning:
- Determine key heuristics to playing Tetris in addition to current basic heuristics
- Use ML techniques to train AI to find optimal heuristic values
- Compare performance with and without usage of ML


# Try it yourself! :
- In one fullscreen window pull up tetr.io
- In another window pull up ur code editor of choice
    - Clone the repo and open locally
    - pip install project dependencies
    - open bot.py
    - hit run
- Now go back to tetr.io and play a game
- Once the game starts the bot should kick in and start playing!

NOTE: The usage of this bot to cheat in any form of competitive Tetris matches/modes is NOT condoned!



NOTE TO SELF: 
eventually when need update requirements.txt, use pipreqs \path --force
