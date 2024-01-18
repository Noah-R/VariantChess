from piece import Piece

class Bishop(Piece):
    def __init__(self, isWhite = True, x = 0, y = 0, moved = False):
        super().__init__(isWhite, x, y, moved)
    
    def __str__(self):
        if self.isWhite:
            return "B"
        return "b"
        
    
    def listMoves(self, board):
        return super().listMoves(board, directions = [(-1, 1), (1, -1), (-1, -1), (1, 1)])