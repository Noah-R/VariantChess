from piece import Piece

class Knight(Piece):
    def __init__(self, isWhite = True, x = 0, y = 0):
        s = "n"
        if(isWhite):
            s = "N"
        super().__init__(isWhite, x, y, s)