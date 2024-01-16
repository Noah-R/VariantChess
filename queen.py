from piece import Piece

class Queen(Piece):
    def __init__(self, isWhite = True, x = 0, y = 0):
        s = "q"
        if(isWhite):
            s = "Q"
        super().__init__(isWhite, x, y, s)