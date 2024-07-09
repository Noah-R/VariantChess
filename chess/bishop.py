from piece import Piece

class Bishop(Piece):
    def __init__(self, isWhite = True, x = 0, y = 0, hasMoved = False):
        self.lightSquare = (x + y) % 2 == 1
        super().__init__(isWhite, x, y, hasMoved)
    
    def __str__(self):
        if self.isWhite:
            return "B"
        return "b"
        
    
    def listMoves(self, game):
        return super().listMoves(game, directions = [(-1, 1), (1, -1), (-1, -1), (1, 1)])