from piece import Piece

class Knight(Piece):
    def __init__(self, color = "white", x = 0, y = 0):
        super().__init__(color, x, y)

    def __str__(self):
        if(self.color == "white"):
            return "N"
        return "n"