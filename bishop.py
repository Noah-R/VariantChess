from piece import Piece

class Bishop(Piece):
    def __init__(self, isWhite = True, x = 0, y = 0):
        s = "b"
        if(isWhite):
            s = "B"
        super().__init__(isWhite, x, y, s)