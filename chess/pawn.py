from piece import Piece

class Pawn(Piece):
    def __init__(self, isWhite = True, x = 0, y = 0, hasMoved = False):
        super().__init__(isWhite, x, y, hasMoved)
    
    def __str__(self):
        if self.isWhite:
            return "P"
        return "p"
    
    def promote(self, pieceType):
        return pieceType(self.isWhite, self.x, self.y)

    def listMoves(self, board):
        options = []
        direction = 1
        if(not self.isWhite):
            direction = -1
        
        x = self.x
        y = self.y + direction
        square = board[y][x]
        if(square == None):
            if(y == 0 or y == 7):
                options.append((y, x, "Q"))
                options.append((y, x, "R"))
                options.append((y, x, "B"))
                options.append((y, x, "N"))
            else:
                options.append((y, x, ""))
            if((self.isWhite and self.y == 1) or (not self.isWhite and self.y == 6)):
                y += direction
                square = board[y][x]
                if(square == None):
                    options.append((y, x, ""))
        
        y = self.y + direction
        for x in [self.x + 1, self.x-1]:
            if(x > -1 and x < 8):
                square = board[y][x]
                if(square != None and square.isWhite != self.isWhite):
                    if(y == 0 or y == 7):
                        options.append((y, x, "Q"))
                        options.append((y, x, "R"))
                        options.append((y, x, "B"))
                        options.append((y, x, "N"))
                    else:
                        options.append((y, x, ""))

        return options