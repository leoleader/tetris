# tetris

# CS 4100 Final Project - Tetris AI

Current Status: Search problem works pretty good, ML still work in progress

[First Time Working](https://drive.google.com/file/d/1yLJpew49aWK2GLV6rdkJCKcbWQKFBY0B/view?usp=sharing)

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

Search Method: 
- Uses gameState object and formulated search problem to find:
    - Optimal Piece Location
    - Optimal Path to End Location (A* Search Algorithm)
- Converts path to series of keyboard commands and executes using pyautogui

ML:
- Reinforcement Learning, Trained using custom mode
- Chosen Features: Score, Line Height, Holes, Held Piece, ...
- Find optimal heuristic values through ML techniques


# Try it yourself! :
- In one fullscreen window pull up tetr.io
- In another window pull up ur code editor of choice
    - Clone the repo and open locally
    - pip install project dependencies
    - open bot.py
    - hit run
- Now go back to tetr.io and play a game
- Once the game starts the bot should kick in and start playing!

NOTE: The usage of this bot to cheat in any form of competitive Tetris matches/modes is NOT condoned

