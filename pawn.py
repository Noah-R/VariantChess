from piece import Piece

class Pawn(Piece):
    def __init__(self, isWhite = True, x = 0, y = 0):
        s = "p"
        if(isWhite):
            s = "P"
        super().__init__(isWhite, x, y, s)