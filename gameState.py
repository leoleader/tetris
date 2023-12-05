

## class to represent GameState object
## consists of: cartestian grid of either filled or empty squares, current piece, next piece, held piece, score

class GameState:
    grid = []
    score = None
    nextPiece = None
    currPiece = None
    heldPiece = None