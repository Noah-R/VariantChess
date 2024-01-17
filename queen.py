from piece import Piece

class Queen(Piece):
    def __init__(self, isWhite = True, x = 0, y = 0):
        s = "q"
        if(isWhite):
            s = "Q"
        super().__init__(isWhite, x, y, s)
    
    
    def listMoves(self, board):
        return super().listMoves(board, directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (-1, -1), (1, 1)])