from piece import Piece

class Queen(Piece):
    def __init__(self, isWhite = True, x = 0, y = 0, moved = False):
        super().__init__(isWhite, x, y, moved)
    
    def __str__(self):
        if self.isWhite:
            return "Q"
        return "q"
    
    
    def listMoves(self, board):
        return super().listMoves(board, directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (-1, -1), (1, 1)])