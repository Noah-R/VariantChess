from piece import Piece

class Rook(Piece):
    def __init__(self, isWhite = True, x = 0, y = 0):
        s = "r"
        if(isWhite):
            s = "R"
        super().__init__(isWhite, x, y, s)
    
    def listMoves(self, board):
        return super().listMoves(board, directions = [(0, 1), (1, 0), (0, -1), (-1, 0)])