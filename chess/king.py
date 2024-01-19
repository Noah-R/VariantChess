from piece import Piece
from rook import Rook

class King(Piece):
    def __init__(self, isWhite = True, x = 0, y = 0, moved = False):
        super().__init__(isWhite, x, y, moved)
    
    def __str__(self):
        if self.isWhite:
            return "K"
        return "k"

    def listMoves(self, board):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (-1, -1), (1, 1)]
        options = []
        for direction in directions:
            x = self.x + direction[0]
            y = self.y + direction[1]
            if(x > -1 and y > -1 and x < 8 and y < 8):
                square = board[y][x]
                if(square == None or square.isWhite != self.isWhite):
                    options.append((y, x, ""))
        
        if(not self.moved):
            castles = [(1, 8, 6, "O-O"), (-1, -1, 2, "O-O-O")]
            for castle in castles:
                for x in range(self.x + castle[0], castle[1], castle[0]):
                    if(board[self.y][x] != None):
                        piece = board[self.y][x]
                        if(type(piece) == Rook and not piece.moved and piece.isWhite == self.isWhite):
                            options.append((self.y, castle[2], castle[3]))
                        break
            
        return options