from pieces import TetrisPiece, Pieces
from queue import PriorityQueue
## class to handle all of the search algorithm shit

class SearchProblem():

    def __init__(self, gameGrid, nextPiece, currentPiece, score):
        self.gameGrid = gameGrid
        self.nextPiece = nextPiece
        self.currentPiece: TetrisPiece = currentPiece
        self.score = score
    
    ## basically going to overlay root of shape of currnet piece on each square in grid 
    ## and see if shape can fit there. 
    ## going to do this for all 4 rotations of the piece
    ## then return a list of valid placements
    def findValidPlacements(self, gameGrid, currentPiece: TetrisPiece):
        valid_locs = []
        for rotation in range(4):
            if rotation > 0:
                currentPiece.rotatePiece()
            for key in gameGrid:
                currentPiece.updateX(key[0])
                currentPiece.updateY(key[1])
                piece_coords = currentPiece.getPieceLocations()
                valid = True
                floor = False
                ## determining if piece location valid, (not overlapping with other pieces, in grid boundaries, has floor)
                for coord in piece_coords:
                    if (coord[0] < 0) or (coord[0] > 19) or (coord[1] < 0) or (coord[1] > 9):
                        valid = False
                    elif (gameGrid[(coord[0], coord[1])] != Pieces.EMPTY):
                        valid = False
                    elif coord[0] == 19:
                        floor = True
                    elif gameGrid[(coord[0] + 1, coord[1])] != Pieces.EMPTY:
                        floor = True
                if floor and valid:
                    valid_locs.append((key, currentPiece.rotate))
        return valid_locs

    ## determining best placements based on: overall average line height, holes, and if any rows complete
    ## return list of placements with highest score first
    def findBestPlacement(self, placements, currentPiece: TetrisPiece):
        ranking = []
        for placement in placements:
            rating = 0
            currentPiece.updateX(placement[0][0])
            currentPiece.updateY(placement[0][1])
            while currentPiece.rotate != placement[1]:
                currentPiece.rotatePiece()
            piece_coords = currentPiece.getPieceLocations()
            avg_height = 0
            for coord in piece_coords:
                avg_height += coord[0]
            avg_height = avg_height / 4
            rating = avg_height
            ranking.append((rating, placement))
        
        ## sort ranking highest to lowest
        self.sortRanks(ranking, 0, len(ranking)-1)
        print(ranking)
        return ranking
    
    ## using mergesort to sort, sorts in O(nlogn) 
    def sortRanks(self, arr, l, r):
        if l < r:
            
            ## midpoint
            m = l+(r-l)//2
    
            # Sort first and second halves then merge
            self.sortRanks(arr, l, m)
            self.sortRanks(arr, m+1, r)
            self.merge(arr, l, m, r)
    
    ## helper for mergesort
    def merge(self, arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m
    
        # create temp arrays
        L = [0] * (n1)
        R = [0] * (n2)
    
        # Copy data to temp arrays L[] and R[]
        for i in range(0, n1):
            L[i] = arr[l + i]
    
        for j in range(0, n2):
            R[j] = arr[m + 1 + j]
    
        # Merge the temp arrays back into arr[l..r]
        i = 0     # Initial index of first subarray
        j = 0     # Initial index of second subarray
        k = l     # Initial index of merged subarray
    
        while i < n1 and j < n2:
            if L[i][0] <= R[j][0]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
    
        # Copy the remaining elements of L[], if there
        # are any
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
    
        # Copy the remaining elements of R[], if there
        # are any
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    ## given state ((x, y), t), returns list of possible next states using valid actions
    def getSuccessors(self, state):
        successors = []
        for action in ['left', 'right', 'down']:
            if action == 'left':
                pos = state[0]
                newpos = (pos[0], pos[1] - 1)
                piece = self.currentPiece.newPiece(newpos, state[1])
                if piece.isValid(self.gameGrid):
                    successors.append(((newpos, state[1]), action))
            if action == 'right':
                pos = state[0]
                newpos = (pos[0], pos[1] + 1)
                piece = self.currentPiece.newPiece(newpos, state[1])
                if piece.isValid(self.gameGrid):
                    successors.append(((newpos, state[1]), action))
            if action == 'down':
                pos = state[0]
                newpos = (pos[0] + 1, pos[1])
                piece = self.currentPiece.newPiece(newpos, state[1])
                if piece.isValid(self.gameGrid):
                    successors.append(((newpos, state[1]), action))
        return successors
        


    ## A*. Have start pos and end pos and want find shortest path between two
    ## state represented by (path_length, ((x,y) t), [actions taken])
    ## currently possible actions simplified to left right down, (will implement hold and rotate later maybe)
    def findOptimalPath(self, end_goals):

        ## from findBestPlacement, list of all valid placements sorted by quality (heuristic)
        end_goals = end_goals
        solution_path = None

        while solution_path is None:

            if len(end_goals) == 0:
                ## couldnt find any path, so just slam down a piece I guess
                return ['space']
            end_goal = end_goals.pop()

            ## rotating piece to match endgoal
            rotation = end_goal[1][1]
            print('rotation: ' + str(rotation))
            path_start = ['up'] * rotation
            print(path_start)
            
            ## initializing
            start_state = (0, ((-2, 4), rotation), []) #need to figure out how doing this lol
            frontier = PriorityQueue()
            frontier.put(start_state)
            explored_set = []
            solution_set = []

            while len(solution_set) == 0:

                if frontier.empty():
                    solution_set = ["fail"]
            
                curr_node = frontier.get()
                explored_set.append(curr_node[1])

                if curr_node[1] == end_goal[1]:
                    solution_set = curr_node[2]
                
                for node in self.getSuccessors(curr_node[1]):
                    nextnode = (curr_node[0] + 1, node[0], curr_node[2] + [node[1]])
                    if nextnode[1] not in explored_set:
                        nodeinfrontier = False
                        for nodey in frontier.queue:
                            if nodey[1] == nextnode[1]:
                                nodeinfrontier = True
                                if nodey[0] > nextnode[0]:
                                    frontier.queue.remove(nodey)
                                    frontier.put(nextnode)
                                continue
                        if not nodeinfrontier:
                            frontier.put(nextnode)
        
            if solution_set != ['fail']:
                solution_path = path_start + solution_set + ['space']
                print(solution_path)
        
        return solution_path
            
