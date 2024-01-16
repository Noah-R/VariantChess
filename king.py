from piece import Piece

class King(Piece):
    def __init__(self, isWhite = True, x = 0, y = 0):
        s = "k"
        if(isWhite):
            s = "K"
        super().__init__(isWhite, x, y, s)