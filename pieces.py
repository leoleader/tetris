from abc import ABC, abstractmethod 

class Pieces:
    ORGL = 'Orange L Piece' 
    PURPLEL = 'Purple L Piece'
    GREENSTEP = 'Green Step Piece'
    REDSTEP = 'Red Step Piece'
    PINKT = 'Pink T Piece'
    LINE = 'CYAN Line Piece'
    SQUARE = 'Gold Square Piece'
    EMPTY = 'Empty Square'
  
class TetrisPiece(ABC): 

    def __init__(self, root=(0,0), rotation=0):
        self.piece = None
        self.shapes = []
        self.curr_shape = None

        self.rotate = rotation
        self.root_x = root[0]
        self.root_y = root[1]

  
    @abstractmethod
    def rotatePiece(self): 
        pass

    @abstractmethod
    def moveright(self):
        self.root_x += 1

    @abstractmethod
    def moveleft(self):
        self.root_x -= 1
    
    @abstractmethod
    def updateX(self, x):
        self.root_x = x

    @abstractmethod
    def updateY(self, y):
        self.root_y = y

    @abstractmethod
    def moveright(self):
        self.root_y += 1
    
    @abstractmethod
    def getPieceLocations(self):
        locations = []
        for thing in self.shape:
            locations.append((self.root_x + thing[0], self.root_y + thing[1]))
        return locations
    
    
    @abstractmethod
    def printPiece(self):
        for x in range(-3, 3):
            row = ''
            for y in range(-3, 3):
                row += '| '
                if (x,y) in self.shape:
                    row += 'X '
                else:
                    row += '  '
            row += '|'
            print(row)
            print('-------------------' * 2)
        
    
## square piece, rotate doesn't do anything
class Square(TetrisPiece): 

    def __init__(self):
        super().__init__()
        self.piece = Pieces.SQUARE
        self.shape = [(0,0), (0,1), (1,0), (1,1)]
        self.shapes = [[(0,0), (0,1), (1,0), (1,1)],
                       [(0,0), (0,1), (1,0), (1,1)],
                       [(0,0), (0,1), (1,0), (1,1)],
                       [(0,0), (0,1), (1,0), (1,1)]]
  
    # overriding abstract method 
    def rotatePiece(self): 
        self.rotate = (self.rotate + 1) % 4
    
    def moveleft(self):
        return super().moveleft()
    
    def moveright(self):
        return super().moveright()
    
    def updateX(self, x):
        return super().updateX(x)
    
    def updateY(self, y):
        return super().updateY(y)
    
    def printPiece(self):
        return super().printPiece()
    
    def getPieceLocations(self):
        return super().getPieceLocations()

## PurpleL
class PurpleL(TetrisPiece): 

    def __init__(self):
        super().__init__()
        self.piece = Pieces.PURPLEL
        self.shapes = [[(0,0), (0, 1), (0, -1), (-1,-1)],
                       [(0,0), (1,0), (-1,0), (-1,1)],
                       [(0,0), (0, -1), (0, 1), (1,1)],
                       [(0,0), (-1, 0), (1, 0), (1,-1)]]
        self.shape = self.shapes[self.rotate]
  
    # overriding abstract method 
    def rotatePiece(self): 
        if self.rotate == 0:
            self.shape = [(0,0), (1,0), (-1,0), (-1,1)]
        elif self.rotate == 1:
            self.shape = [(0,0), (0, -1), (0, 1), (1,1)]
        elif self.rotate == 2:
            self.shape = [(0,0), (-1, 0), (1, 0), (1,-1)]
        elif self.rotate == 3:
            self.shape = [(0,0), (0, 1), (0, -1), (-1,-1)]
        self.rotate = (self.rotate + 1) % 4
    
    
    def moveleft(self):
        return super().moveleft()
    
    def moveright(self):
        return super().moveright()
    
    def updateX(self, x):
        return super().updateX(x)
    
    def updateY(self, y):
        return super().updateY(y)
    
    def printPiece(self):
        return super().printPiece()
    
    def getPieceLocations(self):
        return super().getPieceLocations()

## Orange L
class OrangeL(TetrisPiece): 

    def __init__(self):
        super().__init__()
        self.piece = Pieces.ORGL
        self.shapes = [[(0,0), (0, 1), (0, -1), (-1, 1)],
                       [(0,0), (1,0), (-1,0), (1,1)],
                       [(0,0), (0, -1), (0, 1), (1,-1)],
                       [(0,0), (-1, 0), (1, 0), (-1,-1)]]
        self.shape = self.shapes[self.rotate]
  
    # overriding abstract method 
    def rotatePiece(self): 
        if self.rotate == 0:
            self.shape = [(0,0), (1,0), (-1,0), (1,1)]
        elif self.rotate == 1:
            self.shape = [(0,0), (0, -1), (0, 1), (1,-1)]
        elif self.rotate == 2:
            self.shape = [(0,0), (-1, 0), (1, 0), (-1,-1)]
        elif self.rotate == 3:
            self.shape = [(0,0), (0, 1), (0, -1), (-1,1)]
        self.rotate = (self.rotate + 1) % 4
    
    def moveleft(self):
        return super().moveleft()
    
    def moveright(self):
        return super().moveright()
    
    def updateX(self, x):
        return super().updateX(x)
    
    def updateY(self, y):
        return super().updateY(y)
    
    def printPiece(self):
        return super().printPiece()
    
    def getPieceLocations(self):
        return super().getPieceLocations()

## GreenStep
class GreenStep(TetrisPiece): 

    def __init__(self):
        super().__init__()
        self.piece = Pieces.GREENSTEP
        self.shapes = [[(0,0), (0, -1), (-1, 0), (-1, 1)],
                       [(0,0), (-1,0), (0,1), (1,1)],
                       [(0,0), (0, 1), (1, 0), (1,-1)],
                       [(0,0), (1, 0), (0, -1), (-1,-1)]]
        self.shape = self.shapes[self.rotate]
  
    # overriding abstract method 
    def rotatePiece(self): 
        if self.rotate == 0:
            self.shape = [(0,0), (-1,0), (0,1), (1,1)]
        elif self.rotate == 1:
            self.shape = [(0,0), (0, 1), (1, 0), (1,-1)]
        elif self.rotate == 2:
            self.shape = [(0,0), (1, 0), (0, -1), (-1,-1)]
        elif self.rotate == 3:
            self.shape = [(0,0), (0, -1), (-1, 0), (-1, 1)]
        self.rotate = (self.rotate + 1) % 4
    
    def moveleft(self):
        return super().moveleft()
    
    def moveright(self):
        return super().moveright()
    
    def updateX(self, x):
        return super().updateX(x)
    
    def updateY(self, y):
        return super().updateY(y)
    
    def printPiece(self):
        return super().printPiece()
    
    def getPieceLocations(self):
        return super().getPieceLocations()

## RedStep
class RedStep(TetrisPiece): 

    def __init__(self):
        super().__init__()
        self.piece = Pieces.REDSTEP
        self.shapes = [[(0,0), (0, 1), (-1, 0), (-1, -1)],
                       [(0,0), (0, 1), (-1, 1), (1, 0)],
                       [(0,0), (1, 0), (1,1), (0, -1)],
                       [(0,0), (0, -1), (1, -1), (-1, 0)]]
        self.shape = self.shapes[self.rotate]
  
    # overriding abstract method 
    def rotatePiece(self): 
        if self.rotate == 0:
            self.shape = [(0,0), (0, 1), (-1, 1), (1, 0)]
        elif self.rotate == 1:
            self.shape = [(0,0), (1, 0), (1,1), (0, -1)]
        elif self.rotate == 2:
            self.shape = [(0,0), (0, -1), (1, -1), (-1, 0)]
        elif self.rotate == 3:
            self.shape = [(0,0), (0, 1), (-1, 0), (-1, -1)]
        self.rotate = (self.rotate + 1) % 4
    
    def moveleft(self):
        return super().moveleft()
    
    def moveright(self):
        return super().moveright()
    
    def updateX(self, x):
        return super().updateX(x)
    
    def updateY(self, y):
        return super().updateY(y)
    
    def printPiece(self):
        return super().printPiece()
    
    def getPieceLocations(self):
        return super().getPieceLocations()

## Pink T
class PinkT(TetrisPiece): 

    def __init__(self):
        super().__init__()
        self.piece = Pieces.PINKT
        self.shape = [(0,0), (0, -1), (0, 1), (-1, 0)]
        self.shapes = [[(0,0), (0, -1), (0, 1), (-1, 0)],
                       [(0,0), (1, 0), (0, 1), (-1, 0)],
                       [(0,0), (1, 0), (0, 1), (0, -1)],
                       [(0,0), (0, -1), (-1, 0), (1, 0)]]
        self.shape = self.shapes[self.rotate]
  
    # overriding abstract method 
    def rotatePiece(self): 
        if self.rotate == 0:
            self.shape = [(0,0), (1, 0), (0, 1), (-1, 0)]
        elif self.rotate == 1:
            self.shape = [(0,0), (1, 0), (0, 1), (0, -1)]
        elif self.rotate == 2:
            self.shape = [(0,0), (0, -1), (-1, 0), (1, 0)]
        elif self.rotate == 3:
            self.shape = [(0,0), (0, -1), (0, 1), (-1, 0)]
        self.rotate = (self.rotate + 1) % 4
    
    def moveleft(self):
        return super().moveleft()
    
    def moveright(self):
        return super().moveright()
    
    def updateX(self, x):
        return super().updateX(x)
    
    def updateY(self, y):
        return super().updateY(y)
    
    def printPiece(self):
        return super().printPiece()
    
    def getPieceLocations(self):
        return super().getPieceLocations()


## Line is built so that root point is stationary even if when rotated is no 
## longer contained in piece
class Line(TetrisPiece): 

    def __init__(self):
        super().__init__()
        self.piece = Pieces.LINE
        self.shape = [(0,0), (0, 1), (0, 2), (0, 3)]
        self.shapes = [[(0,0), (0, 1), (0, 2), (0, 3)],
                       [(0,2), (-1, 2), (1, 2), (2, 2)],
                       [(1,0), (1, 1), (1, 2), (1, 3)],
                       [(0,1), (-1, 1), (1, 1), (2, 1)]]
        self.shape = self.shapes[self.rotate]
  
    # overriding abstract method 
    def rotatePiece(self): 
        if self.rotate == 0:
            self.shape = [(0,2), (-1, 2), (1, 2), (2, 2)]
        elif self.rotate == 1:
            self.shape = [(1,0), (1, 1), (1, 2), (1, 3)]
        elif self.rotate == 2:
            self.shape = [(0,1), (-1, 1), (1, 1), (2, 1)]
        elif self.rotate == 3:
            self.shape = [(0,0), (0, -1), (0, 1), (-1, 0)]
        self.rotate = (self.rotate + 1) % 4
    
    def moveleft(self):
        return super().moveleft()
    
    def moveright(self):
        return super().moveright()
    
    def updateX(self, x):
        return super().updateX(x)
    
    def updateY(self, y):
        return super().updateY(y)
    
    def printPiece(self):
        return super().printPiece()
    
    def getPieceLocations(self):
        return super().getPieceLocations()
