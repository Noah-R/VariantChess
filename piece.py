class Piece:
    def __init__(self, isWhite = True, x = 0, y = 0, string = ""):
        self.isWhite = isWhite
        self.x = x
        self.y = y
        self.string = string

    def __str__(self):
        return self.string