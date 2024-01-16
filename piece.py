class Piece:
    def __init__(self, color = "white", x = 0, y = 0):
        self.color = color
        self.x = x
        self.y = y

    def __str__(self):
        if(self.color == "white"):
            return "X"
        return "x"